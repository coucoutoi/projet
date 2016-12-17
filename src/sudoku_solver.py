#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`sudoku_solver` module

:author: HULSKEN Alexandre & KARTI Adeniss

:date: 2016, november

This module provides sudoku solver's primitive operations

:Provides:

* `MAJ_hipothetic`
* `find_cell_min`
* `not_solved`
* `is_solved`
* `search_sol`
* `ens_cell0`
* `remove`
* `make_image`
"""


import os
from time import sleep
import sudoku_grid, cells
import random

##############################################
# Functions for grid's setup and management
##############################################

   #############
   # Variables #
   #############

sol_way, ens_sol, father, compt_rec = list(), set(), "SUDO", 0 #initialisation des variables globales qui nous servirons de sauvegarde dans le système résolution

# 3 grilles de sudoku qui ont permi de test aux fonctions
sud_notfinished = "490001007000045030382600050003070401800902005907030600030006529020850000500700013"
sud_finished = "495381267671245938382697154263578491814962375957134682738416529129853746546729813"
sud_2sol = '495381267671245938382697154263578400814962375957134682738426500129853746546791823'


   #############
   # Fonctions #
   #############

def MAJ_hipothetic(cell_list,hipo):
    """
    up-date the cells' hipothetics values of cell_list with the value of the other cells of cell_value

    :param cell_list: a list of cells
    :type cell_list: list
    :return: None
    :rtype: NoneType
    :Action: up-date the hipohtetics value of each cell of cell_list
    :UC: none
    :Examples:

    >>> cell_list = [cells.create() for i in range(9)]
    >>> for cell in cell_list: print(set(int(i) for i in cells.get_cellhipo(cell)))
    {1, 2, 3, 4, 5, 6, 7, 8, 9}
    {1, 2, 3, 4, 5, 6, 7, 8, 9}
    {1, 2, 3, 4, 5, 6, 7, 8, 9}
    {1, 2, 3, 4, 5, 6, 7, 8, 9}
    {1, 2, 3, 4, 5, 6, 7, 8, 9}
    {1, 2, 3, 4, 5, 6, 7, 8, 9}
    {1, 2, 3, 4, 5, 6, 7, 8, 9}
    {1, 2, 3, 4, 5, 6, 7, 8, 9}
    {1, 2, 3, 4, 5, 6, 7, 8, 9}
    >>> cells.set_cellvalue(cell_list[0],1)
    >>> MAJ_hipothetic(cell_list,'1')
    >>> for cell in cell_list: print(set(int(i) for i in cells.get_cellhipo(cell)))
    set()
    {2, 3, 4, 5, 6, 7, 8, 9}
    {2, 3, 4, 5, 6, 7, 8, 9}
    {2, 3, 4, 5, 6, 7, 8, 9}
    {2, 3, 4, 5, 6, 7, 8, 9}
    {2, 3, 4, 5, 6, 7, 8, 9}
    {2, 3, 4, 5, 6, 7, 8, 9}
    {2, 3, 4, 5, 6, 7, 8, 9}
    {2, 3, 4, 5, 6, 7, 8, 9}
    """
    for cell in cell_list:
        cells.unset_cellhipothetic(cell,hipo)

def find_cell_min(grid):
    """
    search the cell of the grid with the highter contraints

    :param grid: a sudoku's grid
    :type grid: grid
    :return: the cell with the most contraints
    :rtype: cell
    :UC: none
    """
    cell_min = (cells.create(),0,0)
    for ind_line in range(9):
        for ind_col in range(9):
            cell = sudoku_grid.get_cell(grid,ind_line,ind_col)
            if 0<len(cells.get_cellhipo(cell))<len(cells.get_cellhipo(cell_min[0])):
                cell_min = (cell,ind_col,ind_line) #réatribue cell dans la valeur cell_min avec ses coordonnées si elle possède plus de contraintes que l'ancienne valeure de cell_min 
    return cell_min

def not_solved(grid):
    """
    say if it's impossible to find solution of the sudoku's grid
    
    :param grid: a sudoku's grid
    :type grid: grid
    :return: True if it's impossible to find solution and False if not
    :rtype: bool
    :UC: none
    """
    for i in range(9):
        for cell in sudoku_grid.get_line(grid,i):
            if cells.get_cellvalue(cell) == '0' and not cells.get_cellhipo(cell):
                return True #renvoie True si une cellules ne possède aucune valeur hipothetic et que sa valeur est 0
    return False


def is_solved(grid):
    """
    say if grid is a resolved grid

    :param grid: a sudoku's grid
    :type grid: grid
    :return: True if it's resolved and False if not
    :rtype: bool
    :UC: none
    """
    for ind_line in range(9):
        cell_list = sudoku_grid.get_line(grid,ind_line)
        if len(set(cells.get_cellvalue(cell) for cell in cell_list)) != 9:
            return False

    for ind_col in range(9):
        cell_list = sudoku_grid.get_colomn(grid,ind_col)
        if len(set(cells.get_cellvalue(cell) for cell in cell_list)) != 9:
            return False

    for ind_square in range(9):
        cell_list = sudoku_grid.get_square(grid,ind_square)
        if len(set(cells.get_cellvalue(cell) for cell in cell_list)) != 9:
            return False
    return True


def search_sol(grid,talkative=False,background=False):
    """
    this algorithm search all solutions of a sudoku

    :param grid: a sudoku's grid
    :type string: grid
    :param talkative: (optional) defaults set to False. If True,
                      prints, all stages during the computating
    :type talkative: bool
    :param background: (optional) defaults set to False. If True,
                       the algorithm don't print anything
    :type background: bool
    :return: the number of recursion used by the function
    :rtype: int
    :Action: print all solutions of the grid
    :UC: none
    """
    global sol_way, ens_sol, father, compt_rec

    if talkative:
        os.system("clear")
        sudoku_grid.print_grid(grid)
        sleep(0.1)
    if not len(ens_cell0(grid)): # on vérifie si il n'y a aucune cellule à valeur 0
        if is_solved(grid): #si la solution de la grille est résolu, on imprimera la grille et stockera la chaine de caractère correspondante à cette grille dans une variable globale
            if not talkative and not background: #cette condition nous permet de ne pas imprimer 2 fois de suite chaque grille résolue si l'on choisi de mettre l'obtion talkative à la fonction
                sudoku_grid.print_grid(grid)
            ens_sol.add(sudoku_grid.grid2string(grid))
            try:
                sol_way[-1]["resolved"] = True
            except:
                pass

    elif not_solved(grid): #si la grille que l'on a est insoluble on passe à la suite sans rien faire.
        pass
    
    else:
        grid_list = list()
        cell_min = find_cell_min(grid) #on cherche la cellule ayant le plus de contraintes
        list_hipo = cells.get_cellhipo(cell_min[0])
        for hipo in list_hipo: #pour chaque valeur hipothetiques de la cellule, on applique l'une de ces valeurs puis on stock la chaine de caractère correspondant à la grille obtenu dans une liste
            cells.set_cellvalue(cell_min[0],hipo)
            string = sudoku_grid.grid2string(grid)
            grid_bis = sudoku_grid.make_grid(string) #on utilise une variable temporaire pour tester la valeur attribuée

            sol_way += [{"string":string,"resolved":False,'father':father,'son':[(str(hipo),cell_min[2],cell_min[1]),compt_rec]}] #on sauvegarde la modifivation que l'on a fait en y sauvegardant le compteur de récursion ce qui nous sera utile dans la fonction make_image
            save_father = father #on sauvegarde father temporairement
            father = [(str(hipo),cell_min[2],cell_min[1]),compt_rec] # on réattribue la nouvelle valuer de father
            search_sol(grid_bis, talkative = talkative, background = background)
            compt_rec += 1
            father = save_father

def ens_cell0(grid,reverse = False):
    """
    return all cells with a value equal at 0 or if reverse is True, return all cells with a value different at 0

    :param grid: a sudoku grid
    :type grid: grid
    :param reverse: (optional) defaults set to False. If True,
                    return the reverse of a normal using
    :type reverse: bool
    :return: a list of all cell with a value at 0 if reverse is True and the reverse if not
    :rtype: list of cells
    :UC: none
    :Examples:
    
    >>> grid = sudoku_grid.make_grid()
    >>> len(ens_cell0(grid))
    81
    >>> len(ens_cell0(grid,reverse=True))
    0
    """
    cell_list = list()
    for ind_line in range(9):
        for cell in sudoku_grid.get_line(grid,ind_line):
            if cells.get_cellvalue(cell) == '0' and not reverse:
                cell_list.append(cell)
            if reverse and cells.get_cellvalue(cell) != '0':
                cell_list.append(cell)
    return cell_list

def remove(grid):
    """
    print a random grid with removing cells from grid with one solution

    :param grid: a sudoku grid
    :type grid: grid
    :return: the string of a random sudoku's grid with removed cells
    :rtype: str
    :UC: none
    """
    global ens_sol

    cell_list = ens_cell0(grid,reverse = True)
    if len(cell_list) <= 17: #il est impossible d'avoir une grille de sudoku avec moins de 17 remplies si l'on veut avoir une unique solution
        ens_sol = set() #on réinitialise les variables globales
        compt_rec = 0
        father = "SUDO"
        sol_way = list()

        return sudoku_grid.grid2string(grid)
    else:
        cell = cell_list[random.randint(1,len(cell_list)-1)] #on récupère une cellule au hasard dans l'ensemble des cellules non vides
        value = cells.get_cellvalue(cell)
        cells.set_cellvalue(cell,'0')
        string = sudoku_grid.grid2string(grid) #le fait de faire cette transformation nous permet de faire une mise à jour des valeurs hipothétiques
        search_sol(sudoku_grid.make_grid(string),background = True)
        if len(ens_sol) == 1:
            ens_sol = set() #on réinitialise les variables globales
            compt_rec = 0
            father = "SUDO"
            sol_way = list()

            return remove(sudoku_grid.make_grid(string))
        else:
            ens_sol = set() #on réinitialise les variables globales
            compt_rec = 0
            father = "SUDO"
            sol_way = list()
            
            cells.set_cellvalue(cell,value)
            return sudoku_grid.grid2string(grid)

def make_image(file_name="arbre"):
    """
    create a picture with file_name.dot as name of the differents part of sol_way

    :param file_name: (optional) the nale of the picture who is created
    :type file_name: str
    :return: None
    :rtype: NoneType
    :Action: create a picture of the resolved way
    :UC: none
    """
    global sol_way

    text = 'digraph G {\n   bgcolor="#FFFF00";\n   node[style=filled];\n'
    for ind_dic in range(len(sol_way)):
        #le fait d'avoir gardé le compteur de récursion nous premet d'avoir des noms uniques et ainsi ne pas avoir les mêmes nom parce qu'une case à été modifiée de la même manière mais dans deux branches de récursion différentes
        if sol_way[ind_dic]["father"] == "SUDO":
            text += '   "'+str(sol_way[ind_dic]["father"])+'"[shape=hexagon, fillcolor="#FF0000"];\n'
        else:
            text += '   "'+str(sol_way[ind_dic]["father"])+'"[label="'+str(sol_way[ind_dic]["father"][0])+'"];\n'

        if sol_way[ind_dic]["resolved"]:
            text += '   "'+str(sol_way[ind_dic]["son"])+'"[label="'+str(sol_way[ind_dic]["son"][0])+'", shape=hexagon, fillcolor="#00FF00"];\n'
        else:
            text += '   "'+str(sol_way[ind_dic]["son"])+'"[label="'+str(sol_way[ind_dic]["son"][0])+'"];\n'

        text += '   "'+str(sol_way[ind_dic]["father"])+'"->"'+str(sol_way[ind_dic]["son"])+'";\n'

    with open(file_name+".dot",'w') as stream:
        stream.write(text+"}")

    if os.name == "nt":
        os.system("bash")
    os.system("dot -Tpng -o "+file_name+".png "+file_name+".dot")



if __name__ == '__main__':
    import doctest
    doctest.testmod()

# eof

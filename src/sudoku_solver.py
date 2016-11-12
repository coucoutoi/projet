#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`sudoku_solver` module

:author: HULSKEN Alexandre & KARTI Adeniss

:date: 2016, november

This module provides sudoku solver's primitive operations

:Provides:

* `MAJ_hipothetic`
* `is_solved`
* `find_cell_min`
* `not_solved`
* `search_sol`
"""


import sudoku_grid,cells

##############################################
# Functions for grid's setup and management
##############################################

   #############
   # Variables #
   #############

sol_way, ens_sol, compt_rec = list(), set(), 0 #initialisation des variables globales qui nous servirons de sauvegarde dans le système résolution
# 3 grilles de sudoku qui ont permi de test aux fonctions
sud_notfinished = "490001007000045030382600050003070401800902005907030600030006529020850000500700013"
sud_finished = "495381267671245938382697154263578491814962375957134682738416529129853746546729813"
sud_2sol = '495381267671245938382697154263578400814962375957134682738426500129853746546791823'


   #############
   # Fonctions #
   #############

def is_solved(grid):
    """
    verify if the grid is solved

    :param grid: the sudoku's grid
    :type grid: grid
    :return: True if the sudoku is solved and False if not
    :rtype: bool
    :UC: none

    :Example:
    >>> grid1 = sudoku_grid.make_grid()
    >>> grid2 = sudoku_grid.make_grid(sud_finished)
    >>> is_solved(grid1)
    False
    >>> is_solved(grid2)
    True
    """
    for i in range(9):
        ens_cell_in_line = set()
        for cell in sudoku_grid.get_line(grid,i):
            ens_cell_in_line.add(cells.get_cellvalue(cell))
            if cells.get_cellvalue(cell) == '0': #si trouve une valeur de cellule nulle, renvoie False
                return False
        if len(ens_cell_in_line) != len(sudoku_grid.get_line(grid,i)): #si une valeure est 2 fois sur la même ligne, renvoie False
            return False
    return True #renvoie True si tous les tests sont passés

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
            if 0<len(cells.get_cellhipo(cell))<=len(cells.get_cellhipo(cell_min[0])):
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

def complete_1hipo(grid,talkative=False):
    """
    while there is always a cell with a unique hipothetic solution, it's replace this value and up-date the hipothetics values in the grid.
    :param grid: a sudoku's grid
    :type grid: grid
    :param talkative: (optional) defaults set to False. If True,
                      prints, all stages during the computating
    :type talkative: bool
    :return: None
    :rtype: NoneType
    :Action: repalce all cell with a unique hipothetic solution wile there is no one.
    :UC: none
    """
    global sol_way
    boolean = True #on initialise un booléen qui nous permettra de savoir quand on sortira de la boucke while
    while boolean:
        boolean = False #on lui réattribue la valeur False que l'on changera si il y a au moins une valeur de cellule qui sera changer dans la boucle. Cela nous permet de sortir de celle-ci si on parcour toute la grille sans changer aucune valeur
        for ind_line in range(9):
            for ind_col in range(9):
                cell = sudoku_grid.get_cell(grid,ind_line,ind_col)
                if len(cells.get_cellhipo(cell)) == 1: #on vérifie si la cellule ne possède qu'une seule valeur hipothétiques
                    boolean = True
                    value = cells.get_cellhipo(cell).pop() #on stock cette valeur hipothétique
                    sol_way += [(value,ind_col,ind_line)] #on sauvegarde la valeur et les coordonnées de la cellule que l'on a modifiée
                    cells.set_cellvalue(cell,value)
                    if talkative:
                        sudoku_grid.print_grid(grid)
                    ind_square = sudoku_grid.get_nthsquare(ind_line,ind_col)
                    func_lists = [sudoku_grid.get_line(grid,ind_line),sudoku_grid.get_colomn(grid,ind_col),sudoku_grid.get_square(grid,ind_square)] #on construit une liste 3 listes des cellules influencées par la cellule que l'on viens de modifier
                    for cell_list in func_lists:
                        MAJ_hipothetic(cell_list,value) #on mets à jour les valeurs hipothetiques des cellules de chaqu'une de ces 3 listes

def search_sol(grid,talkative=False):
    """
    this algorithm search all solutions of a sudoku

    :param grid: a sudoku's grid
    :type string: grid
    :param talkative: (optional) defaults set to False. If True,
                      prints, all stages during the computating
    :type talkative: bool
    :return: None
    :rtype: NoneType
    :Action: print all solutions of the grid
    :UC: none
    """
    global sol_way, ens_sol, compt_rec
    
    complete_1hipo(grid,talkative=talkative) #on remplis toutes les cases qui n'ont qu'une seule valeur hipothetique
    if is_solved(grid): #si la grille est résolue, on imprimera la grille et stockera la chaine de caractère correspondante à cette grille dans une variable globale
        if not talkative: #cette condition nous permet de ne pas imprimer 2 fois de suite chaque grille résolue si l'on choisi de mettre l'obtion talkative à la fonction
            sudoku_grid.print_grid(grid)
            ens_sol.add(sudoku_grid.grid2string(grid))
    elif not_solved(grid): #si la grille que l'on a est insoluble on passe la fonction sans rien faire.
        pass
    else:
        grid_list = list()
        cell_min = find_cell_min(grid) #on cherche la cellule ayant le plus de contraintes
        list_hipo = cells.get_cellhipo(cell_min[0])
        for hipo in list_hipo: #pour chaque valeur hipothetiques de la cellule, on applique l'une de ces valeurs puis on stock la chaine de caractère correspondant à la grille obtenu dans une liste
            sol_way += [(str(hipo),cell_min[1],cell_min[2])] #on sauvegarde la modifivation que l'on a fait
            cells.set_cellvalue(cell_min[0],hipo)
            grid_list += [sudoku_grid.grid2string(grid)]
        for string in grid_list: #pour chaque grille de la liste que l'on a construite, on teste de la résoudre par une relation de récursion
            grid = sudoku_grid.make_grid(string)
            if talkative:
                sudoku_grid.print_grid(grid)
            search_sol(grid,talkative=talkative)
            compt_rec += 1



if __name__ == '__main__':
    import doctest
    doctest.testmod()

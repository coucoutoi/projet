#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`sudoku_grid` module

:author: HULSKEN Alexandre & KARTI Adeniss

:date: 2016, november

This module provides grid's primitive operations for the sudoku solver.

:Provides:

* `make_grid`
* `grid2string`
* `get_line`
* `get_colomn`
* `get_square`
* `get_cell`
* `get_nthsquare`
* `print_grid`
* `NotInGridError`
* `NotGoodTypeError`
"""


import cells,sudoku_solver


#############################
# Exceptions for gthe grid
#############################

class NotInGridError(Exception):
    """
    Exception for coordonates values not in grid
    """
    def __init__(self, msg):
        self.message = msg

class NotGoodTypeError(Exception):
    """
    Exception for not correct type of values
    """
    def __init__(self, msg):
        self.message = msg


##############################################
# Functions for grid's setup and management
##############################################


   ############
   # Variable #
   ############

val_test = "012345678"*9


   ###############
   # Constructor #
   ###############
   
def make_grid(string='0'*81):
    """
    return a sudoku's grid.

    :param string: the sudoku
    :type string: str
    :return: a grid of sudoku
    :rtype: list of list of cells
    :UC: none
    :Examples:

    >>> grid = make_grid('1'*81)
    >>> make_grid('1'*80)
    Traceback (most recent call last):
    ...
    cells.NotCorrectValueError: len of s must be 81
    >>> make_grid(int('1'*81))
    Traceback (most recent call last):
    ...
    NotGoodTypeError: s must be a string
    """
    if type(string) == str:
        if len(string) == 81:
            grid = [[cells.create() for y in range(9)] for x in range(9)] #construction d'une grille vide
            for ind_line in range(9):
                for ind_col in range(9):
                    cells.set_cellvalue(grid[ind_line][ind_col],string[ind_line*9+ind_col]) #on modifie la valeur de chaque cellule avec la valeur de string correspondante
                    func_list = [get_line(grid,ind_line),get_colomn(grid,ind_col),get_square(grid,(ind_col//3) + (ind_line//3)*3)] #on récupère les cellules sur la même ligne, même colonne et même carré que celle que l'on a modifié
                    for cell_list in func_list:
                        sudoku_solver.MAJ_hipothetic(cell_list,string[ind_line*9+ind_col]) #on mets à jour les valeurs hipothetiques des cellules par rapport à la cellule que l'on a modifié
            return grid
        else:
            raise cells.NotCorrectValueError("len of s must be 81")
    else:
        raise NotGoodTypeError("s must be a string")

def grid2string(grid):
    """
    return the string from the grid

    :param grid: a grid of sudoku
    :type grid: grid
    :return: a srting of values from the sudoku
    :rtype: str
    :UC: none
    :Examples:

    >>> string = "490001007000045030382600050003070401800902005907030600030006529020850000500700013"
    >>> grid = make_grid(string)
    >>> grid2string(grid) == string
    True
    """
    string = ''
    for ind_line in range(9):
        for cell in get_line(grid,ind_line):
            string += cells.get_cellvalue(cell) #on cherche à reconstruire la chaîne de caractères correspondante à la grille que l'on donne
    return string


   #############
   # Selectors #
   #############

def get_line(grid,nthline):
    """
    return all cells' value in the nth line.
    
    :param grid: the sudoku's grid
    :type grid: grid
    :param nthline: a number of line
    :type nthline: int
    :return: a list of all cells in the nth line
    :rtype: list of cells
    :UC: nth must be an integer between 0 and 8
    :Examples:

    >>> grid = make_grid(val_test)
    >>> [cells.get_cellvalue(c) for c in get_line(grid,0)]
    ['0', '1', '2', '3', '4', '5', '6', '7', '8']
    >>> get_line(grid,10)
    Traceback (most recent call last):
    ...
    NotInGridError: nthline is not in grid
    >>> get_line(grid,{4})
    Traceback (most recent call last):
    ...
    NotGoodTypeError: you don't choose a correct type of value
    """
    try:
        if -1<nthline<9:
            return [grid[nthline][i] for i in range(9)] #on construit une liste de toutes les cellules se trouvant sur la ligne d'indice nthline
        else:
            raise NotInGridError('nthline is not in grid')
    except TypeError:
        raise NotGoodTypeError("you don't choose a correct type of value")

def get_colomn(grid,nthcol):
    """
    return all cells' value in the nth colomn.

    :param grid: the sudoku's grid
    :type grid: grid
    :param nthcol: a number of colomn
    :type nthcol: int
    :return: a list of all cells in the nth colomn
    :rtype: list of cells
    :UC: nth must be between 0 and 8
    :Examples:

    >>> grid = make_grid(val_test)
    >>> [cells.get_cellvalue(c) for c in get_colomn(grid,8)]
    ['8', '8', '8', '8', '8', '8', '8', '8', '8']
    >>> get_colomn(grid,9)
    Traceback (most recent call last):
    ...
    NotInGridError: nthcol is not in grid
    >>> get_colomn(grid,(4,))
    Traceback (most recent call last):
    ...
    NotGoodTypeError: you don't choose a correct type of value
    """
    try:
        if -1<nthcol<9:
            return [line[nthcol] for line in grid] #on construit une liste de toutes les cellules se trouvant sur la colonne d'indice nthcol
        else:
            raise NotInGridError('nthcol is not in grid')
    except TypeError:
        raise NotGoodTypeError("you don't choose a correct type of value")

def get_square(grid,nthsquare):
    """
    return all cells' value in the nth square of the grid.
    the disposition of nth's square in the grid:

               `+---+---+---+`\n
               `| 0 | 1 | 2 |`\n
               `+---+---+---+`\n
               `| 3 | 4 | 5 |`\n
               `+---+---+---+`\n
               `| 6 | 7 | 8 |`\n
               `+---+---+---+`\n
    
    :param grid: the sudoku's grid
    :type grid: grid
    :param nthsquare: a number of square
    :type nthsquare: int
    :return: a list of all cells in the nth square
    :rtype: list of cells
    :UC: nth must be between 0 and 8
    :Examples:

    >>> grid = make_grid(val_test)
    >>> [cells.get_cellvalue(c) for c in get_square(grid,5)]
    ['6', '7', '8', '6', '7', '8', '6', '7', '8']
    >>> get_square(grid,-1)
    Traceback (most recent call last):
    ...
    NotInGridError: nthsquare is not in grid
    >>> get_square(grid,[4])
    Traceback (most recent call last):
    ...
    NotGoodTypeError: you don't choose a correct type of value
    """
    try:
        if -1<nthsquare<9:
            return [grid[line+nthsquare//3*3][col+nthsquare%3*3] for line in range(3) for col in range(3)] #on construit une liste de toutes les cellules se trouvant dans le carré d'indice nthsquare
        else:
            raise NotInGridError('nthsquare is not in grid')
    except TypeError:
        raise NotGoodTypeError("you don't choose a correct type of value")

def get_cell(grid,nthline,nthcol):
    """
    return the value in coordonates nthline,nthcol of the sudoku's grid.

    :param grid: the sudoku's grid
    :type grid: grid
    :param nthline: a number of line
    :type nthline: int
    :param nthcol: a number of colomn
    :type nthcol: int
    :return: the cell at coordonates nthline,nthcol
    :rtype: cell
    :UC: nthline and nthcol must be integers between 0 and 8
    :Examples:

    >>> grid = make_grid()
    >>> get_cell(grid,0,0) == cells.create()
    True
    >>> get_cell(grid,-10,5)
    Traceback (most recent call last):
    ...
    NotInGridError: nthline is not in grid
    >>> get_cell(grid,[4],4)
    Traceback (most recent call last):
    ...
    NotGoodTypeError: you don't choose a correct type of value
    >>> get_cell(grid,5,31)
    Traceback (most recent call last):
    ...
    NotInGridError: nthcol is not in grid
    >>> get_cell(grid,{'r':5},5)
    Traceback (most recent call last):
    ...
    NotGoodTypeError: you don't choose a correct type of value
    """
    try:
        if not -1<nthline<9:
            raise NotInGridError('nthline is not in grid')
        elif not -1<nthcol<9:
            raise NotInGridError('nthcol is not in grid')
        else:
            return grid[nthline][nthcol]
    except TypeError:
        raise NotGoodTypeError("you don't choose a correct type of value")


    ####################
    # others functions #
    ####################

def get_nthsquare(nthline,nthcol):
    """
    return the nthsquare correspondate at the nthline and nthcol

    :param nthline: a number of line
    :type nthline: int
    :param nthcol: a number of colomn
    :type nthcol: int
    :return: the number of the square at the coordonate nthline,nthcol
    :rtype: int
    :Examples:

    >>> get_nthsquare(8,8)
    8
    >>> get_nthsquare(-1,8)
    Traceback (most recent call last):
    ...
    NotInGridError: nthline is not in grid
    >>> get_nthsquare(8,9)
    Traceback (most recent call last):
    ...
    NotInGridError: nthcol is not in grid
    >>> get_nthsquare("2",5)
    Traceback (most recent call last):
    ...
    NotGoodTypeError: you don't choose a correct type of value
    """
    try:
        if not -1<nthline<9:
            raise NotInGridError('nthline is not in grid')
        elif not -1<nthcol<9:
            raise NotInGridError('nthcol is not in grid')
        else:
            return (nthcol//3) + (nthline//3)*3 #on calcule l'indice du carré dans lequel se trouve la cellule de coordonnées données
    except TypeError:
        raise NotGoodTypeError("you don't choose a correct type of value")

def print_grid(grid):
    """
    print the sudoku's grid

    :param grid: a sudoku's grid
    :type grid: grid
    :return: None
    :rtype: NoneType
    :Action: print the grid
    :UC: none
    :Examples:

    >>> grid = make_grid(val_test)
    >>> print_grid(grid)
    +-------+-------+-------+
    | . 1 2 | 3 4 5 | 6 7 8 |
    | . 1 2 | 3 4 5 | 6 7 8 |
    | . 1 2 | 3 4 5 | 6 7 8 |
    +-------+-------+-------+
    | . 1 2 | 3 4 5 | 6 7 8 |
    | . 1 2 | 3 4 5 | 6 7 8 |
    | . 1 2 | 3 4 5 | 6 7 8 |
    +-------+-------+-------+
    | . 1 2 | 3 4 5 | 6 7 8 |
    | . 1 2 | 3 4 5 | 6 7 8 |
    | . 1 2 | 3 4 5 | 6 7 8 |
    +-------+-------+-------+
    """
    print('+'+'-------+'*3)
    for l1 in range(3):
        for l2 in range(3):
            print('|',end='')
            for c1 in range(3):
                for c2 in range(3):
                    if cells.get_cellvalue(get_cell(grid,l1*3+l2,c1*3+c2)) == '0':
                        print(' .',end='')
                    else:
                        print(' '+cells.get_cellvalue(get_cell(grid,l1*3+l2,c1*3+c2)),end='')
                print(' |',end='')
            print()
        print('+'+'-------+'*3)



if __name__ == '__main__':
    import doctest
    doctest.testmod()

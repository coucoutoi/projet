#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`solver` module

:author: HULSKEN Alexandre & KARTI Adeniss

:date: 2016, november

This module provides sudoku solver's primitive operations

:Provides:

* `print_grid`
* `MAJ_hipothetic`
"""


import sudoku_grid,cells

def print_grid(grid):
    """
    :Examples:
    >>> grid = sudoku_grid.make_grid(sudoku_grid.val_test)
    >>> print_grid(grid)
    +-------+-------+-------+
    | . 1 2 | 3 4 5 | 6 7 8 |
    | 1 2 3 | 4 5 6 | 7 8 . |
    | 2 3 4 | 5 6 7 | 8 . 1 |
    +-------+-------+-------+
    | 3 4 5 | 6 7 8 | . 1 2 |
    | 4 5 6 | 7 8 . | 1 2 3 |
    | 5 6 7 | 8 . 1 | 2 3 4 |
    +-------+-------+-------+
    | 6 7 8 | . 1 2 | 3 4 5 |
    | 7 8 . | 1 2 3 | 4 5 6 |
    | 8 . 1 | 2 3 4 | 5 6 7 |
    +-------+-------+-------+
    """
    print('+'+'-------+'*3)
    for l1 in range(3):
        for l2 in range(3):
            print('|',end='')
            for c1 in range(3):
                for c2 in range(3):
                    if cells.get_cellvalue(sudoku_grid.get_cell(grid,l1*3+l2,c1*3+c2)):
                        print(' {:d}'.format(cells.get_cellvalue(sudoku_grid.get_cell(grid,l1*3+l2,c1*3+c2))),end='')
                    else:
                        print(' .',end='')
                print(' |',end='')
            print()
        print('+'+'-------+'*3)

def is_solved(grid):
    """
    verify if the grid is solved

    :param grid: the sudoku's grid
    :type grid: grid
    :return: True if the sudoku is solved and False if not
    :rtype: bool

    :Example:
    >>> grid1 = sudoku_grid.make_grid()
    >>> grid2 = sudoku_grid.make_grid(sudoku_grid.sud_finished)
    >>> is_solved(grid1)
    False

    >>> is_solved(grid2)
    True
    """
    for i in range(9):
        for cell in sudoku_grid.get_line(grid,i):
            if not cells.get_cellvalue(cell):
                return False
    return True

def MAJ_hipothetic(cell_list):
    hipos = [cells.get_cellvalue(cell) for cell in cell_list]
    for cell in cell_list:
        for hipo_value in hipos:
            cells.unset_cellhipothetic(cell,hipo_value)

def solver(string):
    grid = sudoku_grid.make_grid(string)
    

if __name__ == '__main__':
    import doctest
    doctest.testmod

#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`sudoku_solver` module

:author: HULSKEN Alexandre & KARTI Adeniss

:date: 2016, november

This module provides sudoku solver's primitive operations

:Provides:

* `print_grid`
* `MAJ_hipothetic`
* `is_solved`
"""


import sudoku_grid,cells

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
    >>> grid = sudoku_grid.make_grid(sudoku_grid.val_test)
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
    :UC: none

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
    """
    up-date the cells' hipothetics values of cell_list with the value of the other cells of cell_value

    :param cell_list: a list of cells
    :type cell_list: list
    :return: None
    :rtype: NoneType
    :Action: up-date the hipohtetics value of each cell of cell_list
    :UC: none

    :Examples:
    >>> cell_list1 = [cells.create(i) for i in range(9)]
    >>> for cell in cell_list1: print(cells.get_cellhipo(cell),end="")
    {1, 2, 3, 4, 5, 6, 7, 8, 9}{}{}{}{}{}{}{}{}
    
    >>> MAJ_hipothetic(cell_list1)
    >>> for cell in cell_list1: print(cells.get_cellhipo(cell),end="")
    {9}{}{}{}{}{}{}{}{}
    """
    hipos = [cells.get_cellvalue(cell) for cell in cell_list]
    for cell in cell_list:
        for hipo_value in hipos:
            cells.unset_cellhipothetic(cell,hipo_value)

def solver(string):
    grid = sudoku_grid.make_grid(string)
    boolean = True
    while boolean:
        boolean = False
        for line in range(9):
            for col in range(9):
                cell = sudoku_grid.get_cell(grid,line,col)
                if len(cells.get_cellhipo(cell)) == 1:
                    boolean = True
                    cells.set_cellvalue(cell,cells.get_cellhipo(cell).pop())
                    lists = [sudoku_grid.get_line(grid,line),sudoku_grid.get_colomn(grid,col),sudoku_grid.get_square(grid,(col//3) + (line//3)*3)]
                    for cell_list in lists:
                        MAJ_hipothetic(cell_list)
        print_grid(grid)
                    
                    



if __name__ == '__main__':
    import doctest
    doctest.testmod()

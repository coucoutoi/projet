#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`solver` module

:author: HULSKEN Alexandre & KARTI Adeniss

:date: 2016, november

This module provides sudoku solver's primitive operations

:Provides:

* ``
"""


import sudoku_grid,cell

def print_grid(grid):
    """
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
                    if cell.get_cellvalue(sudoku_grid.get_cell(grid,l1*3+l2,c1*3+c2)):
                        print(' {:d}'.format(cell.get_cellvalue(sudoku_grid.get_cell(grid,l1*3+l2,c1*3+c2))),end='')
                    else:
                        print(' .',end='')
                print(' |',end='')
            print()
        print('+'+'-------+'*3)

def MAJ_hipothetic(grid,nthline,nthcol,set_value):
    line = sudoku_grid.get_line(grid,nthline)
    col = sudoku_grid.get_colomn(grid,nthcol)
    """square = sudoku_grid.get_square(grid,)"""
    for k in [line,col]:
        for c in k:
            cell.unset_cellhipothetic(c,set_value)
            if len(cell.get_cellhipo(c)) == 1:
                cell.set_cellvalue(c,cell.get_cellhipo(c).pop())



if __name__ == '__main__':
    import doctest
    doctest.testmod

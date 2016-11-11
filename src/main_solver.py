#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
        A little program using cells, sudoku_grid and sudoku_solver modules. Type ``usage()``.

        A sudoku's solver
"""


import sys,sudoku_solver,sudoku_grid

def usage():
    print('Usage : {:s} sudoku'.format(sys.argv[0]))
    print('with sudoku a string of number correspondate at a sudoku, the empty cells as 0')
    exit(1)

if __name__ == '__main__':
    try:
        string = sys.argv[1]
        grid = sudoku_grid.make_grid(string)
        sudoku_solver(grid)
    except:
        usage()

# eof

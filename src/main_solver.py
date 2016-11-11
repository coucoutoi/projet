#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
        A little program using cells, sudoku_grid and sudoku_solver modules. Type ``usage()``.

        A sudoku's solver
"""


import sys,sudoku_solver,sudoku_grid

def usage():
    print('Usage : {:s} -options sudoku'.format(sys.argv[0]))
    print('with sudoku a string of number correspondate at a sudoku, the empty cells as 0')
    print('and -options (optional) the options of the solver')
    exit(1)

if __name__ == '__main__':
    try:
        string = sys.argv[-1]
        grid = sudoku_grid.make_grid(string)
        talkative = False
        if len(sys.argv) == 2:
            pass
        if '-t' in sys.argv[1]:
            talkative = True
        sudoku_solver.search_sol(grid,talkative)
        if 'i' in sys.argv[1]:
            pass #create img
        elif 'rm' in sys.argv[1]:
            pass #remove a cell
    except:
        usage()

# eof

#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
        A little program using cells, sudoku_grid and sudoku_solver modules. Type ``usage()``.

        A sudoku's solver
"""


import sys,sudoku_solver,sudoku_grid

def usage():
    print()
    print('Usage : {:s} -options sudoku'.format(sys.argv[0]))
    print('  with sudoku a string of number correspondate at a sudoku, the empty cells as 0')
    print('  and -options (optional) the options of the solver')
    print('  --help for give the help to use the algorithm.')
    exit(1)

def help_options():
    print()
    print("The differents options possible for this sudoku's solver are:")
    print("  [-t] for print all stages of the solving")
    print("  [-i] for create a picture of the solving's tree")
    print("  [-rm] for remove a maximal of cell but with always one solution at the grid")
    exit(1)
    
if __name__ == '__main__':
    try:
        if '--help' in sys.argv[1]:
            help_options()
        string = sys.argv[-1]
        grid = sudoku_grid.make_grid(string)
        talkative = False
        if len(sys.argv) == 2:
            pass
        
        if '-t' in sys.argv[1]:
            talkative = True
        sudoku_solver.search_sol(grid,talkative)
        if '-i' in sys.argv[1]:
            pass #create img
        elif '-rm' in sys.argv[1]:
            pass #remove a cell
    except:
        usage()

# eof

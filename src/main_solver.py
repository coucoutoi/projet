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
    print('  --help for give the help to use this algorithm.')
    exit(1)

def help_options():
    print()
    print("The differents options possible for this sudoku's solver are:")
    print("  [-t] for print all stages of the solving")
    print("  [-i] for create a picture of the solving's tree")
    print("  [-rm] for remove random cells with keep always one solution at the grid")
    print("  [-rec] for give the number of recursion of the resolving function")
    
if __name__ == '__main__':
    try:
        if '--help' in sys.argv[1]:
            help_options()
        else:
            string = sys.argv[-1]
            grid = sudoku_grid.make_grid(string)
            talkative = False

            if '-rm' in sys.argv:
                sudoku_solver.remove(grid)
            else:
                if '-t' in sys.argv:
                    talkative = True

                compt_rec = sudoku_solver.search_sol(grid,talkative)

                if '-rec' in sys.argv:
                    if compt_rec:
                        print("There are {:d} recursions used for the resolution.".format(compt_rec))
                    else:
                        print("The algorithm don't used any recursion.")
                elif '-i' in sys.argv:
                    pass #create img
    except:
        usage()

# eof
"""
ajout option -rec avec compt_rec
"""

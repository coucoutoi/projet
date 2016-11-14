#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
        A little program using cells, sudoku_grid and sudoku_solver modules. Type ``usage()``.

        A sudoku's solver
"""


import sys, sudoku_solver, sudoku_grid, argparse


def usage():
    print()
    print('Usage : {:s} -options sudoku'.format(sys.argv[0]))
    print('  with sudoku a string of number correspondate at a sudoku, the empty cells as 0')
    print('  and -options (optional) the options of the solver')
    print('  --help for give the help to use this algorithm.')
    print()
    print("The differents options possible for this sudoku's solver are:")
    print("  [-t] for print all stages of the solving")
    print("  [-i] for create a picture of the solving's tree")
    print("  [-rm] for remove random cells with keep always one solution at the grid")
    print("  [-rec] for give the number of recursion of the resolving function")
    exit(1)

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--talkative", action = "store_true", help = " for print all stages of the solving")
parser.add_argument("-rec", "--recursion", action = "store_true", help = " for give the number of recursion of the resolving function")
parser.add_argument("-i", "--image", action = "store_true", help = " for create a picture of the solving's tree")
parser.add_argument("-rm", "--remove", action = "store_true", help = " for remove random cells with keep always one solution at the grid")
parser.add_argument("sudoku_string", help = " A sudoku grid represented by a string")
args = parser.parse_args()

if __name__ == '__main__':
    try:
        grid = sudoku_grid.make_grid(args.sudoku_string)
        talkative = False
        if args.remove:
            sudoku_solver.remove(grid)
        else:
            if args.talkative:
                talkative = True

            compt_rec = sudoku_solver.search_sol(grid,talkative=talkative)

            if args.recursion:
                if compt_rec:
                    print("There are {:d} recursions used for the resolution.".format(compt_rec))
                else:
                    print("The algorithm don't used any recursion.")
            elif args.image:
                pass #create image
    except:
        usage()

# eof

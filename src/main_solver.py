#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
        A little program using cells, sudoku_grid and sudoku_solver modules. Type ``usage()``.

        A sudoku's solver
"""


import sys, sudoku_solver, sudoku_grid, argparse

parser = argparse.ArgumentParser()
parser.add_argument("-t", "--talkative", action = "store_true", help = " for print all stages of the solving")
parser.add_argument("-rec", "--recursion", action = "store_true", help = " for give the number of recursion of the resolving function")
parser.add_argument("-i", "--image", action = "store", nargs="?", help = " for create a picture of the solving's tree")
parser.add_argument("-rm", "--remove", action = "store_true", help = " for remove random cells with keep always one solution at the grid")
parser.add_argument("sudoku_string", help = " A sudoku grid represented by a string")
args = parser.parse_args()

if __name__ == '__main__':
    grid = sudoku_grid.make_grid(args.sudoku_string)
    talkative = False
    if args.remove:
        sudoku_solver.remove(grid)
    else:

        compt_rec = sudoku_solver.search_sol(grid,talkative=args.talkative)

        if args.recursion:
            if compt_rec:
               print("There are {:d} recursions used for the resolution.".format(compt_rec))
            else:
                print("The algorithm don't used any recursion.")
        elif args.image:
            sudoku_solver.make_image(args.image)

# eof

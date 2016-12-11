#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
        A little program using cells, sudoku_grid and sudoku_solver modules. Type ``usage()``.

        A sudoku's solver
"""

from os import system
import sys, argparse
import sudoku_grid, graphical_main, sudoku_solver, cells

parser = argparse.ArgumentParser()
parser.add_argument("sudoku_string", nargs = "?", help = " A sudoku grid represented by a string")
parser.add_argument("-gr", "--graphical", action = "store_true", help = " for use the GUI")
parser.add_argument("-t", "--talkative", action = "store_true", help = " for print all stages of the solving")
parser.add_argument("-rec", "--recursion", action = "store_true", help = " for give the number of recursion of the resolving function (used for costs' calculate)")
parser.add_argument("-i", "--image", action = "store", metavar = "FileName", nargs = "?", help = " for create a picture of the solving's tree with FileName as name")
parser.add_argument("-rm", "--remove", action = "store_true", help = " for remove random cells with keeping always one solution at the grid")
args = parser.parse_args()

if __name__ == '__main__':
    try:
        if ((args.remove or args.graphical) and (args.talkative or args.recursion or args.image)) or (args.remove and args.graphical):
            print("Error: You can't use the option graphical or remove with an another option\n")
        
        elif args.graphical:
            graphical_main.main()

        else:
            sudoku_solver.compt_rec = 0
            sudoku_solver.ens_sol = set()
            grid = sudoku_grid.make_grid(args.sudoku_string)

            if args.remove:
                grid = sudoku_grid.make_grid(sudoku_solver.remove(grid))
                print("This is a random grid:")
                sudoku_grid.print_grid(grid)
            else:

                sudoku_solver.search_sol(grid,talkative=args.talkative)

                if args.talkative:
                    system("clear")
                    print("The solutions of the sudoku's grid are:")
                    for sol in sudoku_solver.ens_sol:
                        sudoku_grid.print_grid(sudoku_grid.make_grid(sol))

                if args.recursion:
                    if sudoku_solver.compt_rec:
                       print("There are {:d} recursions used for the resolution.".format(sudoku_solver.compt_rec))
                    else:
                        print("The algorithm don't used any recursion.")

                if args.image:
                    sudoku_solver.make_image(args.image)
                elif "-i" in sys.argv or "--image" in sys.argv:
                    sudoku_solver.make_image()
    except:
        system("python3 main_solver.py --help")

# eof

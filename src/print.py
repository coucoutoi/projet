import sudoku_grid

def p(grid):
    print('+'+'-------+'*3)
    for l in range(3):
        for k in range(3):
            line = sudoku_grid.get_line(grid,l+k)
            print("|",end="")
            for i in range(3):
                if line[i]:
                    print(" {:d}".format(line[i]),end="")
                else:
                    print(' .',end='')
            print(' |')
        print('\n+'+'-------+'*3)

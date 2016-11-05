import sudoku_grid

def p(grid):
    print('+'+'-------+'*3)
    for l1 in range(3):
        for l2 in range(3):
            print('|',end='')
            for c1 in range(3):
                for c2 in range(3):
                    if grid[l1*3+l2][c1*3+c2]:
                        print(' {:d}'.format(grid[l1*3+l2][c1*3+c2]),end='')
                    else:
                        print(' .',end='')
                print(' |',end='')
            print()
        print('+'+'-------+'*3)

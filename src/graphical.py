import os
import tkinter as tk
from functools import partial
import sudoku_grid

img = []

def create(string='0'*81):
    global img,win
    grid = sudoku_grid.make_grid(string)
    win = tk.Tk()
    win.title('Sudoku Solver')
    iconpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "icons")
    img = [
        tk.PhotoImage(file=os.path.join(iconpath, "0.gif")),
        tk.PhotoImage(file=os.path.join(iconpath, "1.gif")),
        tk.PhotoImage(file=os.path.join(iconpath, "2.gif")),
        tk.PhotoImage(file=os.path.join(iconpath, "3.gif")),
        tk.PhotoImage(file=os.path.join(iconpath, "4.gif")),
        tk.PhotoImage(file=os.path.join(iconpath, "5.gif")),
        tk.PhotoImage(file=os.path.join(iconpath, "6.gif")),
        tk.PhotoImage(file=os.path.join(iconpath, "7.gif")),
        tk.PhotoImage(file=os.path.join(iconpath, "8.gif")),
        tk.PhotoImage(file=os.path.join(iconpath, "9.gif"))
        ]
    b = list()
    for ind_line in range(9):
        b.insert(ind_line,[])
        for ind_col in range(9):
            button = tk.Button(win, padx=0, pady=0, width=19, height=19, image=img[0])
            button.grid(column=ind_line, row=ind_col)
            b[ind_line].insert(ind_col, button)
            button.bind("<Button-3>",partial(__changeflag,b=b,grid=grid,ind_line=ind_line,ind_col=ind_col))
            button.config(command=partial(__changestate,b,grid,ind_line,ind_col))
    for ind_square in range(9):
        button_list = sudoku_grid.get_square(b,ind_square)
        for button in button_list:
            if ind_square%2:
                button.config(bg="black")
    win.mainloop()

def __changestate(b,grid,ind_line,ind_col):
    grid[ind_line][ind_col]['value'] = str((int(grid[ind_line][ind_col]['value'])+1)%10)
    __redraw(b,grid,ind_line,ind_col)

def __changeflag(evt,b,grid,ind_line,ind_col):
    pass

def __redraw(b,grid,ind_line,ind_col):
    for i in range(9):
        for j in range(9):
            button = b[ind_line][ind_col]
            cell = grid[ind_line][ind_col]
            button.config(image=img[int(cell['value'])])

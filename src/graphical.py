import os
import tkinter as tk
from functools import partial
import sudoku_grid, cells

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
    button_grid = list()
    for ind_line in range(9):
        button_grid.insert(ind_line,[])
        for ind_col in range(9):
            button = tk.Button(win, padx=0, pady=0, width=19, height=19, image=img[0])
            button.grid(column=ind_line, row=ind_col)
            button_grid[ind_line].insert(ind_col, button)
            button.bind("<Button-3>",partial(__changeflag,button_grid=button_grid,grid=grid,ind_line=ind_line,ind_col=ind_col))
            button.config(command=partial(__changestate,button_grid,grid,ind_line,ind_col))
    for ind_square in range(9):
        button_list = sudoku_grid.get_square(button_grid,ind_square)
        for button in button_list:
            if ind_square%2:
                button.config(bg="black")
    win.mainloop()

def __changestate(button_grid,grid,ind_line,ind_col):
    cell = sudoku_grid.get_cell(grid,ind_line,ind_col)
    value = (int(cells.get_cellvalue(cell))+1)%10
    cells.set_cellvalue(cell,str(value))
    __redraw(button_grid,grid,ind_line,ind_col)

def __changeflag(evt,button_grid,grid,ind_line,ind_col):
    pass

def __redraw(button_grid,grid,ind_line,ind_col):
    for i in range(9):
        for j in range(9):
            button = sudoku_grid.get_cell(button_grid,ind_line,ind_col)
            cell = sudoku_grid.get_cell(grid,ind_line,ind_col)
            button.config(image=img[int(cell['value'])])

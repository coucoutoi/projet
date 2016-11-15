import os
import tkinter as tk
from functools import partial

img = []

def create():
    global img,win
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
            button.bind("<Button-3>",partial(__changestate(b=b,i=ind_line,j=ind_col)))
    win.mainloop()

def __changestate(b,i,j):
    pass

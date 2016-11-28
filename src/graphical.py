#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
:mod: `graphical` module

:author: HULSKEN Alexandre & KARTI Adeniss

:date: 2016, november

This module provides graphicals' primitive operations for the sudoku solver.

:Provides:

* `create`
* `run`
* `__decre`
* `__incre`
* `__redraw`
"""

import os
import tkinter as tk
from functools import partial
import sudoku_grid, cells, sudoku_solver

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
            button = tk.Button(win, padx=0, pady=0, width=30, height=30, image=img[int(string[ind_line*9+ind_col])])
            button.grid(column=ind_col, row=ind_line)
            button_grid[ind_line].insert(ind_col, button)
            button.config(command=partial(__change,button_grid,grid,ind_line,ind_col))

    for ind_square in range(9):
        button_list = sudoku_grid.get_square(button_grid,ind_square)
        for button in button_list:
            if ind_square%2:
                button.config(bg="black")
            else:
                button.config(bg="white")

    talkative_var = tk.IntVar()
    talkative_check = tk.Checkbutton(win,text = "talkative",variable = talkative_var)
    talkative_check.grid(column = 9,row = 1)

    recursion_var = tk.IntVar()
    recursion_check = tk.Checkbutton(win,text = "recursion",variable = recursion_var)
    recursion_check.grid(column = 9,row = 3)

    image_var = tk.IntVar()
    image_check = tk.Checkbutton(win,text = "image",variable = image_var)
    image_check.grid(column = 9,row = 5)

    remove_var = tk.IntVar()
    remove_check = tk.Checkbutton(win,text = "remove",variable = remove_var)
    remove_check.grid(column = 9,row = 7)

    start_button = tk.Button(win, text="start")
    start_button.grid(column=1,row=9)
    start_button.config(command = partial(__run,button_grid,grid,talkative=talkative_var,rec=recursion_var,img=image_var,rm=remove_var))
    raz_button = tk.Button(win, text="RAZ")
    raz_button.grid(column=4,row=9)
    raz_button.config(command = partial(__RAZ,button_grid,grid))
    quit_button = tk.Button(win, text="quit")
    quit_button.grid(column=7,row=9)
    quit_button.config(command = win.destroy)

    win.mainloop()


def __clavier(button_grid,grid,ind_line,ind_col,event):
    value = event.keysym
    if value in set(str(i) for i in range(10)):
        cell = sudoku_grid.get_cell(grid,ind_line,ind_col)
        cells.set_cellvalue(cell,str(value))
        __redraw(button_grid,grid,ind_line,ind_col)

def __change(button_grid,grid,ind_line,ind_col):
    for ind_square in range(9):
        button_list = sudoku_grid.get_square(button_grid,ind_square)
        for button in button_list:
            if ind_square%2:
                button.config(bg="black")
            else:
                button.config(bg="white")
    button = sudoku_grid.get_cell(button_grid,ind_line,ind_col)
    button.config(bg="blue")
    win.bind("<Key>",partial(__clavier,button_grid,grid,ind_line,ind_col))

def __run(button_grid,grid,talkative,rec,img,rm):
    sudoku_solver.ens_sol = set()
    sudoku_solver.compt_rec = 0
    sudoku_solver.search_sol(grid,background=True)
    grid = sudoku_grid.make_grid(sudoku_solver.ens_sol.pop())
    for ind_line in range(9):
        for ind_col in range(9):
            __redraw(button_grid,grid,ind_line,ind_col)
    if rec.get():
        print(sudoku_solver.compt_rec)
    elif img.get():
        sudoku_solver.make_image()
    elif rm.get():
        sudoku_solver.remove(grid)

def __RAZ(button_grid,grid):
    for ind_line in range(9):
        for ind_col in range(9):
            cell = sudoku_grid.get_cell(grid,ind_line,ind_col)
            if int(cells.get_cellvalue(cell)):
                cells.set_cellvalue(cell,'0')
                __redraw(button_grid,grid,ind_line,ind_col)

def __redraw(button_grid,grid,ind_line,ind_col):
    button = sudoku_grid.get_cell(button_grid,ind_line,ind_col)
    cell = sudoku_grid.get_cell(grid,ind_line,ind_col)
    value = cells.get_cellvalue(cell)
    button.config(image=img[int(value)])

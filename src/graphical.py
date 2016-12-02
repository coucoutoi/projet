#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod: `graphical` module

:author: HULSKEN Alexandre & KARTI Adeniss

:date: 2016, november

This module provides graphicals' primitive operations for the sudoku solver.

:Provides:

* `create`
* `__write`
* `__RAZ`
* `__popup`
* `__clavier`
* `__change`
* `__run`
* `__decre`
* `__incre`
* `__redraw`
* `__ativate`
"""

import os
import tkinter as tk
from functools import partial
import sudoku_grid, cells, sudoku_solver
from tkinter.messagebox import *

img = []

def create(string='0'*81):
    """
    this function creates the graphical board from a solver. It also
    launches the event loop. Thus, this is the only function to run to
    have a functional graphical board.

    :param string: the sudoku
    :type string: str
    :return: None
    :rtype: NoneType
    """
    global img,win,grid,recursion_check,image_check,remove_check,talkative_check,start_button,enter_button

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
            button.config(command=partial(__change,button_grid,ind_line,ind_col))

    for ind_square in range(9):
        button_list = sudoku_grid.get_square(button_grid,ind_square)
        for button in button_list:
            if ind_square%2:
                button.config(bg="grey")
            else:
                button.config(bg="white")

    text = tk.Label(win,text = "options:",font = "bold 16 italic")
    text.grid(column = 9,row = 1)

    image_var = tk.IntVar()
    image_check = tk.Checkbutton(win,text = "arbre",variable = image_var)
    image_check.grid(column = 9,row = 2)

    remove_var = tk.IntVar()
    remove_check = tk.Checkbutton(win,text = "remove",variable = remove_var)
    remove_check.grid(column = 9,row = 3)

    talkative_var = tk.IntVar()
    talkative_check = tk.Checkbutton(win,text = "talkative",variable = talkative_var)
    talkative_check.grid(column = 9,row = 4)
    
    recursion_var = tk.IntVar()
    recursion_check = tk.Checkbutton(win,text = "recursion",variable = recursion_var)
    recursion_check.grid(column = 9,row = 5)

    enter_button = tk.Button(win, text = "Write a grid")
    enter_button.grid(column = 9,row = 6)
    enter_button.config(command = partial(__popup,button_grid))

    start_button = tk.Button(win, text="run")
    start_button.grid(column=1,row=9)
    start_button.config(command = partial(__run,button_grid,rec=recursion_var,img=image_var,rm=remove_var,t=talkative_var))

    raz_button = tk.Button(win, text="RAZ")
    raz_button.grid(column=4,row=9)
    raz_button.config(command = partial(__RAZ,button_grid))

    quit_button = tk.Button(win, text="quit")
    quit_button.grid(column=7,row=9)
    quit_button.config(command = win.destroy)

    win.mainloop()


def __clavier(button_grid,ind_line,ind_col,event):
    """
    This function reads the event key system and attributes a value of the cell at coordonates ind_line,ind_col

    :param button_grid: the board of buttons
    :type button_grid: list of list of ``button``
    :param ind_line: the line of the cell
    :type ind_line: int
    :param ind_col: the column of the cell
    :type ind_col: int
    :param event: the event who caused the function's call
    :type event: event
    """
    global grid

    value = event.keysym
    if value in set(str(i) for i in range(10)):
        cell = sudoku_grid.get_cell(grid,ind_line,ind_col)
        cells.set_cellvalue(cell,str(value))
        __redraw(button_grid,ind_line,ind_col)


def __change(button_grid,ind_line,ind_col):
    """
    this function attributes a new event for cells

    :param button_grid: the board of buttons
    :type button_grid: list of list of ``button``
    :param ind_line: the line of the cell
    :type ind_line: int
    :param ind_col: the column of the cell
    :type ind_col: int
    """
    global grid

    for ind_square in range(9):
        button_list = sudoku_grid.get_square(button_grid,ind_square)
        for button in button_list:
            if ind_square%2:
                button.config(bg="grey")
            else:
                button.config(bg="white")

    button = sudoku_grid.get_cell(button_grid,ind_line,ind_col)
    button.config(bg="blue")
    win.bind("<Key>",partial(__clavier,button_grid,ind_line,ind_col))


def __run(button_grid,rec,img,rm,t):
    """
    This function starts and coordonates the solver algorithm

    :param button_grid: the board of buttons
    :type button_grid: list of list of ``button``
    :param rec: the value of the recursion checker
    :param img: the value of the image checker
    :param rm: the value of the remove checker
    :param t: the value of the talkative checker
    """
    global grid,recursion_check,image_check,remove_chek,talkative_chack,start_button

    sudoku_solver.sol_way = list()
    sudoku_solver.ens_sol = set()
    sudoku_solver.father = "SUDO"
    sudoku_solver.compt_rec = 0

    if rm.get() and (rec.get() or img.get() or t.get()):
        showerror("Error","You can't use the remove option with an another option.")

    elif rm.get():
        grid = sudoku_grid.make_grid(sudoku_solver.remove(grid))

        for ind_line in range(9):
            for ind_col in range(9):
                __redraw(button_grid,ind_line,ind_col)

    else:
        from time import sleep

        string = sudoku_grid.grid2string(grid)
        try:
            sudoku_solver.search_sol(sudoku_grid.make_grid(string),background=True)
 
            if t.get():
                for dic in sudoku_solver.sol_way:
                    grid = sudoku_grid.make_grid(string)
                    move = dic['son'][0]
                    cell = sudoku_grid.get_cell(grid,move[1],move[2])
                    cells.set_cellvalue(cell,move[0])
                    __redraw(button_grid,move[1],move[2])
                    sleep(0.1)
                    win.update()
            else:
                if len(sudoku_solver.ens_sol):
                    for sol in sudoku_solver.ens_sol:
                        grid = sudoku_grid.make_grid(sol)

                        for ind_line in range(9):
                            for ind_col in range(9):
                                __redraw(button_grid,ind_line,ind_col)
                        sleep(3)
                        win.update()
                else:
                    showwarning("WARNING","There is no solution find for this grid")
        except RecursionError:
            showerror("Error","You give a grid too hard to solved for this little algorithm")


        if rec.get():
            showinfo("Recursion","Le programme a effecté "+str(sudoku_solver.compt_rec)+" recursions")

        if img.get():
            sudoku_solver.make_image()

    recursion_check.deselect()
    image_check.deselect()
    remove_check.deselect()
    talkative_check.deselect()


def __RAZ(button_grid):
    """
    This funciton redraws the board with all cell's values at '0'.

    :param button_grid: the board of buttons
    :type button_grid: list of list of ``button``
    """
    global grid

    for ind_line in range(9):
        for ind_col in range(9):
            cell = sudoku_grid.get_cell(grid,ind_line,ind_col)
            if int(cells.get_cellvalue(cell)):
                cells.set_cellvalue(cell,'0')
            __redraw(button_grid,ind_line,ind_col)


def __redraw(button_grid,ind_line,ind_col):
    """
    This function draws the board. Position ind_line and ind_col are used to test
    which number icon has to be drawn.

    :param button_grid: the board of buttons
    :type button_grid: list of list of ``button``
    :param ind_line: the line of the cell
    :type ind_line: int
    :param ind_col: the column of the cell
    :type ind_col: int
    """
    global grid

    button = sudoku_grid.get_cell(button_grid,ind_line,ind_col)
    cell = sudoku_grid.get_cell(grid,ind_line,ind_col)
    value = cells.get_cellvalue(cell)
    button.config(image=img[int(value)])


def __activate(self):
    """
    This function ables the enter_button
    """
    global enter_button
    enter_button.config(state = 'normal')


def __popup(button_grid):
    """
    This function coordonates the popup to enter a new grid

    :param button_grid: the board of buttons
    :type button_grid: list of list of ``button``
    """
    global popup,enter,enter_button
    popup = tk.Tk()

    enter_button.config(state = 'disable')

    label = tk.Label(popup,text = "Enter a new your grid")
    label.pack(side = 'top')

    string = tk.StringVar()    
    enter = tk.Entry(popup,textvariable = string)
    enter.bind("<Return>",partial(__write,button_grid))
    enter.pack()

    button = tk.Button(popup,text = "Ok")
    button.bind("<Button-1>",partial(__write,button_grid))
    button.pack(side = 'bottom')

    popup.bind("<Destroy>",__activate)
    popup.mainloop()


def __write(button_grid,self):
    """
    This function write the new grid or shows an error if not a good value

    :param button_grid: the board of buttons
    :type button_grid: list of list of ``button``
    """
    global grid

    try:
        string = enter.get()
        grid = sudoku_grid.make_grid(string)
        for ind_line in range(9):
            for ind_col in range(9):
                __redraw(button_grid,ind_line,ind_col)
    except:
        showerror("NotGoodValueError","You will enter 81 integers between 0 and 9 without anything else for create a new grid")

    popup.destroy()

# eof

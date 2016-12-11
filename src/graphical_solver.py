#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod: `graphical_solver` module

:author: HULSKEN Alexandre & KARTI Adeniss

:date: 2016, november/december

This module provides graphicals' primitive operations for the sudoku solver.

:Provides:

* `create`
* `help_option`
* `__write`
* `__RAZ`
* `__popup`
* `__clavier`
* `__change`
* `__run`
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

    grid_frame = tk.Frame(win,bd=1.5,bg="black")
    grid_frame.grid(column=0,row=0,columnspan=9,rowspan=9,padx=3,pady=3)

    for ind_line in range(9):
        button_grid.insert(ind_line,[])
        for ind_col in range(9):
            cell = sudoku_grid.get_cell(grid, ind_line, ind_col)
            value = cells.get_cellvalue(cell)
            
            button = tk.Button(grid_frame, padx=0, pady=0, width=30, height=30, image=img[int(value)])
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

    options_frame = tk.Frame(win)
    options_frame.grid(column=9,row=0,rowspan=10)
    
    text = tk.Label(options_frame,text = "options:",font = "bold 16 italic")
    text.grid(row = 1,pady=10)

    image_var = tk.IntVar()
    image_check = tk.Checkbutton(options_frame,text = "arbre",variable = image_var)
    image_check.grid(row = 2,sticky="nw",padx=2,pady=5)

    remove_var = tk.IntVar()
    remove_check = tk.Checkbutton(options_frame,text = "remove",variable = remove_var)
    remove_check.grid(row = 3,sticky="nw",padx=2,pady=5)

    talkative_var = tk.IntVar()
    talkative_check = tk.Checkbutton(options_frame,text = "talkative",variable = talkative_var)
    talkative_check.grid(row = 4,sticky="nw",padx=2,pady=5)
    
    recursion_var = tk.IntVar()
    recursion_check = tk.Checkbutton(options_frame,text = "recursion",variable = recursion_var)
    recursion_check.grid(row = 5,sticky="nw",padx=2,pady=5)

    enter_button = tk.Button(options_frame, text = "Write a grid")
    enter_button.grid(row = 6,padx=2,pady=30)
    enter_button.config(bd=2,command = partial(__popup,button_grid))

    image = tk.PhotoImage(file = 'icons/help-icon.png')
    can = tk.Canvas(options_frame,width = 40,height = 40)
    item = can.create_image(24,24,image = image)
    can.grid(row = 7)
    can.bind("<Button-1>",help_option)
    

    start_button = tk.Button(win, text="run")
    start_button.grid(column=1,row=9,pady=5)
    start_button.config(bd=2,command = partial(__run,button_grid,rec=recursion_var,img=image_var,rm=remove_var,t=talkative_var))

    raz_button = tk.Button(win, text="RAZ")
    raz_button.grid(column=4,row=9)
    raz_button.config(bd=2,command = partial(__RAZ,button_grid))

    quit_button = tk.Button(win, text="exit")
    quit_button.grid(column=7,row=9)
    quit_button.config(bd=2,command = back)

    win.mainloop()


def help_option(self):
    """
    Create a window to explain how do use the graphical solver
    """
    first_text = "This is a little algorithm of sudoku solver coded by Alexandre & Adeniss"
    help_text = """

    In this window, you can see several things, and we will see all for explain how do you use this sudoku solver.

    For enter a grid:
    - You can click on the button "write a grid" for open a popup.
        In the entry of this, you do enter a sequence of integers between 1 and 9
        and if you want to have an empty cell, enter 0.
        For validate your entry, you can click on the "ok" button or on the keyboard key enter.
    - You can also select a cell with a left click and use your keyboard for enter a number in this cell.

    For reset your window, you must click on button "RAZ" and it's ok.

    For used the different option of your solver, you can check checkers on rigth:
        - The "arbre" checker:
            if it used, the algorithm create a PNG picture of the sudoku's tree resolution
        - The "remove" checker:
            if it used, the algorithm remove cells to give a new gid with only one solution
            WARNING: if you use this option, you can't an another option.
        - The "talkative" checker:
            this option print step of all steps of the solution
        - The "recursion" checker:
            open a popup to say how many recursions are used for resolved the sudoku

    For run your solver with options' wanted, click on the button 'write'
    If the sudoku have many solutions, the algorithm print all, one per one with a break of 3s

    Finally, I hope you know what it's the button 'exit'... ;)
    """
    window = tk.Tk()
    window.title("HELP")

    label1 = tk.Label(window,text = first_text)
    label2 = tk.Label(window,text = help_text,justify = 'left')
    label1.pack(padx = 5,pady = 5)
    label2.pack(padx = 5)

    button = tk.Button(window,text = "close",command = window.destroy)
    button.pack(pady=5)

    window.mainloop()


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
    if value in set(str(i) for i in range(10)).union(set("KP_"+str(i) for i in range(10))):
        cell = sudoku_grid.get_cell(grid,ind_line,ind_col)
        cells.set_cellvalue(cell,str(value[-1]))
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
            if len(sudoku_solver.ens_cell0(grid,reverse=True)) < 17:
                showerror("Error","You give a grid too hard to solved for this little algorithm")
                return None

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


def back():
    """
    This funtcion manage if the user want to quit the GUI or return to the main window
    """
    global win
    import graphical_main

    ask = askyesno("Exit","Do you want to return to the main window of the GUI?")
    win.destroy()
    if ask:
        graphical_main.main()
    

# eof

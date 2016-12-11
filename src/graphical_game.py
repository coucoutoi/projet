#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod: `graphical_game` module

:author: HULSKEN Alexandre & KARTI Adeniss

:date: 2016, november/december

This module provides graphicals' primitive operations for the sudoku game.

:Provides:

* `create`
* `help_popup`
* `__write`
* `__RAZ`
* `__clavier`
* `__change`
* `__redraw`
* `__open_grid`
* `__choose_dif`
* `__write_grid`
* `__save`
* `__solve`
* `__correction`
* `__export`
* `__back`
"""

import os
import pickle
import tkinter as tk
from functools import partial
import sudoku_grid, cells, sudoku_solver, graphical_solver
from tkinter.messagebox import *
import tkinter.filedialog as tkfdial


img = list()

def create():
    """
    This function creates the graphical board for a game. It also
    launches the event loop. Thus, this is the inly functino to run to
    have a functional graphical board.
    """
    global img, win, grid, string

    string = '0'*81
    grid = sudoku_grid.make_grid()
    win = tk.Tk()
    win.title('Sudoku Game')
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
            button = tk.Button(grid_frame, padx=0, pady=0, width=30, height=30, image=img[0])
            button.grid(column=ind_col, row=ind_line)
            button_grid[ind_line].insert(ind_col, button)
            button.config(command=partial(__change,button_grid,ind_line,ind_col))
            button.config(state = "disabled")

    for ind_square in range(9):
        button_list = sudoku_grid.get_square(button_grid,ind_square)
        for button in button_list:
            if ind_square%2:
                button.config(bg="grey")
            else:
                button.config(bg="white")

    menu_bar = tk.Menu(win)

    file_menu = tk.Menu(menu_bar, tearoff = 0)
    solver_menu = tk.Menu(menu_bar, tearoff = 1)
    help_menu = tk.Menu(menu_bar, tearoff = 0)

    open_menuB = tk.Menubutton(file_menu, text = "Open")
    sub_menu = tk.Menu(open_menuB, tearoff = 0)
    sub_menu.add_command(label = "Open random grid", command = partial(__open_grid, button_grid))
    sub_menu.add_command(label = "Open a save grid", command = partial(__open_grid, button_grid, save = True))
    file_menu.add_cascade(label = "Open", menu = sub_menu)

    file_menu.add_command(label = "Save your grid", command = __save)
    file_menu.add_separator()
    file_menu.add_command(label = "Back", command = __back)
    file_menu.add_command(label = "Exit", command = win.destroy)

    solver_menu.add_command(label = "Reset", command = partial(__RAZ, button_grid))
    solver_menu.add_command(label = "Check values", command = partial(__correction, button_grid))
    solver_menu.add_separator()
    solver_menu.add_command(label = "Solve grid", command = partial(__solve, button_grid))
    solver_menu.add_command(label = "Export to solver", command = __export)

    help_menu.add_command(label = "Help", command = help_popup)

    menu_bar.add_cascade(label = "File", menu = file_menu)
    menu_bar.add_cascade(label = "Solver", menu = solver_menu)
    menu_bar.add_cascade(label = "Help", menu = help_menu)

    win.config(menu = menu_bar)
    win.mainloop()


def help_popup():
    """
    Creates a window to explain how do use the graphical game
    """
    first_text = "This is a little algorithm of sudoku solver coded by Alexandre & Adeniss"
    help_text = """
    In this window, you can see several things, and we will see all for explain how do you use this sudoku game.

    The options on the menu bar:
        * File
            - Open: you can open a random grid with the difficulty that you want or a grid that was saved in a
                GRD file
            - Save your grid: you can save your grid in a GRD file
            - Back: you are redirected on the main menu of the GUI
            - Exit: you quit the GUI
        * Solver
            - Reset: reset all cell's value that you enter in the grid
            - Check values:
            - Solve grid: print a solution of the grid
            - Export to solver: export your grid to the Solver module of the GUI without cells that enter by
                the user
            #Note: It's possible to cut this submenu to an another window for an ergonomique using of the solving
        * Help
            - Open the help window

    For play, you can select a cell with a left click (the cell who is selected is blue) and enter
    that you want with your keyboard.

    When you open a random grid, a popup is open to ask you a difficulty, click on this that you want and after,
    click in the 'ok' button. Differents difficultys that you can choose are sorted in order of difficulty:
            * EASY
            * MEDIUM
            * HARD
            * FIENDISH
            * 17 CELLS

    Good game for you and THANKS for playing... :)
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


def __RAZ(button_grid):
    """
    This funciton redraws the board with all cell's values as the beginnig.
    """
    global grid, string

    grid = sudoku_grid.make_grid(string)
    for ind_line in range(9):
        for ind_col in range(9):
            __redraw(button_grid,ind_line,ind_col)


def __clavier(button_grid,ind_line,ind_col,event):
    """
    This function reads the event key system and attributes a value of the cell at coordonates ind_line,ind_col
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
    """
    global grid

    for ind_square in range(9):
        button_list = sudoku_grid.get_square(button_grid,ind_square)
        for button in button_list:
            if button["bg"] in ["blue", "green"]:
                if ind_square%2:
                    button.config(bg="grey")
                else:
                    button.config(bg="white")

    button = sudoku_grid.get_cell(button_grid,ind_line,ind_col)
    button.config(bg="blue")
    win.bind("<Key>",partial(__clavier,button_grid,ind_line,ind_col))


def __redraw(button_grid,ind_line,ind_col,solver=False):
    """
    This function draws the board. Position ind_line and ind_col are used to test
    which number icon has to be drawn.
    It's also manage it must to create a finished popup with solver.
    """
    global grid

    button = sudoku_grid.get_cell(button_grid,ind_line,ind_col)
    cell = sudoku_grid.get_cell(grid,ind_line,ind_col)
    value = cells.get_cellvalue(cell)
    button.config(image=img[int(value)])
    if sudoku_solver.is_solved(grid) and not len(sudoku_solver.ens_cell0(grid)) and not solver:
        showinfo("CONGRATULATIONS","You have finished the sudoku")


def __open_grid(button_grid,save = False):
    """
    This function open a sudoku grid
    """
    global grid, string

    if save:
        stream = tkfdial.askopenfile(mode="rb", filetypes = [("GRD",".grd")], defaultextension=".grd")
        if stream:
            my_pickle = pickle.Unpickler(stream)
            save_value = my_pickle.load()
            stream.close()

            string = ""
            grid = sudoku_grid.make_grid()

            for ind_line in range(9):
                for ind_col in range(9):
                    save_cell = sudoku_grid.get_cell(save_value, ind_line, ind_col)
                    button = sudoku_grid.get_cell(button_grid, ind_line, ind_col)
                    button.config(image = img[int(save_cell["value"])])
                    cell = sudoku_grid.get_cell(grid, ind_line, ind_col)
                    cells.set_cellvalue(cell, save_cell["value"])
                    if save_cell["computer value"]:
                        button.config(state = "disabled")
                        string += save_cell["value"]
                    else:
                        button.config(state = "normal")
                        string += '0'

    else:
        __choose_diff(button_grid)


def __choose_diff(button_grid):
    """
    This function manage a popup to choose a difficulty of grid.
    """
    root = tk.Tk()

    label = tk.Label(root, text = "Choose a difficulty:")
    label.pack()

    var = tk.IntVar(root)
    R0 = tk.Radiobutton(root, text = "EASY", variable = var, value = 0)
    R0.select()
    R0.pack(anchor = tk.W )

    R1 = tk.Radiobutton(root, text = "MEDIUM", variable = var, value = 1)
    R1.pack(anchor = tk.W )

    R2 = tk.Radiobutton(root, text = "HARD", variable = var, value = 2)
    R2.pack(anchor = tk.W)

    R3 = tk.Radiobutton(root, text = "FIENDISH", variable = var, value = 3)
    R3.pack(anchor = tk.W)

    R4 = tk.Radiobutton(root, text = "17", variable = var, value = 4)
    R4.pack(anchor = tk.W)

    button = tk.Button(root, text = "OK", command = partial(__write_grid, button_grid, var, root))
    button.pack()

    root.mainloop()


def __write_grid(button_grid, var, root):
    """
    This function write a grid with th edifficulty choosen by the user.
    """
    global string, grid
    import random

    difficultys_list = ["easy","medium","hard","fiendish"]
    if var.get() == 4:
        with open("data/sudoku17.bdd","r") as stream:
            string = random.choice(stream.readlines())[:81]
    else:
        temp = ["",""]
        while temp[0] != difficultys_list[var.get()]:
            with open("data/sudokus.bdd","r") as stream:
                temp = random.choice(stream.readlines()).split(":")
        string = temp[-1][:81]

    grid = sudoku_grid.make_grid(string)
    for ind_line in range(9):
        for ind_col in range(9):
            __redraw(button_grid, ind_line, ind_col)
            cell = sudoku_grid.get_cell(grid, ind_line, ind_col)
            button = sudoku_grid.get_cell(button_grid, ind_line, ind_col)
            if int(cells.get_cellvalue(cell)):
                button.config(state = "disabled")
            else:
                button.config(state = "normal")
    root.destroy()

def __save():
    """
    This function save your sudoku grid.
    """
    global grid, string

    save_value = list()
    for ind_line in range(9):
        save_value.insert(ind_line, list())
        for ind_col in range(9):
            cell = sudoku_grid.get_cell(grid, ind_line, ind_col)
            value = cells.get_cellvalue(cell)
            save_value[ind_line].insert(ind_col, {"value":value, "computer value":string[ind_col+9*ind_line] == value and int(value)})

    stream = tkfdial.asksaveasfile(mode = "wb", title = "Save", filetypes = [("GRD", ".grd")], defaultextension = ".grd")
    if stream:
        my_pickle = pickle.Pickler(stream)
        my_pickle.dump(save_value)
        stream.close()
        showinfo("Save","You have saved your sudoku grid")


def __solve(button_grid):
    """
    This function resolved the sudoku grid and print one of its solutions
    """
    global grid, string

    if not len(sudoku_solver.ens_cell0(grid, reverse = True)):
        showerror("ERROR","Open a grid before before wanted to solved it...")
        return None

    try:
        sudoku_solver.search_sol(sudoku_grid.make_grid(string), background = True)
    except:
        showerror("ERROR","It's impossible to solve your grid")
        return None
    
    try:
        sol = sudoku_solver.ens_sol.pop()
    except:
        showwarning("WARNING","There is no solution find for your grid")
        return None
    grid = sudoku_grid.make_grid(sol)

    for ind_line in range(9):
        for ind_col in range(9):
            __redraw(button_grid, ind_line, ind_col, solver = True)


def __correction(button_grid):
    """
    """
    global grid, string

    if not len(sudoku_solver.ens_cell0(grid, reverse = True)):
        showerror("ERROR","Open a grid...")
        return None

    try:
        sudoku_solver.search_sol(sudoku_grid.make_grid(string), background = True)
    except:
        showerror("ERROR","It's impossible to solve your grid")
        return None
    
    try:
        sol = sudoku_solver.ens_sol.pop()
    except:
        showwarning("WARNING","There is no solution find for your grid")
        return None
    solved_grid = sudoku_grid.make_grid(sol)

    wrong_cells_list = list()
    for ind_line in range(9):
        for ind_col in range(9):
            cell = sudoku_grid.get_cell(grid, ind_line, ind_col)
            value = cells.get_cellvalue(cell)
            if int(value):
                solved_cell = sudoku_grid.get_cell(solved_grid, ind_line, ind_col)
                solved_value = cells.get_cellvalue(solved_cell)
                button = sudoku_grid.get_cell(button_grid, ind_line, ind_col)
                if value != solved_value and button["state"] == "normal":
                    button.config(bg = "red")
                    wrong_cells_list += [(cell , (ind_line, ind_col), solved_value, button)]

    if len(wrong_cells_list):
        boolean = askyesno("Corrected","Do you want that the algorithm corrected your errors?")
        if boolean:
            for saved_tuple in wrong_cells_list:
                cell = saved_tuple[0]
                ind_line, ind_col = saved_tuple[1][0], saved_tuple[1][1]
                solved_value = saved_tuple[2]
                button = saved_tuple[3]
                cells.set_cellvalue(cell, solved_value)
                __redraw(button_grid, ind_line, ind_col, solver = True)
                button.config(bg = "green")
    else:
        showinfo("Corrected","All cell's values are checked.")


def __export():
    """
    With this function, it's possible to export the grid in the graphical solver module.
    """
    global win, string

    win.destroy()
    graphical_solver.create(string)


def __back():
    """
    This function destroy the game window and open the main window.
    """
    global win
    import graphical_main

    win.destroy()
    graphical_main.main()


# eof

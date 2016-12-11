#!/usr/bin/python3
# -*- coding: utf-8 -*-

import graphical_game
import graphical_solver
import tkinter as tk

def gameB():
    window.destroy()
    graphical_game.create()

def solverB():
    window.destroy()
    graphical_solver.create()

def main():
    global window

    window = tk.Tk()
    window.title("Alexandre's & Adeniss's AP2 project")
    welcome_label = tk.Label(window, text = "Welcome to you in this project")
    ask_label = tk.Label(window, text = "What do you want to run?")
    frame = tk.Frame(window)
    solver_button = tk.Button(frame, text = "The Solver", bd = 2, width = 8, command = solverB)
    game_button = tk.Button(frame, text = "The Game", bd = 2, width = 8, command = gameB)
    exit_button = tk.Button(window, text = "Exit", bd = 2, command = window.destroy)

    welcome_label.pack(padx = 5, pady = 3)
    ask_label.pack(padx = 5)
    frame.pack(pady = 5)
    exit_button.pack(pady = 2)

    solver_button.pack(side = "left", padx = 4)
    game_button.pack(side = "right", padx = 4)

    window.mainloop()

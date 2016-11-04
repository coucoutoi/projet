#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`sudoku_grid` module

:author: HULSKEN Alexandre & KARTI Adeniss

:date: 2016, november

This module provides grid's primitive operations for the sudoku solver.
"""



class NotInGridError(Exception):
    """
    Exception for coordonates values not in grid
    """
    def __init__(self, msg):
        self.message = msg

def NotCorrectValueError(Exception):
    """
    Exception for not correct values of the grid
    """
    def __init__(self, msg):
        self.message = msg

def NotGoodTypeError(Exception):
    """
    Exception for not correct type of values
    """
    def __init__(self, msg):
        self.message = msg


##############################################
# Functions for game's setup and management
##############################################


default = ''
for i in range(9*9):
    default += '0'

def make_grid(s=default):
    """
    return a sudoku's grid.

    :param str: the sudoku
    :type str: list
    :return: a fresh grid of sudoku
    :rtype: list of list of numbers
    :UC: type(s) == str
    """
    if type(s) == str:
        grid = [[[] for y in range(9)] for x in range(9)]
        for line in range(9):
            for col in range(9):
                grid[line][col] = int(s[col+line*8])
        return grid
    else:
        raise NotGoodTypeError("s must be a string")

def get_line(grid,nth):
    """
    return all cells' value in the nth line.
    
    :param grid: the sudoku's grid
    :type grid: grid
    :param nth: a number of line
    :type nth: int
    :return: a list of all cells' value in the nth line
    :rtype: list of numbers
    :UC: nth must be an integer between 0 and 8

    :Examples:
    >>> grid = make_grid()
    >>> get_line(grid,0)
    [0, 1, 2, 3, 4, 5, 6, 7, 8]

    >>> get_line(grid,10)
    Traceback (most recent call last):
    ...
    AssertionError: nth must be an integer between 0 and 8
    """
    assert type(nth) == int and 0<=nth<9,"nth must be an integer between 0 and 8"
    return grid[nth]

def get_colomn(grid,nth):
    """
    return all cells' value in the nth colomn.

    :param grid: the sudoku's grid
    :type grid: grid
    :param nth: a number of colomn
    :type nth: int
    :return: a list of all cells' value in the nth colomn
    :rtype: list of numbers
    :UC: nth must be between 0 and 8

    :Examples:
    >>> grid = make_grid()
    >>> get_colomn(grid,8)
    [8, 16, 24, 32, 40, 48, 56, 64, 72]

    >>> get_colomn(grid,9)
    Traceback (most recent call last):
    ...
    AssertionError: nth must be an integer between 0 and 8
    """
    assert type(nth) == int and 0<=nth<9,"nth must be an integer between 0 and 8"
    return [line[nth] for line in grid]

def get_square(grid,nth):
    """
    return all cells' value in the nth square of the grid.

    :param grid: the sudoku's grid
    :type grid: grid
    :param nth: a number of square
    :type nth: int
    :return: a list of all cells' value in the nth square
    :rtype: list of numbers
    :UC: nth must be between 0 and 8

    :Examples:
    >>> grid = make_grid()
    >>> get_square(grid,5)
    [10, 11, 12, 18, 19, 20, 26, 27, 28]

    >>> get_square(grid,-1)
    Traceback (most recent call last):
    ...
    AssertionError: nth must be an integer between 0 and 8
    """
    assert type(nth) == int and 0<=nth<9,"nth must be an integer between 0 and 8"
    return [grid[line+nth//3][col+nth%3] for line in range(3) for col in range(3)]

def get_value(grid,nthline,nthcol):
    """
    return the value in coordonates nthline,nthcol of the sudoku's grid.

    :param grid: the sudoku's grid
    :type grid: grid
    :param nthline: a number of line
    :type nthline: int
    :param nthcol: a number of colomn
    :type nthcol: int
    :return: the value at coordonates nthline,nthcol
    :rtype: int
    :UC: nthline and nthcol must be integers between 0 and 8

    :Examples:
    >>> grid = make_grid()
    >>> get_value(grid,5,5)
    45

    >>> get_value(grid,-10,5)
    Traceback (most recent call last):
    ...
    AssertionError: nthline must be an integer between 0 and 8

    >>> get_value(grid,5,31)
    Traceback (most recent call last):
    ...
    AssertionError: nthcol must be an integer between 0 and 8
    """
    assert type(nthcol) == int and 0<=nthcol<9,"nthcol must be an integer between 0 and 8"
    assert type(nthline) == int and 0<=nthline<9,"nthline must be an integer between 0 and 8"
    return grid[nthline][nthcol]

def set_value(grid,nthline,nthcol,value):
    """
    :param grid: the sudoku's grid
    :type grid: grid
    :param nthline: a number of line
    :type nthline: int
    :param nthcol: a number of colomn
    :type nthcol: int
    :param value: the value of the cell
    :type value: int
    :return: None
    :rtype: NoneType
    :Action: mofify the value at coordonates nthline,nthcol in the grid
    :UC: nthline and nthcol must be integers between 0 and 8; value must be an integer between 0 and 9

    :Exemples:
    >>> grid = make_grid()
    >>> get_value(grid,5,5)
    0
    
    >>> set_value(grid,5,5,9)
    >>> get_value(grid,5,5)
    9

    >>> set_value(grid,-1,1,1)
    Traceback (most recent call last):
    ...
    NotInGridError: nthline is not in grid

    >>> set_value(grid,1,99,1)
    Traceback (most recent call last):
    ...
    NotInGridError: nthcol is not in grid

    >>> set_value(grid,0,0,55)
    Traceback (most recent call last):
    ...
    NotCorrectValueError: value is not a correct value
    
    >>> set_value(grid,1,1,'a')
    Traceback (most recent call last):
    ...
    NotGoodTypeError: you don't choose a good type of value

    >>> set_value(grid,'a',1,1)
    Traceback (most recent call last):
    ...
    NotGoodTypeError: you don't choose a good type of value
    """
    try:
        if not -1<nthline<9:
            raise NotInGridError('nthline is not in grid')
        elif not -1<nthcol<9:
            raise NotInGridError('nthcol is not in grid')
        elif not -1<value<10:
            raise NotCorrectValueError('value is not a correct value')
        else:
            grid[nthline][nthcol] = value
    except TypeError:
        raise NotGoodTypeError("you don't choose a good type of value")



if __name__ == '__main__':
    import doctest
    doctest.testmod()

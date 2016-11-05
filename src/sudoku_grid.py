#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`sudoku_grid` module

:author: HULSKEN Alexandre & KARTI Adeniss

:date: 2016, november

This module provides grid's primitive operations for the sudoku solver.

:Provides:

* `get_line`
* `get_colomn`
* `get_square`
* `get_value`
* `set_value`
"""


#############################
# Exceptions for gthe grid
#############################

class NotInGridError(Exception):
    """
    Exception for coordonates values not in grid
    """
    def __init__(self, msg):
        self.message = msg

class NotCorrectValueError(Exception):
    """
    Exception for not correct values of the grid
    """
    def __init__(self, msg):
        self.message = msg

class NotGoodTypeError(Exception):
    """
    Exception for not correct type of values
    """
    def __init__(self, msg):
        self.message = msg


##############################################
# Functions for grid's setup and management
##############################################


default = ''
for i in range(9*9):
    default += '0'

val_test = '012345678'*9

   ###############
   # Constructor #
   ###############
   
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
        for ind in range(9*9):
            grid[ind//9][ind%9] = int(s[ind])
        return grid
    else:
        raise NotGoodTypeError("s must be a string")

   #############
   # Selectors #
   #############

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
    >>> grid = make_grid(val_test)
    >>> get_line(grid,0)
    [0, 1, 2, 3, 4, 5, 6, 7, 8]

    >>> get_line(grid,10)
    Traceback (most recent call last):
    ...
    NotInGridError: nth is not in grid

    >>> get_line(grid,{4})
    Traceback (most recent call last):
    ...
    NotGoodTypeError: you don't choose a correct type of value
    """
    try:
        if -1<nth<9:
            return grid[nth]
        else:
            raise NotInGridError('nth is not in grid')
    except TypeError:
        raise NotGoodTypeError("you don't choose a correct type of value")

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
    >>> grid = make_grid(val_test)
    >>> get_colomn(grid,8)
    [8, 8, 8, 8, 8, 8, 8, 8, 8]

    >>> get_colomn(grid,9)
    Traceback (most recent call last):
    ...
    NotInGridError: nth is not in grid

    >>> get_colomn(grid,(4,))
    Traceback (most recent call last):
    ...
    NotGoodTypeError: you don't choose a correct type of value
    """
    try:
        if -1<nth<9:
            return [line[nth] for line in grid]
        else:
            raise NotInGridError('nth is not in grid')
    except TypeError:
        raise NotGoodTypeError("you don't choose a correct type of value")

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
    >>> grid = make_grid(val_test)
    >>> get_square(grid,5)
    [2, 3, 4, 2, 3, 4, 2, 3, 4]

    >>> get_square(grid,-1)
    Traceback (most recent call last):
    ...
    NotInGridError: nth is not in grid

    >>> get_square(grid,[4])
    Traceback (most recent call last):
    ...
    NotGoodTypeError: you don't choose a correct type of value
    """
    try:
        if -1<nth<9:
            return [grid[line+nth//3][col+nth%3] for line in range(3) for col in range(3)]
        else:
            raise NotInGridError('nth is not in grid')
    except TypeError:
        raise NotGoodTypeError("you don't choose a correct type of value")

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
    >>> grid = make_grid(val_test)
    >>> get_value(grid,5,5)
    5

    >>> get_value(grid,-10,5)
    Traceback (most recent call last):
    ...
    NotInGridError: nthline is not in grid

    >>> get_value(grid,[4],4)
    Traceback (most recent call last):
    ...
    NotGoodTypeError: you don't choose a correct type of value
    
    >>> get_value(grid,5,31)
    Traceback (most recent call last):
    ...
    NotInGridError: nthcol is not in grid

    >>> get_value(grid,{'r':5},5)
    Traceback (most recent call last):
    ...
    NotGoodTypeError: you don't choose a correct type of value
    """
    try:
        if not -1<nthline<9:
            raise NotInGridError('nthline is not in grid')
        elif not -1<nthcol<9:
            raise NotInGridError('nthcol is not in grid')
        else:
            return grid[nthline][nthcol]
    except TypeError:
        raise NotGoodTypeError("you don't choose a correct type of value")

   ############
   # modifier #
   ############

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

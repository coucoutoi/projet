#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
:mod:`cell` module

:author: HULSKEN Alexandre & KARTI Adeniss

:date: 2016, november

This module provides cells' primitive operations for the sudoku solver.

:Provides:

* `create`
* `get_cellvalue`
* `get_cellhipo`
* `set_cellvalue`
"""

import sudoku_grid


##############################################
# Functions for grid's setup and management
##############################################


   ###############
   # Constructor #
   ###############

def create(value):
    """
    :param value: the cell's value
    :type value: int
    :return: a new cell of a sudoku's grid.
    :rtype: cell
    :UC: none
    """
    res = {'value':value,'hipothetic':{}}
    if value == 0:
        res['hipothetic'] = {1,2,3,4,5,6,7,8,9}
    return res


   #############
   # Selectors #
   #############

def get_cellvalue(cell):
    """
    :param cell: a cell of the sudoku's grid
    :type cell: cell
    :return: the value of the cell
    :rtype: int
    :UC: none

    :Examples:
    >>> cell = create(5)
    >>> get_cellvalue(cell)
    5
    """
    return cell['value']

def get_cellhipo(cell):
    """
    :param cell: a cell of the sudoku's grid
    :type cell: cell
    :return: all of hipothetic values of the cell
    :rtype: set
    :UC: none
    
    :Examples:
    >>> cell = create(0)
    >>> cell2 = create(5)
    >>> get_cellhipo(cell)
    {1, 2, 3, 4, 5, 6, 7, 8, 9}

    >>> get_cellhipo(cell2)
    {}
    """
    return cell['hipothetic']


   ############
   # modifier #
   ############
   
def set_cellvalue(cell,value):
    """
    :param cell: a cell of the sudoku's grid
    :type cell: cell
    :param value: the value of the cell
    :type value: int
    :return: None
    :rtype: NoneType
    :Action: modify the value of the cell
    :UC: value must be between 0 and 9

    :Examples:
    >>> cell = create(0)
    >>> get_cellvalue(cell)
    0

    >>> get_cellhipo(cell)
    {1, 2, 3, 4, 5, 6, 7, 8, 9}
    
    >>> set_cellvalue(cell,5)
    >>> get_cellvalue(cell)
    5
    
    >>> get_cellhipo(cell)
    {}
    """
    cell['value'] = value
    if value !=0:
        cell['hipothetic'] = {}
    else:
        cell['hipothetic'] = {1,2,3,4,5,6,7,8,9}



if __name__ == '__main__':
    import doctest
    doctest.testmod()
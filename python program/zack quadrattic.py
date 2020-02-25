# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 22:58:36 2018

@author: 18537
"""

def Quadratic(a, b, c, x):
    '''
    a, b, c: numerical values for the coefficients of a quadratic equation
    x: numerical value at which to evaluate the quadratic.
    '''
    return a*(x**2) + b*x + c
print(Quadratic(2, 3, 4, 5))

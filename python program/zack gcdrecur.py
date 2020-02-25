# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 22:17:56 2018

@author: 18537
"""

def gcdRecur(a, b):
    '''
    a, b: positive integers
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcdRecur(b, a % b)
print(gcdRecur(5, 6))

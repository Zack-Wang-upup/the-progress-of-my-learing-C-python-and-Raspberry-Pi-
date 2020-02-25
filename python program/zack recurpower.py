# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 22:52:34 2018

@author: 18537
"""

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    else:
        return base * recurPower(base, exp - 1)
print(recurPower(4, 7))
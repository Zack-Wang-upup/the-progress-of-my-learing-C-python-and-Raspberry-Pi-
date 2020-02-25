# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 22:54:02 2018

@author: 18537
"""

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
    returns: int or float, base^exp
    '''
    result = base
    if exp == 0:
        return 1
    else:
        for i in range(1, exp):
            result *= base
    return result
print(iterPower(3,8))

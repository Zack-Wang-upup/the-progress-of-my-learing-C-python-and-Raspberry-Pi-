# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 22:11:57 2018

@author: 18537
"""

def gcdIter(a, b):
    gcd = 1
    c = min(a, b)
    for i in range(c, 1, -1):
        if (a % i == 0) and (b % i == 0):
            gcd = i
            break
        else:
            gcd = 1
    return gcd
print(gcdIter(4, 5))






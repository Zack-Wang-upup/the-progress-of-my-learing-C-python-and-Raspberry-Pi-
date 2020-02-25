# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 21:42:54 2019

@author: 18537
"""

def sum(x):
    if x==0 or x== 1:
     return 1
    else:
        return sum(x-1) + sum(x-2)
    
        
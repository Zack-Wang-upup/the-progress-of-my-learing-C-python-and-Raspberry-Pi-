# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 09:33:48 2019

@author: 18537
"""
def printMove(fr, to):
    print('move from' + str(fr) + 'to' + str(to))
def Towers(n, fr, to, spare):
    if n==1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)
print(Towers(3,'p1', 'p2', 'p3'))

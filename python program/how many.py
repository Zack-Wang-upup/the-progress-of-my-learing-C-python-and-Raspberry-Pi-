# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 09:36:00 2019

@author: 18537
"""

def how_many(aDict):

    sum = 0

    for i in aDict.values():

        sum += len(i)

    return sum
print(how_many({'u': [10, 15, 5, 2, 6], 'B': [15]}))

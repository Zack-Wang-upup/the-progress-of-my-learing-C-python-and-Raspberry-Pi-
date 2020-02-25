# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 22:20:42 2018

@author: 18537
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    returns: True if char is in aStr; False otherwise
    '''
    if aStr == "":
        return False
    elif len(aStr) == 1 and aStr == char:
        return True
    elif len(aStr) == 1 and aStr != char:
        return False
    elif aStr[len(aStr)//2] == char:
        return True
    else:
        if char < aStr[len(aStr)//2]:
            return isIn(char, aStr[:len(aStr)//2])
        else:
            return isIn(char, aStr[len(aStr)//2:])
print(isIn('b','abcd'))



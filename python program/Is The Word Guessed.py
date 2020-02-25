# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 09:54:06 2019

@author: 18537
"""

def isWordGuessed(apple, lettersGuessed):


    for i in apple:

        if i not in lettersGuessed:

            return False

    return True
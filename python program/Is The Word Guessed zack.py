# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 09:54:06 2019

@author: 18537
"""

def isWordGuessed(secretWord, lettersGuessed):


    for i in secretWord:

        if i not in lettersGuessed:

            return False

    return True
secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(isWordGuessed(secretWord, lettersGuessed))

# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 09:58:30 2019

@author: 18537
"""

def getGuessedWord(secretWord, lettersGuessed):

    result = []

    for i in secretWord:

        if i in lettersGuessed:

            result.append(i)

        else:

            result.append('_')

    return ' '.join(result)
secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getGuessedWord(secretWord, lettersGuessed))

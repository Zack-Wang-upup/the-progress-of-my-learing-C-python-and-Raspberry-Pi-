# -*- coding: utf-8 -*-
"""
Created on Tue Jan  1 10:00:46 2019

@author: 18537
"""

import string

alph = string.ascii_lowercase



def getAvailableLetters(lettersGuessed):


    remain = []

    for i in alph:

        if i not in lettersGuessed:

            remain.append(i)

    return ''.join(remain)
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getAvailableLetters(lettersGuessed))

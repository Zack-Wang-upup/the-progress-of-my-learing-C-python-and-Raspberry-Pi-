# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 11:03:09 2019

@author: 18537
"""

def updateHand(hand, word):

    output = hand.copy()

    for letter in word:

        if letter in output.keys():

            output[letter] -= 1

    return output
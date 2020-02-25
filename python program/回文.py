# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 20:04:53 2019

@author: 18537
"""
    

def ispal(s):
   if len(s)<=1:
            return True
   else:
            return s[0]==s[-1] and ispal(s[1:-1])
print('')
print('is eve a palindrome?')
print(ispal('eveve'))  
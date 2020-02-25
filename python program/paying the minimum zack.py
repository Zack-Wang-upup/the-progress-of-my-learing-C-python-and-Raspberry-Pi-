# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 15:42:00 2018

@author: 18537
"""

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

for i in range(12):
    balance = balance - (balance * monthlyPaymentRate) + ((balance - (balance * monthlyPaymentRate)) * (annualInterestRate/12))
print("Remaining balance:", round(balance, 2))



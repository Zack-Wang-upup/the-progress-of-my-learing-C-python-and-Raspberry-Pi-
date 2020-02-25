# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
high = 100
low = 0
correct = False
response = ""
user_number = input("Please think of a number between 0 and 100!")
while (response != "c"):
    guess = int((high + low)/2)
    print("Is your secret number", guess, "?")
    response = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly")
    if not  (response == "h" or response == "c" or response == "l"):
        print("Sorry, I did not understand your input.")
    elif (response is "h"):
        high = guess
    elif (response is "l"):
        low = guess

print ("Game over. Your secret number was:", guess)
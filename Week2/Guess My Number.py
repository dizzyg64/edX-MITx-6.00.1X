# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 16:25:06 2016

@author: RichardG
"""

print("Please think of a number between 0 and 100!")
high, low = 100, 0
guessed = False

while not guessed:
    g = (high + low)//2
    print("Is your secret number " + str(g) + "?")
    raw_input = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if raw_input == 'c':
        guessed = True
    elif raw_input == 'h':
        high = g
    elif raw_input == 'l':
        low = g
    else:
        print("Sorry, I did not understand your input.")
print('Game over. Your secret number was: ' + str(g))
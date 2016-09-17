# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 16:19:57 2016

@author: RichardG
"""
n = 0
v = ['a', 'e', 'i', 'o', 'u']
for letter in s:
    if letter in v:
        n += 1
print("Number of vowels: " + str(n))

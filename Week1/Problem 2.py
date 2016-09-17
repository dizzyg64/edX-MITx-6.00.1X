# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 16:20:41 2016

@author: RichardG
"""
bob = 0
for name in range(len(s)):
    if s[name:].startswith('bob'):
        bob += 1
print("Number of times bob occurs is: " + str(bob))

# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 16:21:03 2016

@author: RichardG
"""
string = s[0]
l = s[0]
for n in range(1, len(s)):
    if s[n] >= string[-1]:
        string += s[n]
        if len(string) > len(l):
            l = string
    else:
        string = s[n]
print ('Longest substring in alphabetical order is: ', l)
        

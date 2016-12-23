# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 20:35:00 2016

@author: RichardG
"""

def applyF_filterG(L, f, g):
    to_remove = []
    for s in L:
        if not g(f(s)):
            to_remove.append(s)
    for s in to_remove:
        L.remove(s)
    return max(L) if L != [] else -1
    
    
'''
def f(i):
    return i + 2
def g(i):
    return i > 5

L = [0, -10, 5, 6, -4]
print(applyF_filterG(L, f, g))
print(L)

Should print:

6
[5, 6]
'''
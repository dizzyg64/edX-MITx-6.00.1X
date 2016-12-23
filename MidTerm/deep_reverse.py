# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 20:33:49 2016

@author: RichardG
"""

def deep_reverse(L):  
    for i in L:  
        if type(i)==list:deep_reverse(i)  
    L.reverse()
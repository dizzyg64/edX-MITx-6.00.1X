# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 16:27:47 2016

@author: RichardG
"""

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp <= 0:
        return 1
    else:
        return base * recurPower(base, exp - 1)
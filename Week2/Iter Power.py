# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 16:27:32 2016

@author: RichardG
"""

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    result = 1
    while exp > 0:
        result *= base
        exp -= 1
    return result
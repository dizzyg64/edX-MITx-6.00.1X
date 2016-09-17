# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 16:28:25 2016

@author: RichardG
"""

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)
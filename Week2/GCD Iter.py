# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 16:28:08 2016

@author: RichardG
"""

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    testValue = min(a,b)
    while a % testValue != 0 or b % testValue != 0:
        testValue -= 1
    
    return testValue
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 19:53:34 2016

@author: RichardG
"""

def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    return lambda x: sum(e*x**n for e, n in zip(L, range(len(L)-1, -1, -1)))

print(general_poly([1,2,3,4])(10))
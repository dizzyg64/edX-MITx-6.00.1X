# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 20:32:50 2016

@author: RichardG
"""

def closest_power(base, num):
    exp = 0
    while True:
        if base**exp >= num:
            break
        exp += 1
    if abs(num - base**exp) >= abs(num - base**(exp - 1)):
        return exp - 1
    elif abs(num - base**exp) < abs(num - base**(exp - 1)):
        return exp
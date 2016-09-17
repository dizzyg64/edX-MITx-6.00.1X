# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 16:33:11 2016

@author: RichardG
"""
from math import tan
import math
math.pi
def polysum(n,s):
    area = (0.25*n*(s**2))/(tan(math.pi/n))
    perimeter = n * s
    sum = area + (perimeter**2)
    sum = round(sum, 4)
    return sum
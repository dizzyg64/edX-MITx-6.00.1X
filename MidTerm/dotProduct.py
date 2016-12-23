# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 20:33:24 2016

@author: RichardG
"""

def dotProduct(listA, listB):
    if listA == [] :
        return 0
    else:
        return (dotProduct(listA[1:], listB[1:]) + (listA[0] * listB[0]))
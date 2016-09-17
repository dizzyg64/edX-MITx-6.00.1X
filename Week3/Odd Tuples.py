# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 16:31:39 2016

@author: RichardG
"""

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    rTup = ()
    index = 0
    
    while index < len(aTup):
        rTup += (aTup[index],)
        index += 2
    return rTup
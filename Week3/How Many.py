# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 16:32:35 2016

@author: RichardG
"""

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    result = 0
    for key in aDict.keys():
        result += len(aDict[key])
    return result
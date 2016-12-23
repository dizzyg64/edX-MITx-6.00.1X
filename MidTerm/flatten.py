# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 20:36:04 2016

@author: RichardG
"""

def flatten(aList):
    result = []
    for entry in aList:
        if hasattr(entry, "__iter__") and not isinstance(entry, str):
            result.extend(flatten(entry))
        else:
            result.append(entry)
    return result
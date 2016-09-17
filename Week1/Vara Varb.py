# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 16:23:13 2016

@author: RichardG
"""
if type(varA) == str or type(varB) == str:
    print('string involved')
elif varA > varB:
    print('bigger')
elif varA == varB:
    print('equal')
else:
    print('smaller')

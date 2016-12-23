# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 19:59:19 2016

@author: RichardG
"""

def convert_to_mandarin(us_num):
    '''
    us_num, a string representing a US number 0 to 99
    returns the string mandarin representation of us_num
    '''
    num = int(us_num)
    small = num % 10
    big = (num - small) // 10
    translated = ""
    trans = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4': 'si',
          '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10': 'shi'}
    if num <= 10:
        if num is 10:
            translated += trans['10']
        else:
            translated += trans[str(small)]
    elif num > 10 and num < 20:
        translated += "shi " + trans [str(small)]
    else:
        translated += trans[str(big)] + " shi "
        if small is not 0:
            translated += trans[str(small)]
    return translated.strip()

print(convert_to_mandarin('36'))
print(convert_to_mandarin('20'))
print(convert_to_mandarin('16'))    
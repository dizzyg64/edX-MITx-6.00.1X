# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 16:18:38 2016

@author: RichardG
"""
monthlyInterestRate = annualInterestRate / 12.0
tmpBalance = balance
monthlyPayment = 0
while tmpBalance > 0:
    tmpBalance = balance
    monthlyPayment += 10
    for month in range(12):
        tmpBalance -= monthlyPayment
        tmpBalance += tmpBalance * monthlyInterestRate
print ("Lowest Payment: %i" % monthlyPayment)
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 16:15:36 2016

@author: RichardG
"""
totalPaid = 0
monthlyInterestRate = annualInterestRate / 12.0
for month in range(12):
    minimumMonthlyPayment = monthlyPaymentRate * balance  # PRAVILNO!!!
    totalPaid += minimumMonthlyPayment
    balance -= minimumMonthlyPayment
    balance += balance * monthlyInterestRate
print ("Remaining balance: " + str(round(balance, 2)))

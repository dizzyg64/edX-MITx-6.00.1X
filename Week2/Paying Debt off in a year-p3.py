# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 16:19:20 2016

@author: RichardG
"""
miR = annualInterestRate / 12.0
tmpBal = balance
low = balance / 12.0
high = balance * (1 + miR) ** 12 / 12.0
mPayment = round((low + high) / 2, 2)
while True:
    mPayment = round((low + high) / 2, 2)
    tmpBal = balance
    for month in range(12):
        tmpBal -= mPayment
        tmpBal += tmpBal * miR
    if abs(tmpBal - 0.01) < 0.1:
        print ("Lowest Payment: " + str(mPayment))
        break
    elif tmpBal < 0:
        high = mPayment
        mPayment = round((low + high) / 2, 2)
    else:
        low = mPayment
        mPayment = round((low + high) / 2, 2)

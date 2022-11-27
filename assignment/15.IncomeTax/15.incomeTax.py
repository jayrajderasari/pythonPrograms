# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 18:20:33 2022

@author: Jayraj Derasari
"""
#taking input of income
income=int(input("Enter your income:"))

if income<500000:                                   # 0 tax for income less than 5L
    tax = 0
elif income>500000 and income<1000000:
    income = income - 500000
    tax = (income*10)/100                           # tax of income over 5L as 10%
elif income>1000000:
    income = income - 1000000
    tax = ((500000*10)/100) + ((income*20)/100)     # tax of income between 5L and 10L is fix 10%=50k and calculating tax over 10L as 20%
else:
    tax=0
    
#printing payable tax    
print("Tax payable is:", tax)
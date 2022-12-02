# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 23:55:48 2022

@author: Jayraj Derasari
"""

#taking income as input
income=int(input("Enter Income:"))
# tax=0

#Calculating tax as per the tax slab and income
if income<=500000:
    tax=0   #No tax till income of 5Lakhs as standard deduction
elif income>500000 and income<1000000:
    tax=0   #No tax till income of 5Lakhs
    income=income-500000    #Calculating taxable income by removing standard deduction
    tax=income*10/100   #Calculating tax of income over 5Lakhs as 10%
elif income>=1000000:
    tax=50000   #Tax of income of tax slab of 5L to 10L
    income=income-1000000 #Removing income of standard deduction and lesser tax slab
    tax=tax+(income*20/100) # Calculating tax of income over 10Lakhs as 20%
    
#printing payable tax
print("Tax Payable:", tax)

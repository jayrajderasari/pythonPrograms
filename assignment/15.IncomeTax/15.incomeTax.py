# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 23:55:48 2022

@author: Jayraj Derasari
"""

# =============================================================================
# 15. Calculate income tax for the given income by following the given rules:
# Income Rate (in %)
# upto Rs 5,00,000 0%
# upto Rs 10,00,000 10% (of income above 5,00,000)
# above Rs 10,00,000 20% (of income above 10,00,000)
# Expected Output:
# Enter your income (Rs): 600000
# Income tax payable by you (Rs) = 10000/-
# =============================================================================

#taking income as input from user
income = int(input("Enter Income:"))

#defining variable tax to be calculated
tax = 0
#Calculating tax as per the tax slab and income
if income <= 500000:
    tax = 0   #No tax till income of 5Lakhs
elif income > 500000 and income < 1000000:
    tax = 0   #No tax till income of 5Lakhs as standard deduction
    income = income - 500000    #Calculating taxable income by removing standard deduction
    tax = (income) * (10 / 100)   #Calculating tax of income over 5Lakhs as 10%
elif income >= 1000000:
    tax = 50000   #Tax of income of tax slab of 5L to 10L
    income = income - 1000000 #Removing income of standard deduction and lesser tax slab
    tax = tax + (income * 20 / 100) # Calculating tax of income over 10Lakhs as 20%
    
#printing payable tax
print("Tax Payable:", tax)

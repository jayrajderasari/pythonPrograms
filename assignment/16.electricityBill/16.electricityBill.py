# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 09:31:01 2022

@author: Jayraj Derasari
"""

# =============================================================================
# 16. Write a program to calculate the electricity bill (accept the number of electricity units used
# from user) using following details:
# Units Price/unit
# Up to 100 units No charge
# After 100 units Rs 5 per unit
# After 500 units Rs 8 per unit
# =============================================================================

#take number of units consumed as input from user
units = int(input("Enter number of units consumed:"))

#Calculating charges from number of units
if units > 100:
    if units <= 500:
        charges = 0   #first 100 units are free
        units = units - 100
        charges = 5 * (units) #5rs per unit till 500 units after 100 units
    else:
        charges = 0   #first 100 units are free
        units = units - 100
        charges = charges + 5 * (400)     #5rs per unit till 500 units after 100 units
        units = units - 400
        charges = charges + (units)*8   #charges of units after 500 units
else:
    charges = 0
    
#Printing calculated Charges
print("charges:", charges)
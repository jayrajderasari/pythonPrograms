# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 16:33:53 2022

@author: Jayraj Derasari
"""

# =============================================================================
# 19. Write a python program to check whether the entered number is an Armstrong number or
# not.
# =============================================================================

#taking number as string input and storing as n
n = str(input("Enter a number:"))

#calculating length of string
l = len(n)

#defining sum of nth power of digits to be calculated
sum = 0

#using for loop to calculate sum of nth power of digits
for i in range (0,l):
    sum = sum + (int(n[i])) ** l 
    
#Checking and printing if n is equal to sum then number is armstrong
if int(n) == sum: #using int(n) as string cannot be compared with integer
    print ("The number is Armstrong")
else:
    print("The number is not Armstrong")
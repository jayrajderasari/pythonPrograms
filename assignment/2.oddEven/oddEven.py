# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 23:46:24 2022

@author: Jayraj Derasari
"""
# =============================================================================
# 2. Write a Python program to input a number and check whether the entered number is even or
# odd.
# =============================================================================

#taking value of n
n = int(input("Enter a number:"))

#Calculating and printing if n is even or odd
if n % 2 == 0:
    print("The number is Even")
else:
    print("The number is Odd")
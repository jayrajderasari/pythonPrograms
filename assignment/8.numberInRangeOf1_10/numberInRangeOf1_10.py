# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 13:02:10 2022

@author: Jayraj Derasari
"""

# =============================================================================
# 8. Make a program that asks the number between 1 and 10. If the number is out of range the
# program should display “invalid number”.
# =============================================================================

#taking input of number from user and storing as n
n = float(input("Enter a number:"))
n = int(n)
#if n is in 1 to 10 then print valid else invalid
if n in range(1,10):
    print("Valid number")
else:
    print("Invalid number") 
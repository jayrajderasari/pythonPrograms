# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 23:46:12 2022

@author: Jayraj Derasari
"""

# =============================================================================
# 9. Write a Python program that generates and prints 100 random numbers.
# =============================================================================

#importing random library function
import random

#making a for loop for 100 values
for i in range(1,101):
   #generating random numbers and storing as n
    n=random.random()
    
    #printing random values
    print(n)
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 00:17:28 2022

@author: Jayraj Derasari
"""

#taking age as input
age = int(input("Please enter your age:"))

#Checking and printing that if age is greater than 18 than person can vote otherwise not
if age>=18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
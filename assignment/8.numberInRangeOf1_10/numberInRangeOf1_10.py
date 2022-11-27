# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 13:02:10 2022

@author: Jayraj Derasari
"""
#taking input from user
n=int(input("Enter a number:"))

#if n is in 1 to 10 then print valid else invalid
if n in range(1,11):
    print("Valid number")
else:
    print("Invalid number") 
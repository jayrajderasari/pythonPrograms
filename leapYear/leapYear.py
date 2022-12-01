# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 09:45:12 2022

@author: Jayraj Derasari
"""
#Taking value of year as input
year = int (input("Please enter year:"))

#checking condition of leap year according to Georgian Calendar and printing if it's a leap year or not
if year%4==0 and year%100!=0 or year%400==0:
    print("It is a leap year")
else:
    print("It is not a leap year")
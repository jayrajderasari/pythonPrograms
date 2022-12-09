# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 18:21:39 2022

@author: Jayraj Derasari
"""
#take input of number whose factors are to be calculated
num=int(input("Enter a number:"))
#Checking and printing if the number is factor of n or not from 1 to n
for i in range(1,num+1):
    if num%i==0:
        print(i)

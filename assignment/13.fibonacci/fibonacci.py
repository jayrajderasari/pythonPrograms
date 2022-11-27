# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 14:16:43 2022

@author: Jayraj Derasari
"""
#taking value of n as lenght of series
n = int(input("Enter a number:"))

#Inititalising array of fibonacci and its initial values
fibonacci = [0]*n
fibonacci[0] = 0
fibonacci[1] = 1

#calculating further values of fibonacci series
for i in range(2,n):
    fibonacci[i] = fibonacci[i-1] + fibonacci[i-2]
    
#printing fibonacci
print(fibonacci)
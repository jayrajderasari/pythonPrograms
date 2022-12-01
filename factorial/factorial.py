# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 11:58:06 2022

@author: Jayraj Derasari
"""
#Taking input of number from user
num = int(input("Enter a Number:"))

#defining factorial to be calculated
factorial = 1

#Checking if the value of num is valid or invalid or 0 and printing factorial
if num<0:
    print("Sorry invalid value")
elif num == 0:
    print("1")
else:
    # Calculating value of factorial if num>0 and printing factorial
    for i in range(1,num+1):
        factorial = factorial*i
    print("The factorial of",num,"is",factorial)
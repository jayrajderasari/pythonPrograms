# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 18:07:06 2022

@author: Jayraj Derasari
"""
#taking input of number and considering c as a differentiating variable as flag
c = 0
num=int(input("Enter a number:"))

#Calculating c to find if number is prime or composite
for i in range(1,num+1):
    if num%i==0:
        c=c+1
    if c>=3:
        break
    
#Using c as flag and print if the number is prime composite or none
if c==1:
    print("Neither prime nor composite")
elif c==2:
    print("number is prime")
else:
    print("number is composite")
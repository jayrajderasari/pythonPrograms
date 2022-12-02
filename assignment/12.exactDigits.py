# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 00:23:57 2022

@author: Jayraj Derasari
"""
#taking input as string and string as n
n=str(input("Enter number:"))

#printing string in reversed order using for loop and using (end=' ') to keep space while printing values
for i in reversed(range(0,len(n))):
    print(n[i], end=' ')
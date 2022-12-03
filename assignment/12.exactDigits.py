# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 00:23:57 2022

@author: Jayraj Derasari
"""

"""
12. Write a program called ExtractDigits to extract each digit from an int in the reverse order. For
example, if the int is 12345, the output shall be "5 4 3 2 1", with a space separating the digits.
"""

#taking input as string and string as n
n=str(input("Enter number:"))

#printing string in reversed order using for loop
#using (end=' ') to keep space while printing values
for i in reversed(range(0,len(n))):
    print(n[i], end=' ')
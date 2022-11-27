# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 13:06:09 2022

@author: Jayraj Derasari
"""
#taking values of variables and operators
x=int(input("Enter variable 1:"))
o=input("Enter mathematical operator:")
y=int(input("Enter variable 2:"))
result='-'
#calculating result
if o=='+':
    result=x+y
elif o=='-':
    result=x-y
elif o=='*':
    result=x*y
elif o=='/':
    result=x/y
elif o=='**':
    result=x**y
elif o=='%':
    result=x%y
else:
    print('invalid mathematical operator')
    
#printing result
print(x,o,y,'=',result)
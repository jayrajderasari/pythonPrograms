# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 17:50:27 2022

@author: Jayraj Derasari
"""
a=int(input("Enter side a:"))
b=int(input("Enter side b:"))
c=int(input("Enter side c:"))

s=(a+b+c)/2

area = ((s-a)*(s-b)*(s-c))**(1/2)

print("Area:",area)
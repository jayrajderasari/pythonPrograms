# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 00:13:26 2022

@author: Jayraj Derasari
"""
#taking input of angles of triangle
a=int(input("Enter angle 1:"))
b=int(input("Enter angle 2:"))
c=int(input("Enter angle 3:"))

#checking that all angles are positive and sum of angles equal 180
if a+b+c==180 and a>0 and b>0 and c>0:
    print("Triangle is valid")
else:
    print("Triangle is invalid")
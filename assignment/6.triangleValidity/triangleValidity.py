# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 00:13:26 2022

@author: Jayraj Derasari
"""

# =============================================================================
# 6. Write a Python program to input angles of a triangle and check whether triangle is valid or
# not.
# =============================================================================

#taking input of angles of triangle
a = float(input("Enter angle 1:"))
b = float(input("Enter angle 2:"))
c = float(input("Enter angle 3:"))

#checking that all angles are positive and sum of angles equal 180
if a+b+c == 180 and a > 0 and b > 0 and c > 0:
    print("The triangle is valid")
else:
    print("The triangle is invalid")
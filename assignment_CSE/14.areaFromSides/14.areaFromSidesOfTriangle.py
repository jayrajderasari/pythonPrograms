# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 17:50:27 2022

@author: Jayraj Derasari
"""

# =============================================================================
# 14. Calculate the area of triangle given its three sides. The formula or algorithm used is:
# Area = sqrt(s(s – a)(s – b)(s – c)), where s = (a + b + c) / 2 or perimeter / 2 and a, b & c are the
# sides of triangle.
# =============================================================================


#taking sides of triangle as input
a = int(input("Enter side a:"))
b = int(input("Enter side b:"))
c = int(input("Enter side c:"))

#Calculating semi-perimeter
s = (a + b + c) / 2

#Calculating area of triangle
area = ((s - a) * (s - b) * (s - c)) ** (1/2)

#printing the area
print("Area:",area)
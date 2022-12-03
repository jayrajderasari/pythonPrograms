# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 17:55:41 2022

@author: Jayraj Derasari
"""

"""
25. Write a python program using conditional statements to allocate multiple grades as per the
marks range. For example, a student having marks greater than or equal to 95 should get an A+
grade."""

#take marks as input
marks=int(input("Enter your marks:"))

#Calculating and printing appropriate grade as per marks

if marks>100 or marks<0:    #Marks cannot be negative or greater than 100
    print("Enter correct marks")

elif marks>=95: #A+ grade for marks greater than or equal to 95
    print("Grade: A+")

elif marks>=80: #A grade for marks greater than or equal to 80
    print("Grade: A")

elif marks>=60: #B grade for marks greater than or equal to 60
    print("Grade: B")

elif marks>=50: #C grade for marks greater than or equal to 50
    print("Grade: C")

elif marks>=40: #D grade for marks greater than or equal to 40
    print("Grade: D")

else:   #F grade for marks less than 40
    print("Grade: F")
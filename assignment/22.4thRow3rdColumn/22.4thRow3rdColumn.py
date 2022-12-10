# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 13:17:58 2022

@author: Jayraj Derasari
"""
# =============================================================================
# 22. Create a .csv file which has ten students’ marks in seven subjects. Write a python program to
# import this file in your code. Print the data which is stored in the 4th column and 3rd row.
# =============================================================================

#importing pandas library
import pandas as pd

#reading csv file as a 
a = pd.read_csv(r"C:\Users\deras\Desktop\pythonPrograms\assignment\22.4thRow3rdColumn\22.4thRow3rdColumn.csv")
#printing value of 4th row and 3rd column
print(a.iloc[4, 3])

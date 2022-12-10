# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 00:06:31 2022

@author: Jayraj Derasari
"""

# =============================================================================
# 24. Create a .csv file which has ten students’ marks in seven subjects. Write a python program to
# find mean marks for each subject. Moreover, visualize the marks of all students in each subject
# using a box plot.
# =============================================================================

#importing CSV file using pandas
import pandas as pd
df = pd.read_csv(r"C:\Users\deras\Desktop\pythonPrograms\assignment\24.meanMarks\24.meanMarks.csv")

#Calculating mean marks for physics
meanPhysics = df.Phy.mean()
#Printing mean marks for physics
print("Physics", "=", meanPhysics)

#Calculating mean marks for physics
meanChemistry = df.Chem.mean()
#Printing mean marks for physics
print("Chemistry", "=", meanChemistry)

#Calculating mean marks for physics
meanMaths = df.Math.mean()
#Printing mean marks for physics
print("Maths", "=", meanMaths)

#Calculating mean marks for physics
meanGujarati = df.Gujarati.mean()
#Printing mean marks for physics
print("Gujarati", "=", meanGujarati)

#Calculating mean marks for physics
meanHindi = df.Hindi.mean()
#Printing mean marks for physics
print("Hindi", "=", meanHindi)

#Calculating mean marks for physics
meanSanskrit = df.Sanskrit.mean()
#Printing mean marks for physics
print("Sanskrit", "=", meanSanskrit)

#Calculating mean marks for physics
meanEnglish = df.Englllish.mean()
#Printing mean marks for physics
print("English", "=", meanEnglish)


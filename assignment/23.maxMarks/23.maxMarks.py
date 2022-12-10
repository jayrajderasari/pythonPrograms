# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 23:43:57 2022

@author: Jayraj Derasari
"""
# =============================================================================
# 23. Create a .csv file which has ten students’ marks in seven subjects. Write a python program to
# print the names of the students who have achieved the maximum marks in each subject.
# =============================================================================

#importing pandas library
import pandas as pd
#reading csv data file
df = pd.read_csv(r"C:\Users\deras\Desktop\pythonPrograms\assignment\23.maxMarks\23.maxMarks.csv")

#to print name of student with max marks in Physics
for i in range(0,len(df)):
    if df.Phy[i] == df.Phy.max():
        print(df.Name[i], ":", "Physics", "=", df.Phy[i])

#to print name of student with max marks in Maths
for i in range(0,len(df)):
    if df.Math[i] == df.Math.max():
        print(df.Name[i], ":", "Maths", "=", df.Math[i])
        
#to print name of student with max marks in Gujarati
for i in range(0,len(df)):
    if df.Gujarati[i] == df.Gujarati.max():
        print(df.Name[i], ":", "Gujarati", "=", df.Gujarati[i])

#to print name of student with max marks in Hindi
for i in range(0,len(df)):
    if df.Hindi[i] == df.Hindi.max():
        print(df.Name[i], ":", "Hindi", "=", df.Hindi[i])

#to print name of student with max marks in Sanskrit
for i in range(0,len(df)):
    if df.Sanskrit[i] == df.Sanskrit.max():
        print(df.Name[i], ":", "Sanskrit", "=", df.Sanskrit[i])

#to print name of student with max marks in Chemistry
for i in range(0,len(df)):
    if df.Chem[i] == df.Chem.max():
        print(df.Name[i], ":", "Chem", "=", df.Chem[i])

#to print name of student with max marks in English
for i in range(0,len(df)):
    if df.Englllish[i] == df.Englllish.max():
        print(df.Name[i], ":", "English", "=", df.Englllish[i])

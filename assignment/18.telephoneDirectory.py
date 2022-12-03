# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 17:41:58 2022

@author: Jayraj Derasari
"""

"""
18. Write a python program to store telephone directory record of a person using a dictionary
type variable. Print the stored details using get().
"""

#Defining telephone directory using variable as dictionary with few values
telephoneDirectory={
                    "JAYRAJ":"9409649494",
                    "KARTIK":"8780279796",
                    "ANUPAM":"9374062268"}

#taking name input of person whose number is required
name=str(input("Enter Name:"))
name = name.upper()

#Printing name and phone number
print(name, ":", telephoneDirectory.get(name))
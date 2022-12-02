# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 09:31:01 2022

@author: Jayraj Derasari
"""
units=int(input("Enter number of units consumed:"))

if units>100:
    if units>100 and units<=500:
        charges=0   #first 100 units are free
        units=units-100
        charges = 5*(units) #5rs per unit till 500 units after 100 units
    else:
        charges=0   #first 100 units are free
        units=units-100
        charges=charges+5*(400)     #5rs per unit till 500 units after 100 units
        units=units-400
        charges=charges+(units)*8   #charges of units after 500 units
else:
    charges=0
print("charges:", charges)
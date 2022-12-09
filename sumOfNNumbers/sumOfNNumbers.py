# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 18:32:35 2022

@author: Jayraj Derasari
"""
#Program to add numbers submitted by users till user enters character "N"

#defining sum and addNumber
addNumber='yes'
sum = 0

#Calculating the sum until the user writes no
while addNumber!='no':
    i = input("Do you want to add a number")
    i=i.lower()
    if(i=='yes'):
        n=int(input("Enter number:"))
        sum = (sum) + (n) 
    if(i=='no'):
        break
    
#Print the calculated sum    
print(sum)
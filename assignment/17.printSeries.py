# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 09:58:21 2022

@author: Jayraj Derasari
"""

"""
17. Write to program to print following series using looping concept (use while or for loop).
A. 1, 2, 3, 4 ........ 100
B. 100, 99, 98.......1
C. 1, 3, 5, 7........99
D. 2, 4, 8, 16, 32, 64
"""

#A. 1,2,3...100
for i in range(1,101):  #print all numbers from 1 to 100
    print(i)

#B. 100,99,98...1
for i in reversed(range(1,101)):    #print all numbers 1 to 100 in reversed order
    print(i)
    
#C. 1,3,5,7...99
for i in range(1,101):    #print all odd numbers 1 to 100
    if i%2==1:
        print(i)
        
#D. 2,4,8,16,32,64
for n in range(1,10):    #print numbers from 1 to 100 which are increasing power of 2
    for i in range(1,101):
        if i==2**n:
            print(i)
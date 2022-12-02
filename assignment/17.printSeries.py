# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 09:58:21 2022

@author: Jayraj Derasari
"""
#A. 1,2,3...100
for i in range(1,101):
    print(i)

#B. 100,99,98...1
for i in reversed(range(1,101)):
    print(i)
    
#C. 1,3,5,7...99
for i in range(1,101):
    if i%2==1:
        print(i)
        
#D. 2,4,8,16,32,64
for n in range(1,10):
    for i in range(1,101):
        if i==2**n:
            print(i)
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 14:16:43 2022

@author: Jayraj Derasari
"""

"""
13. Accept a number N from the user and print the first N elements of the Fibonacci series.
Hint: The Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21
Fibonacci series is defined as a sequence of numbers in which the first two numbers are 1
and 1, or 0 and 1, depending on the selected beginning point of the sequence, and each
subsequent number is the sum of the previous two. So, in this series, the nth term is the sum
of (n-1)th term and (n-2)th term.
Mathematically, the nth term of the Fibonacci series can be represented as:
tn = tn-1 + tn-2
"""

#taking value of n as lenght of series
n = int(input("Enter a number:"))

#Inititalising array of fibonacci and its initial values
fibonacci = [0]*n
fibonacci[0] = 0
fibonacci[1] = 1

#calculating further values of fibonacci series
for i in range(2,n):
    fibonacci[i] = fibonacci[i-1] + fibonacci[i-2]
    
#printing fibonacci
print(fibonacci)
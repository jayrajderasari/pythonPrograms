# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 13:06:09 2022

@author: Jayraj Derasari
"""

# =============================================================================
# 11. Write a program to accept two numbers and one mathematical operator. Calculate and
# display appropriate answer as shown below:
# Sample output:
# Enter first number : 5
# Enter mathematical operator : +
# Enter second number : 6
# 5 + 6 = 11
# =============================================================================

#taking values of variables and operators from user
x = int(input("Enter variable 1:"))
o = input("Enter mathematical operator:")
y = int(input("Enter variable 2:"))

#defining result
result = 0

#calculating result as per the mathematical operator
if o == '+':
    result = x + y
elif o == '-':
    result = x - y
elif o == '*':
    result = x * y
elif o == '/':
    result = x / y
elif o == '**':
    result = x ** y
elif o == '%':
    result = x % y
else:
    print('invalid mathematical operator')
    
#printing calculated result
print(x, o, y, '=', result)
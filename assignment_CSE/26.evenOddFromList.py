# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 00:17:10 2022

@author: Jayraj Derasari
"""

# =============================================================================
# 26. Write a python program using a loop to go through a list of elements. For each element, check
# if the number is even or odd. Store the output for each element in a separate list and merge both
# the lists together.
# =============================================================================

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l = len(list_1)
list_2 = [0]*l
for i in range(0,l):
    if list_1[i] % 2 == 0:
        list_2[i] = 'even'
    if list_1[i] % 2 == 1:
        list_2[i] = 'odd'
list_result = list_1 + list_2
print(list_result)
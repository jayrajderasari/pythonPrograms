# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 12:06:45 2022

@author: Jayraj Derasari
"""
# =============================================================================
# 21. Write a python program to print date and time being shown in your computer.
# =============================================================================

#importing datetime library
import datetime

#assigning and printintg current date and time value 
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))
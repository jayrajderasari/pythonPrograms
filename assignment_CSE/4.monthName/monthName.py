# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 23:49:12 2022

@author: Jayraj Derasari
"""

# =============================================================================
# 4. Write a Python program to read a month number and print corresponding month name.
# Sample output:
# Enter Month Number: 11
# November
# =============================================================================

from sys import exit
#taking month number as input
monthNumber = int(input("Enter number of Month:"))

#calculating month name from monthnumber
if monthNumber == 1:
    monthName = "January"
elif monthNumber == 2:
    monthName = "February"
elif monthNumber == 3:
    monthName = "March"
elif monthNumber == 4:
    monthName = "April"
elif monthNumber == 5:
    monthName = "May"
elif monthNumber == 6:
    monthName = "June"
elif monthNumber == 7:
    monthName = "July"
elif monthNumber == 8:
    monthName = "August"
elif monthNumber == 9:
    monthName = "September"
elif monthNumber == 10:
    monthName = "October"
elif monthNumber == 11:
    monthName = "November"
elif monthNumber == 12:
    monthName = "December"

#Printing invalid month number if monthnumber not between 1 to 100 and ending program
else:
    print("Invalid month number")
    exit()
    
#printing month name as output
print('Month name is', monthName)


# =============================================================================
# Printing month name using calendar library
# =============================================================================

#import calendar
#
#taking month number as input
#monthNumber=int(input("Enter number of Month:"))
#
##printing month name as output
#print('Month name is', calendar.month_name[monthNumber])

# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 23:49:12 2022

@author: Jayraj Derasari
"""

#taking month number as input
monthNumber=int(input("Enter number of Month:"))

#calculating month name
if monthNumber==1:
    monthName="January"
elif monthNumber==2:
    monthName="February"
elif monthNumber==3:
    monthName="March"
elif monthNumber==4:
    monthName="April"
elif monthNumber==5:
    monthName="May"
elif monthNumber==6:
    monthName="June"
elif monthNumber==7:
    monthName="July"
elif monthNumber==8:
    monthName="August"
elif monthNumber==9:
    monthName="September"
elif monthNumber==10:
    monthName="October"
elif monthNumber==11:
    monthName="November"
else:
    monthName="December"
    
#printing month name as output
print('Month name is', monthName)
#
#import calendar
#
#taking month number as input
#monthNumber=int(input("Enter number of Month:"))
#
##printing month name as output
#print('Month name is', calendar.month_name[monthNumber])
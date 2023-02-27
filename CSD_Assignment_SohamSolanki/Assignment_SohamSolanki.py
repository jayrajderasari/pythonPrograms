# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 22:32:36 2022

@author: Jayraj Derasari
"""

import pandas as pd
from pandas import DataFrame, Series
from matplotlib import pyplot as plt
df = pd.read_excel(r"C:\Users\deras\Desktop\pyth_CSD_SS\Dataset.xlsx")
 
# #1
# print(df.loc[14:39,['Name','NA_Sales']])



# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# pd.set_option('display.width', None)
# pd.set_option('display.max_colwidth', -1)

# #2
# mean_NA_Sales = df['NA_Sales'].mean()
# df['NA_Sales'].fillna(value=mean_NA_Sales, inplace=True)
# mean_EU_Sales = df['EU_Sales'].mean()
# df['EU_Sales'].fillna(value=mean_EU_Sales, inplace=True)
# mean_JP_Sales = df['JP_Sales'].mean()
# df['JP_Sales'].fillna(value=mean_JP_Sales, inplace=True)
# print(df)

#3

# for i in range(0,len(df)):
#     if df.Platform[i] == 'PS' or df.Platform[i]=='PS2' or df.Platform[i]=='PS3' or df.Platform[i]=='PS4':
#         print(df.iloc[0,:])

#4
# for i in range(0,len(df)):
#     if df.Genre[i] == 'Shooter':
#         print(df.iloc[0,:])


# #5
# for i in range(0,len(df)):
#     if df.Year[i]<2004 and df.NA_Sales[i]>10:
#         print(df.iloc[0,:])
        

# #6
# for i in range(0,len(df)):
#     if df.Year[i]>2004 and df.JP_Sales[i]>1:
#         print(df.iloc[0,:])
        
#7
# Game_ascending = df.sort_values(by='NA_Sales', ascending = True)
# print(Game_ascending)

#8

sum = df.EU_Sales.sum()
print('sum =', sum)

#9
mean = df.Global_Sales.mean()
print(mean)
median = df.Global_Sales.median()
print(median)


#10
a = []
b = []
for i in range (0, len(df)):
    if df.Platform[i]=='SNES':
        a.append(df.Name[i])
        b.append(df.Global_Sales[i])
plt.xlabel=('Name')
plt.ylabel('Global_Sales')
plt.title('platform="SNES" vs Global Sales')
plt.xticks(rotation=90)
plt.bar(a, b)
plt.show()

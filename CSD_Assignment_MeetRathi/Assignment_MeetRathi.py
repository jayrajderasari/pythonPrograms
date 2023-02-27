# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 20:01:49 2022

@author: Kartik_Derasari
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Dec 15 19:50:02 2022

@author: Kartik_Derasari
"""

import pandas as pd
from pandas import DataFrame, Series
from matplotlib import pyplot as plt
df = pd.read_excel(r"C:\Users\deras\Desktop\python_CSD_MR\Pack 6\Pack 6\Bank Aggregated Details.xlsx")
print(df.iloc[0,6])
print(df.iloc[0,7])
for i in range(1,len(df)):
    XYZCardWithdraw = (df.iloc[i,6])
    OtherCardWithdraw = (df.iloc[i,7])
    if XYZCardWithdraw > OtherCardWithdraw:
        ATMName = df.iloc[i,0]
        print(ATMName)

#8
x = (df.iloc[:,3])
y = (df.iloc[:,4]) 
plt.scatter(x, y, color= "cyan",  marker= "^", s=150)
plt.show()
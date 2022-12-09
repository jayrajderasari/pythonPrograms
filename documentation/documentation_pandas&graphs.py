# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 19:43:13 2022

@author: Jayraj Derasari
"""
from pandas import DataFrame, Series
import pandas as pd

#Defining Series
obj = Series(['a', 'b', 'c', 'd', 'e'], [1,2,3,4,5,])   
    # 1    a
    # 2    b
    # 3    c
    # 4    d
    # 5    e
    # dtype: object

#Defining DataFrame
data = {'Name' : ['Jayraj', 'Kartik', 'Jay', 'Raj'],
        'Roll No.' : [11, 12, 13, 15],
        'Programme' : ['Btech.', 'CSE', 'BTech.', 'BTech. CSE']
        }
frame = DataFrame(data)
    #   Name  Roll No.   Programme
    # 0  Jayraj        11      Btech.
    # 1  Kartik        12         CSE
    # 2     Jay        13      BTech.
    # 3     Raj        15  BTech. CSE    
    
# To check null/ NAN/ NA/ none values from dataset
# isnull()
# notnull()
# dropna()
# fillna()
# replace()
# interpolate()

### Using pandas for handling missing data###
import numpy as np
df = pd.DataFrame({
    'A':[1,2,np.nan],
    'B':[5,np.nan,np.nan],
    'C':[1,2,3],
    'D':[4,5,np.nan]
    })
    #      A    B  C    D
    # 0  1.0  5.0  1  4.0
    # 1  2.0  NaN  2  5.0
    # 2  NaN  NaN  3  NaN

#Solution1: remove missing values
df = pd.DataFrame({
    'A':[1,2,np.nan],
    'B':[5,np.nan,np.nan],
    'C':[1,2,3],
    'D':[4,5,np.nan]
    })
print(df.isnull())      #print if the value is null or not
    #       A      B      C      D
    # 0  False  False  False  False
    # 1  False   True  False  False
    # 2   True   True  False   True
print(df.dropna(axis='rows'))       #drop rows which have atleast one none value
    #      A    B  C    D
    # 0  1.0  5.0  1  4.0
print(df.dropna(axis='columns'))       #drop columns which have atleast one none value
    #    C
    # 0  1
    # 1  2
    # 2  3

# Solution2: Imputation - input as 0 or mean
df = pd.DataFrame({
    'A':[1,2,np.nan],
    'B':[5,np.nan,np.nan],
    'C':[1,2,3],
    'D':[4,5,np.nan]
    })
df.fillna(value=0, inplace=True)        #to replace True to 0
print(df)
    #      A    B  C    D
    # 0  1.0  5.0  1  5.0
    # 1  2.0  0.0  2  5.0
    # 2  0.0  0.0  3  0.0

# #Imputate to mean#
df = pd.DataFrame({
    'A':[1,2,np.nan],
    'B':[5,np.nan,np.nan],
    'C':[1,2,3],
    'D':[4,5,np.nan]
    })
mean = df['A'].mean()
print('mean =', mean)
df.fillna(value=mean, inplace=True)
print(df)
    # mean = 1.5
    #      A    B  C    D
    # 0  1.0  5.0  1  4.0
    # 1  2.0  1.5  2  5.0
    # 2  1.5  1.5  3  1.5
    
# ##Imputate to median##
df = pd.DataFrame({
    'A':[1,2,np.nan],
    'B':[5,np.nan,np.nan],
    'C':[1,2,3],
    'D':[4,5,np.nan]
    })
median = df['A'].median()
print('Median =', median)
df.fillna(value=median, inplace=True)
print(df)
    # Median = 1.5
    #      A    B  C    D
    # 0  1.0  5.0  1  4.0
    # 1  2.0  1.5  2  5.0
    # 2  1.5  1.5  3  1.5

##Imputate to ffill##
df = pd.DataFrame({
    'A':[1,2,np.nan],
    'B':[5,np.nan,np.nan],
    'C':[1,2,3],
    'D':[4,5,np.nan]
    })
df = df.fillna(method = 'ffill')
print(df)
    #      A    B  C    D
    # 0  1.0  5.0  1  4.0
    # 1  2.0  5.0  2  5.0
    # 2  2.0  5.0  3  5.0
    
#make an array from a to b with equal spaces
arrange = np.arange(4, 20, 3) #to arrange values from 4 to 20 with difference of 3
print(arrange)
    # [ 4  7 10 13 16 19]
    
###Importing a CSV file###
import pandas as pd
from matplotlib import pyplot as plt
sample_data = pd.read_csv('22.csv')
sample_data = sample_data.Name.iloc[0]      #Jayraj

#Generate random numbers between 0 and 1
r = np.random.rand()    #if want multiple numbers then enter the number in (), it will be in list data type
print(r)                



# ###Line Plots###

#Single line plot#
from matplotlib import pyplot as plt
x = [1, 2, 3]   #define x
y = [1, 4, 9]   #define y
plt.title("test plot")  #define title of graph
plt.xlabel("x") #define label of x
plt.ylabel("y") #define label of y
plt.plot(x,y)   #plot x,y graph

#Multi line plot#
x = [1, 2, 3]   #define x
y = [1, 4, 9]   #define y
z = [10, 5, 0]  #define z
plt.title("test plot")  #define title of graph
plt.xlabel("x") #define label of x
plt.ylabel("y and z")   #define label of y
plt.plot(x,y, 'g', linewidth=5) #mark x-y line as green
plt.plot(x,z, 'r', linewidth=5) #mark y-z line as red
plt.legend(["This is x to y","This is x to z"]) #define a legend to show which line is what

#Sine curve plot using numpy with customisation and plotting points with limits#
import numpy as np
from matplotlib import pyplot as plt
a = np.arange(0, 3 * np.pi, 0.1)
b = np.sin(a)
plt.title("Sin wave form")
plt.plot(a,b)
plt.plot(a, b, color='green', linestyle='dashed', linewidth = 3, marker='o', markerfacecolor='red', markersize=8) 
plt.ylim(0,4) 
plt.xlim(0,4)
plt.show() 

#Scatter Plot#
x = [1,2,3,4,5,6,7,8,9,10] 
y = [2,4,5,7,6,8,9,11,12,12] 
plt.scatter(x, y, label= "stars", color= "green",  marker= "*", s=30)       #plotting points in graph without joining them
plt.legend()

#Plotting a bar graph#
from matplotlib import pyplot as plt
a = [1, 2, 3, 4, 5]
b = [10, 24, 36, 40, 5]
label = ['one', 'two', 'three', 'four', 'five']
plt.bar(a, b, tick_label=label, width=1, color = ['red', 'green'])
plt.xlabel=('x-axis')
plt.ylabel('y-axis')
plt.title('Bar chart')
plt.show()

#Plotting a Histogram graph#
import matplotlib.pyplot as plt 
x = [21,22,23,4,5,6,77,8,9,10,31,32,33,34,35,36, 37,18, 49, 50,100] #data
num_bins = 5        #no bars req
n, bins, patches = plt.hist(x, num_bins, facecolor='blue', rwidth=0.9)
plt.xlabel=('x-axis')
plt.ylabel('y-axis')
plt.title('Bar chart')
plt.show()


#Plotting Pie chart#
activities = ['eat', 'sleep', 'work', 'play']
hours = [3, 7, 8, 6]
colours = ['r', 'g', 'y', 'b']
plt.pie(hours, labels = activities, colors=colours, startangle = 90, shadow='True', explode=(0, 0, 0.1, 0), radius=1.2, autopct = '%1.1f%%')
plt.legend()
plt.show()
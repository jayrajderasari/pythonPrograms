# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 20:58:47 2022

@author: Jayraj Derasari
"""
""" Documentation for python"""

# =============================================================================
# Working with variables
# =============================================================================

#Declaring variables
x = 5
y = 2.5
z = True
name = "jayRAj"
x, y, z, name = (5, 2.5, True, 'jayRAj')


#datatype of variable
print(type(y))  #<class 'float'>

#types for concatenating
print("My name is", name)   #My name is jayRAj
print("My name is {n}" .format(n=name)) #My name is jayRAj
print(f"My name is {name}") #My name is jayRAj

# =============================================================================
# Strings
# =============================================================================

#Capitalize
print(name.capitalize())    #Jayraj

#Upper and lower case
print(name.upper()) #JAYRAJ
print(name.lower()) #jayraj

#Swap Case
print(name.swapcase())  #JAYraJ

#Length of string
print(len(name))    #6

#Replace
str = 'Hello World'
print(str.replace('World', 'everyone')) #Hello everyone

#Count number of times a letter repeats
print(str.count('H'))   #1

#Starts with
print(str.startswith('Hello'))  #True

#Ends with
print(str.endswith('d'))    #True

#Split string to list
print(str.split())  #['Hello', 'World']

#Find position
print(str.find('r'))    #8

#is all alphanumeric
print(str.isalnum())    #False

#alphabetic
print(str.isalpha())    #False

#numeric
print(str.isnumeric())  #False

#remove extra spaces form starting and end
str = "  Jayraj   "
print(str.strip())      #Jayraj

# =============================================================================
# Working with Lists
# =============================================================================

fruits = ['Apples', 'Oranges', 'Grapes', 'Pears']

#print a value
print(fruits[1])    #Oranges

#get length
print(len(fruits))  #4

#append - add new value to last of list
fruits.append('Mangoes')    #['Apples', 'Oranges', 'Grapes', 'Pears', 'Mangoes']

#Remove a value completely from value
fruits.remove('Pears')  #['Apples', 'Oranges', 'Grapes', 'Mangoes']

#Remove with pop - remove value from index number
fruits.pop(2)   #['Apples', 'Oranges', 'Mangoes']

#Reverse list
fruits.reverse()    #['Mangoes', 'Oranges', 'Apples']

#Sort - arrange alphabetically
fruits.sort()   #['Apples', 'Mangoes', 'Oranges']

#Reverse sort
fruits.sort(reverse=True)   #['Oranges', 'Mangoes', 'Apples']

#Change a value
fruits[0] = 'Blueberries'   #['Blueberries', 'Mangoes', 'Apples']

# Insert to position
fruits.insert(2, 'Strawberries')    #['Blueberries', 'Mangoes', 'Strawberries', 'Apples']

# =============================================================================
# Tuple - List which dont allow duplicates and is unordered, unchangable, unindexed
# =============================================================================

#tuples have () brackets while lists have [] brackets
fruits = ('Blueberries', 'Mangoes', 'Strawberries', 'Apples')

#Tuples dont change values
#fruits[0] = 'Grapes'    #ERROR

# =============================================================================
# Sets
# =============================================================================

#Sets have {} brackets#

fruits_set={'Apples', 'Oranges', 'Grapes'}

#Check if in set
print('Apples' in fruits_set)   #True

#Add to set
fruits_set.add('Mango') #{'Apples', 'Grapes', 'Oranges', 'Mango'}

#remove from set
fruits_set.remove('Grapes') #{'Apples', 'Oranges', 'Mango'}

#Clear set
fruits_set.clear()  #set()

#Delete set
del fruits_set      #to delete the set as it was never defined


# =============================================================================
# Dictionary
# =============================================================================

#creating a dictionary
person = {
    'first_name':'Jayraj',
    'last_name':'Derasari'
    }

#Constructor
person2 = dict(first_name = 'Kartik', last_name = 'Derasari')

#print values
print(person['first_name'])     #Jayraj
print(person.get('last_name'))  #Derasari

print(person)
#Add value
person['phone'] = '9409649494'
print(person)   #{'first_name': 'Jayraj', 'last_name': 'Derasari', 'phone': '9409649494'}

#print dict keys and items
print(person.keys())    #dict_keys(['first_name', 'last_name', 'phone'])
print(person.items())   #dict_items([('first_name', 'Jayraj'), ('last_name', 'Derasari'), ('phone', '9409649494')])

#copy dicts
person2 = person.copy()
print(person2)  #{'first_name': 'Jayraj', 'last_name': 'Derasari', 'phone': '9409649494'}

#Remove items
del(person['phone'])
person.pop('last_name')
print(person)   #{'first_name': 'Jayraj'}

#clear the dictionary
person.clear()
print(person)   #{}

#Length of dictionary
print(len(person2)) #3

#Lists of dict
people = [
    {'name':'Jayraj', 'Roll_No':'Au2240109'},
    {'name':'Kartik', 'Roll_No':'Au1234567'}
    ]
print(people[1])    #{'name': 'Kartik', 'Roll_No': 'Au1234567'}


# =============================================================================
# Functions
# =============================================================================

#Creating a function and using it
def sumOfNumbers(): 
    total = a+b
    return total
a = 5
b = 5
print(sumOfNumbers())   #10
sumation = sumOfNumbers()
print(sumation)         #10
#OR
def intro(name):
    print(f"my name is {name}")
intro("Jayraj")     #my name is Jayraj

#using lambda
getSum = lambda a,b : a+b
print(getSum(10,12))    #22

# =============================================================================
# Conditional Operations
# =============================================================================
#if elif and else
x = 10
y = 20
if x>y:
    print("x is greater than y")
elif x<y:
    print("y is greater than x")    
else:
    print("x equals y")

#nested if:
if x>y:
    print("x is greater than y")
else:
    if x<y:
        print("y is greater than x")    
    else:
        print("x equals y")

#Using logical operators
if x>2 and x<10:
    print("x is greater than 2 and less than 10")
if x<=2 or x>=10:
    print("x is greater than or equal to 10 or less than or equal to 2")
if not(x==y):
    print("x not equals to y")

#using membership operators
no = [1,2,3,4,5]
if x in no:
    print("x is in 1 to 5")
if x not in no:
    print(x not in no)
    
#Using identity operators
x = 20
y = 20
if x is y:
    print(x is y)    
# =============================================================================
# Working with loops
# =============================================================================
    
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears', 'Mangoes']
#printing output using for loop
for fruit in fruits:
    print(f'current fruit is {fruit}')
        # current fruit is Apples
        # current fruit is Oranges
        # current fruit is Grapes
        # current fruit is Pears
        # current fruit is Mangoes

#using break and continue
for fruit in fruits:
    if fruit ==  'Oranges':
        continue
    if fruit == 'Pears':
        break
    print(f'fruit is {fruit}')
        # current fruit is Apples
        # current fruit is Grapes

#using range
for i in range (0,11):
    print(i, end = "" )
print("")

#While loop
while i<=20:
    print(i, end="")
    i += 1
print("")    
    
# =============================================================================
# Working with external modules/libraries
# =============================================================================
import datetime

#printing date importing whole datetime
today = datetime.date.today()
print(today)
    
#printing date importing only date from datetime
from datetime import date 
today = date.today()
print(today)

from time import ctime
time = ctime()
print(time)


# =============================================================================
# Working with files
# =============================================================================

#opening or creating a file
file = open('new.doc', 'w')

#getting info of a file
print("Name of file:", file.name)
print("Working mode of file:", file.mode)
print("File is closed?", file.closed)

#writing to a file
file.write('Hello World! I am Jayraj Derasari.')
file.close()

#append data of a file
file = open('new.doc', 'a')
file.write(" I love swimming!")
file.close()

#Printing a file
file = open('new.doc', 'r+')
text = file.read()
print(text)

# =============================================================================
# Working with a JSON file
# =============================================================================

import json

#defining sample json file
userJSON = '{"First_Name" : "Jayraj", "Last_Name" : "Derasari", "Phone_Number" : "9409649494"}'

#Converting and printing JSON file to Dictionary
user = json.loads(userJSON)
print(user)
print(user['First_Name'])

#defining dictionary
reportCard ={'Maths':89, 'Science':70, 'English':60}
#convertinng dictionary to JSON file and printing it
reportCardJSON = json.dumps(reportCard)
print(reportCardJSON)

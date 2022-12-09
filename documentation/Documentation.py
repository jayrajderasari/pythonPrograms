# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 20:58:47 2022

@author: Jayraj Derasari
"""
""" Documentation for python"""

#Declaring variables
x = 5
y = 2.5
z = True
name = "jayRAj"
x, y, z, name = (5, 2.5, True, 'jayRAj')

#datatype of string
print(type(y))  #<class 'float'>

#types for concatenating
print("My name is", name)   #My name is jayRAj
print("My name is {n}" .format(n=name)) #My name is jayRAj
print(f"My name is {name}") #My name is jayRAj

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

#Count
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


##Playing with lists##

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

#Sort - arrange alphabetically
fruits.sort()   #['Apples', 'Mangoes', 'Oranges']

#Reverse sort
fruits.sort(reverse=True)   #['Oranges', 'Mangoes', 'Apples']

#Change a value
fruits[0] = 'Blueberries'   #['Blueberries', 'Mangoes', 'Apples']

# Insert to position
fruits.insert(2, 'Strawberries')    #['Blueberries', 'Mangoes', 'Strawberries', 'Apples']


##Tuple - List which dont allow duplicates and is unordered, unchangable, unindexed##
##tuples have () brackets while lists have [] brackets

fruits = ('Blueberries', 'Mangoes', 'Strawberries', 'Apples')

#Tuples dont change values
#fruits[0] = 'Grapes'    #ERROR

###    Sets    ###
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


##Dictionary##

#create
person = {
    'first_name':'Jayraj',
    'last_name':'Derasari'
    }

#Constructor
person2 = dict(first_name = 'Kartik', last_name = 'Derasari')

#print values
print(person['first_name'])
print(person.get('last_name'))

#Add value
person['phone'] = '9409649494'

#print dict keys and items
print(person.keys())
print(person.items())

#copy dicts
person2 = person.copy()

#Remove item
del(person['phone'])
person.pop('last_name')

#clear the dictionary
person.clear()

#Length of dictionary
print(len(person2))

##Lists of dict
people = [
    {'name':'Jayraj', 'Roll_No':'Au2240109'},
    {'name':'Kartik', 'Roll_No':'Au1234567'}
    ]
print(people[1])


#####
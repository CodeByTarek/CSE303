# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 09:31:47 2021

@author: User
"""

#%%
def myfirstfunction():
    print("Hello World")
    
myfirstfunction()

#%%

length = float(input("Enter Length: "))
width = float(input("Enter width: "))

def calculateArea(length, width):
    return length*width

x = calculateArea(length,width)
print("The area of the rectangle is ", x)

#%%
# Lambda Functions

def square(x):
    return x**2

print(square (10))

square1 = lambda x: x*x #function with no name
print(square1(100))

#%%
def cube(n):
    return n*n*n

list1 = [2, 4, 6, 8, 10]
# compute cubic value of each element and put them 
# inside another list

result = []
for i in list1:
    result.append(cube(i))
    
print(result)

#%%
# demonstrating list comprehension
def cube(n):
    return n*n*n

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = [cube(i) for i in list1 if i%2==1]
# your_list = [your_value iterating_over_an_existing_list]
print(result)

#%%
#Given a list of integers (at least 10), find the values
#which are greater than the mean value and put them 
#into a new list. you must use list comprehension 
#to do that.

list1 = [1,2,3,4,5,6,7,8,9,10]
mean = sum(list1)/len(list1)
result = [i for i in list1 if i>mean]
print(result) 


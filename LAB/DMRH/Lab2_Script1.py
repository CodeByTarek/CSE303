# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 07:57:44 2021

@author: User
"""

# its a comment

#%%
print("Good morning")
print("CSE303")

#%%
a = 10
b = 5
print("Sum = ", a+b)

#%%
# Demonstrating List


mylist = [1,2,3,4]
mylist1 = []

print(mylist[1])

#  0  1  2  3  4  5
# -6 -5 -4 -3 -2 -1

print(mylist[-2]) #3

anotherList = mylist[0:2] # 1, 2
print(anotherList)

anotherList.append(10)
print(anotherList)

mylist2 = mylist.copy()
print(mylist2)
print(id(mylist))
print(id(mylist2))

#%%
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 1, 1]
mylist1 = [10, 20, 30, 40]

print(mylist.count(1))
mylist.extend(mylist1)
print(mylist)
#%%
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 1, 1]
print(mylist.index(1))
mylist.remove(1)
print(mylist)
#%%
country = ['Bangladesh', 'India', 'USA', 'Russia']
country.insert(0, 'Japan')
print(country)

country.pop(3)
print(country)

country.remove('Ban')
print(country)

#%%
mylist = [1, 2, 3, 4, 5, 6, 7, 8, 1, 1]

mylist.sort(reverse=True)
print(mylist)

#%%
def comp(elem):
    return elem[1]

mypoints = [(1, 3), (3, 2), (4, 5), (2, 1)]

mypoints.sort(key=comp, reverse = True)

print(mypoints)
#%%
def comp(elem):
    return len(elem)

country = ['Bangladesh', 'India', 'USA', 'Russia']

country.sort(key = comp, reverse=True)

print(country)

#%%
mytuple = (2, 1, 2, 3)
print(mytuple.index(3))
print(mytuple.count(3))

#%%
# Demonstrating Dictionaries

phonebook = {
"John" : 938477566,
"Jack" : 938377264,
"Jill" : 947662781
}

print(phonebook)

print(phonebook['Jill'])

for k, v in phonebook.items():
    print("%s has phone number %d"%(k, v))

#%%
keys = {'a', 'e', 'i', 'o', 'u'}
value = 'vowel'

vowels = dict.fromkeys(keys, value)
print(vowels)

#%%
phonebook = {
"John" : 938477566,
"Jack" : 938377264,
"Jill" : 947662781
}

print(phonebook)

phonebook.pop('John')

print(phonebook)

phonebook.popitem()
print(phonebook)

#%%
person = {'name': 'Alice', 'age': 22}

cgpa1 = person.setdefault('cgpa', 3.5)
print(person)
print(cgpa1)
print(person['cgpa'])

#%%

dict1 = {'Bangladesh':'Dhaka','India':'Delhi'}
dict2 = {'China':'Beijing'}

dict1.update(dict2)
print(dict1)



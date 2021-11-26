# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 16:25:50 2021

@author: TAREK
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('pima-indians-diabetes.csv', header = None)

df.columns = ['Pregnancies','Glucose', 'BloodPressure', 'SkinThickness', 'Insulin','BMI','DiabetesPedigreeFunction', 'Age', 'ClassVariable']

df.head()

df.info()
print ('Number of rows: ', df.shape[0])
print ('Number of columns: ', df.shape[1])

print(df.describe())
#%%
labels = ['0: Healthy', '1: Diabetic']
sizes = df['ClassVariable'].value_counts(sort = True)

colors = ["green","red"]
explode = (0.05,0) 
 
plt.figure (figsize=(10,10))
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90,)

plt.title('Percentage of diabetes Pateint')
plt.show()

#%%

def A2018_2_60_079():
    BP = df[["DiabetesPedigreeFunction","ClassVariable"]].query("ClassVariable==0")
    BP_0 = BP["DiabetesPedigreeFunction"]
    
    BP = df[["DiabetesPedigreeFunction","ClassVariable"]].query("ClassVariable==1")
    BP_1 = BP["DiabetesPedigreeFunction"]
    
    columns = [BP_0,BP_1]
    fig,ax = plt.subplots()
    box = ax.boxplot(columns, patch_artist=True)
    ax.boxplot(columns)
    plt.title("Test Result for Diabetes vs Pedigree Function")
    plt.xlabel("Test Result for Diabetes")
    plt.ylabel("Pedigree Function")
    plt.xticks([1, 2], ['0 : Negetive', '1 : Positive'])
    colors = ['green', 'red']

    for patch, color in zip(box['boxes'], colors):
        patch.set_facecolor(color)
    
    plt.show()
A2018_2_60_079()


#%%
# x = pregnancy, y = age
plt.figure (figsize=(8,6), dpi = 80)
df.plot(kind='scatter', x='Pregnancies', y='Age',color = 'red',marker='*')
plt.xlabel('Pregnancies')             
plt.ylabel('Age')
plt.title('Pregnancies vs Age Scatter Plot')
plt.show()
#%%
# x = Glucose, y = age
plt.figure (figsize=(8,6), dpi = 80)
df.plot(kind='scatter', x='Glucose', y='Age',color = 'green',marker='p')
plt.xlabel('Glucose')              
plt.ylabel('Age')
plt.title('Glucose vs Age Scatter Plot')
plt.show()
#%%
# x = BMI, y = Age
plt.figure (figsize=(8,6), dpi = 80)
df.plot(kind='scatter', x='BMI', y='Age',color = 'blue',marker='x')
plt.xlabel('BMI')            
plt.ylabel('Age')
plt.title('BMI vs Age Scatter Plot')
plt.show()

#%%
# x = ClassVariable, y = Age
plt.figure (figsize=(8,6), dpi = 80)
df.plot(kind='scatter', x='BloodPressure', y='Age',color = 'Salmon',marker='d')
plt.xlabel('BloodPressure')            
plt.ylabel('Age')
plt.title('BloodPressure vs Age Scatter Plot')
plt.show()

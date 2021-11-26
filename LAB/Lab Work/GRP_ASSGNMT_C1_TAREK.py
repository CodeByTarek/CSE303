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
#Plot 1

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



%##
#Plot 2

x1 = df["Pregnancies"]
x2 = df["Glucose"]
x3 = df["BMI"]
x4 = df["DiabetesPedigreeFunction"]
y1 = df["Age"]
y2 = df["BloodPressure"]

plt.figure (figsize=(20,10), dpi = 100)
plt.subplot(2,2,1)
plt.scatter([x1],[y1], color = 'red',marker='*')
plt.xlabel('Pregnancies')             
plt.ylabel('Age')
plt.title('Pregnancies vs Age Scatter Plot')  

plt.subplot(2,2,2)
plt.scatter([x2],[y1], color = 'green',marker='p')
plt.xlabel('Glucose')              
plt.ylabel('Age')
plt.title('Glucose vs Age Scatter Plot')


plt.subplot(2,2,3)
plt.scatter([x3],[y1], color = 'blue',marker='x')
plt.xlabel('BMI')            
plt.ylabel('Age')
plt.title('BMI vs Age Scatter Plot')

plt.subplot(2,2,4)
plt.scatter([x4],[y2], color = 'Salmon',marker='d')
plt.xlabel('Diabetes')            
plt.ylabel('Diastolic')
plt.title('Diastolic blood pressures against Diabetes function')
plt.subplots_adjust(hspace = 0.3)
plt.show()
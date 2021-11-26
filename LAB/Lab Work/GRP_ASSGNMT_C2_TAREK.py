# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 03:40:35 2021

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

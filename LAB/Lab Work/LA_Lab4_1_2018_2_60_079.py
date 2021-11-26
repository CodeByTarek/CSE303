# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 00:46:44 2021

@author: TAREK
"""
#%%

#Student Id : 2018-2-60-079

#Lab Assignment - 1

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv('dataset_lab04.csv')

df.info()

#%%
#Task 1
def lab04_Task1_2018_2_60_079():
    print ('Number of rows: ', df.shape[0])
    print ('Number of columns: ', df.shape[1])
    print(df.shape)
    print(df.describe())
lab04_Task1_2018_2_60_079()
#%%
#Task 2
def lab04_Task2_2018_2_60_079():
    print(df[["Time", "Amount"]].describe())
lab04_Task2_2018_2_60_079()
#%%
#Task 3
def lab04_Task3_2018_2_60_079():
    print(df[['Amount']].mean())
    print(df[['Amount', 'Time']].mean())
    print(df[['Amount']].median())
    print(df[['Time']].median())
    print(df[['Amount']].std())
    print(df[['Time']].std())
    print(df[['Amount']].var())
    print(df[['Time']].var())
lab04_Task3_2018_2_60_079()


#%%
#Task 4
def lab04_Task4_2018_2_60_079():
    df.boxplot(column=['Time','Amount'])
    Time_Q1=df[['Time']].quantile(0.25)
    Time_Q3=df[['Time']].quantile(0.75)
    Amount_Q1=df[['Amount']].quantile(0.25)
    Amount_Q3=df[['Amount']].quantile(0.75)
    print(df[['Time']].quantile(0.25))
    print(df[['Time']].mean())
    print(df[['Time']].quantile(0.75))
    print(Time_Q3-Time_Q1)
    print(df[['Amount']].quantile(0.25))
    print(df[['Amount']].mean())
    print(df[['Amount']].quantile(0.75))
    print(Amount_Q3-Amount_Q1)
    print ("THERE IS NO OUTLIERS FOUND IN THESE BOX PLOTS BECAUSE THERE IS NO ABNORMAL DISTANCES AMONG VALUES")
lab04_Task4_2018_2_60_079()

#%%
#Task 5
def lab04_Task5_2018_2_60_079():
    print(df.hist(column=['Time']))
    print(df.corr())
    print("Kurtusis:")
    kurtusis=df['Time'].kurtosis()
    skew=df['Time'].skew()
    print(kurtusis)
    print("Skewness:")
    print(skew)
    if skew < 0:
        print("Right Skew")
    elif skew == 0:
        print("Normal Distribution")
    else:
        print("Left Skew")
    if kurtusis>3:
        print("Leptokurtic")
    elif kurtusis<3:
        print("Platykurtic")
    else:
        print("Mesokurtic")
lab04_Task5_2018_2_60_079()

#%%
#Task 6
def lab04_Task6_2018_2_60_079():
    df1 = df.query('Class == 0')
    df2= df.query('Class == 1')

    total = len(df)
    check1 = len(df1)
    check2 = len(df2)

    print("Non-Fraudulent:",(check1/total*100))
    print("Fraudulent:",(check2/total*100))
lab04_Task6_2018_2_60_079()

#%%
#Task 7
def lab04_Task7_2018_2_60_079():
    df['Class'].value_counts().plot(kind='hist')
lab04_Task7_2018_2_60_079()

#%%
#Task 8
def lab04_Task8_2018_2_60_079():
    x1 = df.loc[df['Class']==0]
    y1 = df.loc[df['Class']==1]
    z = x1.size*100/df.size
    o = y1.size*100/df.size
    x2 = [1,2]
    y2 = [z,o]
    tick_label = ['zero', 'one']
    plt.bar(x2,y2,tick_label=tick_label,width= 0.4,color=['green','red'])
    plt.xlabel('Class')
    plt.ylabel('Percentage')
    plt.show()
lab04_Task8_2018_2_60_079()

#%%
#Task 9
def lab04_Task9_2018_2_60_079():
    df.hist(column=['V1'], bins = 50)
    print('V1" column is negetively skeweed')
    df.hist(column=['V2'], bins = 50)
    print('"V2" column is positively skeweed')
    df.hist(column=['V3'], bins = 50)
    print('V3 column is "platykurtic".')
    df.hist(column=['V4'], bins = 50)
    print('V4 column is "leptokurtic".')
    plt.show()
lab04_Task9_2018_2_60_079()

#%%
#Task 10
def lab04_Task10_2018_2_60_079():
    corr_matrix = df.corr().abs()
    x = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k = 1)
    .astype(np.bool))
    to_drop = [column for column in x
    .columns if any(x[column] > 0.95)]
    df.drop(to_drop, axis = 1, inplace = True)
    print(x)
lab04_Task10_2018_2_60_079()

#%%
#Task 11
def lab04_Task11_2018_2_60_079():
     df.plot.scatter(x=['Time'], y=['V2'])
lab04_Task11_2018_2_60_079()

#%%
#Task 12
def lab04_Task12_2018_2_60_079():
    min_value = 99999
    
    for i in df.columns:
        for j in df.columns:
            if i == j:
                continue
            else:
                correlation = df[i].corr(df[j])
                if correlation < min_value:
                    min_value = correlation
                    min_indx1 = i
                    min_indx2 = j
    print(min_indx1, min_indx2)
lab04_Task12_2018_2_60_079()


#%%
#Task 13
def lab04_Task13_2018_2_60_079():   
     df.plot.scatter(x ='Time', y ='Amount')
lab04_Task13_2018_2_60_079()

#%%
#Task 14
def lab04_Task14_2018_2_60_079():   
    df.boxplot(column=['Amount'])
lab04_Task14_2018_2_60_079()

#%%
#Task 15
def lab04_Task15_2018_2_60_079():
    class_0_V2 = df[["Amount","Class"]].query("Class==0")
    V2_0 = class_0_V2["Amount"]
    
    class_0_V2 = df[["Amount","Class"]].query("Class==1")
    V2_1 = class_0_V2["Amount"]
    
    columns = [V2_0,V2_1]
    fig,ax = plt.subplots()
    ax.boxplot(columns)
    plt.show()
lab04_Task15_2018_2_60_079()
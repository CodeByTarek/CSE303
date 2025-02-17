# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 23:39:18 2021

@author: alam_pobon
"""

# Model 4 = Ridge Regression

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split


#%%   #Reading Dataset

train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')
submission = pd.read_csv('sample_submission.csv')

#%%

print(train.shape)
print(train.describe())

#%%     #checking the null value in the train dataset.
print(train.isnull().sum())

#%%  # Data Exploration

# Storing the Categorical Variable and Continoues Variable into lists

cat_cols = [feature for feature in train.columns if 'cat' in feature]
cont_cols = [feature for feature in train.columns if 'con' in feature]

#%%

#Histogram of Continues variable of train dataset...
train[cont_cols].hist(bins = 30, figsize = (20, 15))


#%%

#top 10 value which appears in a particular Categorical Column
for cat in cat_cols:
    plt.figure(figsize = (7,5))
    if cat=='cat0':
        top = train[cat].value_counts().sort_values(ascending=False).head(2)  #Cat0 has only 2 unique variable.
        plt.bar(top.index,top)
        plt.xlabel(cat)
        plt.ylabel('Number Of value Occurs')
        plt.grid()
        plt.show()
    else:
        top = train[cat].value_counts().sort_values(ascending=False).head(10) #top 10 unique value
        plt.bar(top.index,top)
        plt.xlabel(cat)
        plt.ylabel('Number Of value Occurs')
        plt.grid()
        plt.show()
        
        
#%%

# Target Value Distribution of Training Dataset
label = train['target'].value_counts().index  #Class Value = 0,1
value = train['target'].value_counts()    #how many value occurs for class 0 and class 1
ax,fig = plt.subplots(1,2,figsize=(20,5))

# pie Chart
plt.subplot(1,2,1)
plt.pie(value , labels =label,autopct='%1.1f%%')

#bar chart
plt.subplot(1,2,2)
plt.bar(label, value, color ='green')
plt.xlabel("Class Variable")
plt.ylabel("How many values")
plt.xticks(label,fontsize=15)
plt.grid()
plt.show()


#%%

#boxplot of training dataset..

train_cont = train[cont_cols] #splitting only the continues varibles columns from Train Dataset
plt.figure(figsize = (20,6))
plt.title('Boxplot of Training dataset')
plt.boxplot(train_cont,labels=cont_cols)
plt.grid()
plt.show()



#%%

# Correlation among all the Continues Column of Train Dataseet
train_cont = train[cont_cols]
corr = train_cont.corr()
fig = plt.figure(figsize = (20, 5))
sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm')
plt.show()


#%%

#for train dataset
# ID column is not needed
# Cont10 and Cont0 has high correlation which is 0.9
# Cont2 and Cont1 has also high correlation which is 0.86

X = train.drop(['id','cont2','cont10', 'target'], axis=1)
y = train.target

# We will also remove these column from test dataset
test_data = test.drop(['id','cont2','cont10'], axis=1)

#%%

# Dimention of X of Train Dataset..
print(X.shape)

# Dimention of Test Dataset..
print(test_data.shape)


#%%   #Data Preprocessing

# Label Encoding of X from Train Dataset and also from Test Dataset

from sklearn.preprocessing import OrdinalEncoder,StandardScaler,LabelEncoder

le = LabelEncoder()
for cat_name in cat_cols:
    le = LabelEncoder()
    if X[cat_name].dtype=='object':
        X[cat_name] = le.fit_transform(X[[cat_name]])
        test_data[cat_name] = le.fit_transform(test_data[[cat_name]])

print("Train Data")        
print(X)

print('Test Dataset')
print(test_data)


#%%   #it will calculate the sigmoid value and then divide them into class

def classDetect(pred):
    y_pred=[]
    for i in pred:
        z = 1/(1 + np.exp(-i))
        if z >=0.5:
            y_pred.append(1)
        else:
            y_pred.append(0)
    return y_pred


#%%   # Applying Support Vector Machine

from sklearn.linear_model import Ridge

# Instance Of the Model..
ridge = Ridge()

# Model fit...
ridge.fit(X,y)   # X and y is from train Dataset...
print('end')



#%%
# Prediction Value..
y_pred=ridge.predict(X)   #Prediction for X..here X is from Train Dataset...

#y_pred Value
print(y_pred)

# calculating the sigmoid value and then based on this value it will divide into class
y_pred = classDetect(y_pred)


#%%  #Result Checking

# Result Checking...

from sklearn import metrics
print("Confussion Matrix: ", metrics.confusion_matrix(y, y_pred))   #y = Actual value
print("Accuracy:",metrics.accuracy_score(y, y_pred)*100)
print("Precision:",metrics.precision_score(y, y_pred))
print("Recall:",metrics.recall_score(y, y_pred))
print("f1 score: ", metrics.f1_score(y, y_pred))
print("ROC AUC score: ", metrics.roc_auc_score(y, y_pred))



#%%

# changing parameter
ridge = Ridge(fit_intercept=True,normalize=True,tol=1e-4)

ridge.fit(X,y)

# Prediction Value..
y_pred=ridge.predict(X)   #Prediction for X..here X is from Train Dataset...

#y_pred Value
print(y_pred)

y_pred = classDetect(y_pred)

# Result Checking...

from sklearn import metrics
print("Confussion Matrix: ", metrics.confusion_matrix(y, y_pred))   #y = Actual value
print("Accuracy:",metrics.accuracy_score(y, y_pred)*100)
print("Precision:",metrics.precision_score(y, y_pred))
print("Recall:",metrics.recall_score(y, y_pred))
print("f1 score: ", metrics.f1_score(y, y_pred))
print("ROC AUC score: ", metrics.roc_auc_score(y, y_pred))


#%%

# Now for the Test Dataset
# Prediction Value..

y_pred_test=ridge.predict(test_data)   #Prediction for X..here X is from Test Dataset...


#ridge prediction value
print(y_pred_test)

# calculating the sigmoid value and based on this value make them into cass
y_pred_test = classDetect(y_pred_test)

#%%

# Data Storing into Csv File
submission['target'] = y_pred_test
submission.to_csv('Sample Submission For Model 4.csv',index=False)


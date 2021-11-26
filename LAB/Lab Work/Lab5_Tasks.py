#%%
import pandas as pd
import lab5_module as lab

df = pd.read_csv('dataset.csv')

#%%
#Task 1

print("Number of Rows: ", df.shape[0])
print("Number of Columns: ", df.shape[1])

#%%
#Task 2

print(df[['Time', 'Amount']].describe())

#%%
#Task 3

print("Mean of Time", df['Time'].mean())
print("Median of V1",df['V1'].median())
print("Std Deviation of V2",df['V2'].std())
print("Variance of V3",df['V3'].var())

#%%
#Task 4
print("Mean using Pandas: ", df['Time'].mean())

series1 = df['Time']
print("Mean using module: ", lab.mean(series1))

#%%
#Task 5

df_TA = df[["Time", "Amount"]]

df_TA.hist(column = ['Time', 'Amount'], bins = 50)

#%%
#Task 6
class0 = len(df[df['Class']==0])*100
class1 = len(df[df['Class']==1])*100

print("Percentage of 0 :",class0/len(df['Class']))
print("Percentage of 1 :",class1/len(df['Class']))

#%%
#Task 7

df["Class"].value_counts().plot(kind = 'bar')

#%%
#Task 8

df.hist(column = ["V1", "V2", "V3", "V4"], bins = 50)


#%%
#Task 9

print(df["Amount"].corr(df['Time']))
print(df["Amount"].corr(df['Class']))

print(df["Class"].corr(df['Time']))
print(df["Class"].corr(df['V11']))


#%%
#Task 10

df.boxplot(column = ['Amount', 'Time'])

df.boxplot(column = ['Amount', 'Class'])

df.boxplot(column = ['Class', 'Time'])

df.boxplot(column = ['Class', 'V11'])

#%%
#Task 11

df.plot.scatter(x = "Amount", y= "Time")
df.plot.scatter(x = "Amount", y= "Class")
df.plot.scatter(x = "Class", y= "Time")
df.plot.scatter(x = "Class", y= "V11")

#%%
#Task 12

print(df["Amount"].corr(df['V1']))
print(df["Amount"].corr(df['V4']))

print(df["Class"].corr(df['V1']))
print(df["Class"].corr(df['V4']))

#%%
#Task 13
df.boxplot(column = ['Amount', 'V1'])

df.boxplot(column = ['Amount', 'V4'])

df.boxplot(column = ['Class', 'V1'])

df.boxplot(column = ['Class', 'V4'])

#%%
#Task 14
df.plot.scatter(x = "Amount", y= "V1")
df.plot.scatter(x = "Amount", y= "V4")
df.plot.scatter(x = "Class", y= "V1")
df.plot.scatter(x = "Class", y= "V4")
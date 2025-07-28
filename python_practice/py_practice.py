import pandas as pd
import csv
import os
import statistics 
import re
import sys
import random
import seaborn as sns
import matplotlib as plt
import matplotlib.animation as animation


grades = pd.Series([87,100,94])
print(grades)

# new = pd.Series(98.6, range(3))
# print(new)
# print(grades[0])

# print(grades.describe())

# grades = pd.Series([87, 100, 94], index=['Wally', 'Eva', 'Sam'])

# print(grades)

# grades = pd.Series({'Wally': 87, 'Eva': 100, 'Sam': 94})
# print(grades)

# print(grades['Eva'])

# hardware = pd.Series(['Hammer', 'Saw', 'Wrench'])
# hardware.str.contain('a')
# hardware.str.upper()


grades_dict = {'Wally': [87,96,70], 'Eva': [100,87,90], 'Sam': [94,77,90], 'Katie': [100, 81, 82]}
grades = pd.DataFrame(grades_dict, index = ['Test1', 'Test2', 'Test3'])
print(grades)

# Another way to add indexes grades.index = ['Quiz1', 'Quiz2', 'Quiz3']

print(grades)

#use the column names as attributes
print("Eva's Grades:")
print(grades.Eva)


#access a dataframe by its label
grades.loc['Test1']

#accessed with 8-based indices
grades.iloc[1]
grades.loc['Test1':'Test3']

print(grades.loc[['Test1', 'Test2']])

#get just Eva and Katie's grades on Test1 and Test2
eva_katie = grades.loc['Test1':'Test2', ['Eva', 'Katie']]
print(eva_katie)

a_grades = grades[grades >= 90]
b_grades = grades[(grades >= 80) & (grades < 90)]
print(b_grades)

#use .at and iat to get specific values
eva_test2 = grades.at['Test2', 'Eva']
grades.iat[2,0]

#assign new values
grades.at['Test2', 'Eva'] = 100
grades.iat[1,2] = 87

#setting precision of the describe
print(grades.describe())

#transpose grades
print(grades.T)

print(grades.T.describe())

sg = grades.sort_index(ascending=False)
print(sg)

sgt = grades.T.sort_values(by='Test1', ascending=False)

sgt = grades.loc['Test1'].T.sort_values(ascending=False, inplace=True)
print(sgt)
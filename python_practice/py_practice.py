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


# grades = pd.Series([87,100,94])
# print(grades)

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


# grades_dict = {'Wally': [87,96,70], 'Eva': [100,87,90], 'Sam': [94,77,90], 'Katie': [100, 81, 82]}
# grades = pd.DataFrame(grades_dict, index = ['Test1', 'Test2', 'Test3'])
# print(grades)

# # Another way to add indexes grades.index = ['Quiz1', 'Quiz2', 'Quiz3']

# print(grades)

# #use the column names as attributes
# print("Eva's Grades:")
# print(grades.Eva)


# #access a dataframe by its label
# grades.loc['Test1']

# #accessed with 8-based indices
# grades.iloc[1]
# grades.loc['Test1':'Test3']

# print(grades.loc[['Test1', 'Test2']])

# #get just Eva and Katie's grades on Test1 and Test2
# eva_katie = grades.loc['Test1':'Test2', ['Eva', 'Katie']]
# print(eva_katie)

# a_grades = grades[grades >= 90]
# b_grades = grades[(grades >= 80) & (grades < 90)]
# print(b_grades)

# #use .at and iat to get specific values
# eva_test2 = grades.at['Test2', 'Eva']
# grades.iat[2,0]

# #assign new values
# grades.at['Test2', 'Eva'] = 100
# grades.iat[1,2] = 87

# #setting precision of the describe
# print(grades.describe())

# #transpose grades
# print(grades.T)

# print(grades.T.describe())

# sg = grades.sort_index(ascending=False)
# print(sg)

# sgt = grades.T.sort_values(by='Test1', ascending=False)

# sgt = grades.loc['Test1'].T.sort_values(ascending=False, inplace=True)
# print(sgt)

#Chapter 8.2 Formatting strings

# #string formats with floats
# float = f'{17.49:.2f}'
# print(float)

# floatingType = f'{10:d}'

# alignment = f'{27:<15d}'
# align2 = f'[{3.5:<15f}]'

# '{:.2f}'.format(17.489)
# '{}{}'.format('Amanda', 'Cyan')
# '{0}{0}{1}'.format('Happy', 'Birthday')

# s1 = "happy"
# s2 = "birthday"

# can = s1 + ' ' + s2
# print(can)

# sent = '\t \n This is a test string. \t\t \n'
# print(sent.strip())

# title_it = 'strings: a deeper look'.title()
# cap_it = 'strings: a deeper look'.capitalize()

# sentence = "to be or not to be that is the question"
# sentence.count('to')

# #specify a splice string[start_index:end_index] through to end of string:
# sentence.count('to', 12,25)


# #searches for a substring within a string and returns the first index at which substring is found
# sentence.index('be')

# #search from end of the string
# sentence.rindex('be')

# #also find and rfind
# sentence.find('be')
# reverse_it = sentence.rfind('to')

# #can replace substrings
# values = '1\t2\t3\t4\t5'
# t_no = values.replace('\t', ',')
# print(t_no)

# #can do splits and specify the maximum number of splits
# letters = 'A,B,C,D'
# split_it = letters.split(',', 2)

# say = ['I', 'Love', 'Rock', "n'", 'Roll']
# say2 = (' ').join(say)
# print(say2)

# #splits into a tuple based on separator
# amanda_grades = 'Amanda: 89, 79, 90'
# print(amanda_grades.partition(':'))

# url = 'http://www.deitel.com/books/PyCDS/table_of_contents.html'
# rest_of_url, separator, document = url.rpartition('/')
# print(document)
# print(rest_of_url)


# #verify .isdigit()
# '27'.isdigit()

# #Use r to treat escape characters as nomraml

# file_path = r'C:\Root\Sub\File'


pattern = '02215'
print('Match') if re.fullmatch(pattern, '02215') else print('No Match')

# \d represents digits 0-9, 5 is the quantifier
print('Valid') if re.fullmatch(r'\d{5}', '02215') else print('Invalid')


#[aieo] matches lowercase vowels
#[a-z] matches any letter lowercase
#[A-Z] matches any lettr uppercase
'Valid' if re.fullmatch('[A-Z][a-z]*', 'Wally') else 'None'


#search looks for first occurrence of substring and retuns

result = re.search("Python", 'Python is fun')

result.group() if result else 'not found'

contact = 'Wally White Home: 555-129-3344, Work: 333-222-3333'

please = re.findall(r'\d{3}-\d{3}-\d{4}', contact)
print(please)


#finditer retursn one match at a time

for phone in re.finditer(r'\d{3}-\d{3}-\d{4}', contact):
    print(phone.group())

#Optional flags for case sensitivity

result3 = re.search('Sam', 'SAM WHITE', flags=re.IGNORECASE)

print(result3.group() if result3 else 'not found')

#^ matches only the beginning $ matches only the ends

result = re.search('Python$', 'Python is fun')


entry = 'Charlie Cyan, e-mail: demo1@deitel.com'
pattern = r'([A-Z][a-z]+ [A-Z][a-z]+), e-mail: (\w+@\w+\.\w{3})'
result4 = re.search(pattern, entry)
print(result4)

#prints touples
print(f'Name: {result4.group(1)}')
print(f'Email: {result4.group(2)}')

# Both * and + match as many characters as possible and will match 'Al', 'Eva', 

print('Valid' if re.fullmatch('[A-Z][a-z]+', 'Wally') else 'Invalid')
print('Valid' if re.fullmatch('[A-Z][a-z]+', 'E') else 'Invalid')
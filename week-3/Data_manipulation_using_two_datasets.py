# -*- coding: utf-8 -*-
"""Week3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bIifiytTQOpJDSjApll99puwufJfJ4G5
"""

# Importing Libraries

import pandas as pd
import numpy as np

"""### Read the file

"""

data=pd.read_csv("/Data-cleaning-for-beginners-using-pandas (2).csv")

from google.colab import drive
drive.mount('/content/drive')

# Display the first five rows of the data

data.head()

# Using conditional statements split the column location to location and symbol

data['Location'] = data['Location'].str.strip()  # Remove leading and trailing spaces

def splitting(val):
  if ',' in val and ' ' in val:
    return val.split(',')
  elif ' ' in val and ',' not in val:
    return val.split(' ')
  elif ',' in val and ' ' not in val:
    return val.split(',')
data[['Location','Symbol']]=[splitting(x) for x in data['Location']]

# Avoiding inconsistencies in the column names

data.columns=data.columns.str.replace(" ","_")

"""##Let us check NULL values"""

data.isnull().sum()

data.Age.fillna(data.Age.mean(),inplace=True)

data.Rating.fillna(data.Rating.mean(),inplace=True)

data.isnull().sum()

# Replacing '-1' with 'False' and converting the column ini=to 'Boolean'

data.columns
data['Easy_Apply']=data['Easy_Apply'].replace("-1","False")
data['Easy_Apply']=data['Easy_Apply'].replace("TRUE","True")
def true_false(val):
  if val.lower()=='false':
    return False
  else:
    return True
data['Easy_Apply']=[true_false(x) for x in data['Easy_Apply']]

data.info()

# rounding the age column into one decimal for consistency

data.Age=data.Age.round(decimals=1)

# Finding outliers for the data considering Age, Rating and Salary

q1=data[['Age','Salary','Rating']].quantile(0.25)
q3=data[['Age','Salary','Rating']].quantile(0.75)
IQR=q3-q1
outliers=((data[['Age','Salary','Rating']]<(q1-1.5*IQR)) | (data[['Age','Salary','Rating']]>(q3+1.5*IQR)))
print(data[outliers.any(axis=1)])

# Replacing '$' with empty space and 'k' with '000' for consistency and understanding.

data["Salary"]=data["Salary"].str.replace("$","")
data["Salary"]=data["Salary"].str.replace("k","000")
data.head()

d=',| '
data['Location'] = data['Location'].str.split(d,expand=True)[1]

data['Location']=data['Location'].str.replace("York","Ny")

data['Established']=data['Established'].replace(-1,np.nan)

# As we dont know the established year we cant replace that with a value using cenral tendencies so we will make that '-1' to unknown

data['Established']=data['Established'].replace(np.nan,"Unknown")

#rounding the Rating column upto one decimal.

data.Rating=data.Rating.round(decimals=1)

# Some people gave rating less than zero we will make hem zero by replacing '-1'

data['Rating']=data['Rating'].replace(-1.0,0.0)

# Analyze the information of the data

data.info()

#Observe the analysis and statistics of the data

data.describe()

# SPlit the column Salary into two columns as 'salary_range_start' and 'salary_range_end'

data[["salary_range_start","salary_range_end"]]=data['Salary'].str.split('-',expand=True)

# for consistency and integrity remove the column 'Salary'

del data['Salary']

# To avoid confusion remove the column Index.

del data['Index']

# Finally observe the data.

data.loc[:,['Age','Rating','Location','Symbol','salary_range_start','salary_range_end','Established','Easy_Apply']]

"""#NEW DATA----- chipotle dataset"""

# Read the file

data1=pd.read_csv("/chipotle (1).tsv",sep='\t')

# Display the fisrt 5 rows of the data

data1.head()

# check for null values

data1.isnull().sum()

# Replace '$' symbol in 'item_price with '' and change the data type from string to 'boolean'

data1['item_price']=data1['item_price'].str.replace("$","")

data1['item_price']=data1['item_price'].astype(float)

# Display the information of the table.

data1.info()

# check for duplicates in the data

data1.duplicated().any()

# to know the rows and columns number before dropping duplicates.

data1.shape

#Drop the duplicates from the data

data1=data1.drop_duplicates()

#Reset the index of the data

data1=data1.reset_index(drop=True)

# check the shape of the data

data1.shape

# Observe the statistics of the data

data1.describe()

# replace '[' and ']' with '' for the column 'choice_description'

data1['choice_description']=data1['choice_description'].str.replace('[',"")

data1['choice_description']=data1['choice_description'].str.replace(']',"")

# enter different number of choices to convert the column of lists to rows of choices

data1[['1_choice','2_choice','3_choice','4_choice','5_choice','6_choice','7_choice','8_choice','9_choice','10_choice']]=data1['choice_description'].str.split(',',expand=True)

# To maintain integrity delete the column 'choice_description'.

del data1['choice_description']

data1.info()

# fii the null values with 'None to avoid nan in the data

data1['1_choice']=data1['1_choice'].fillna("None")
data1['2_choice']=data1['2_choice'].fillna("None")
data1['3_choice']=data1['3_choice'].fillna("None")
data1['4_choice']=data1['4_choice'].fillna("None")
data1['5_choice']=data1['5_choice'].fillna("None")
data1['6_choice']=data1['6_choice'].fillna("None")
data1['7_choice']=data1['7_choice'].fillna("None")
data1['8_choice']=data1['8_choice'].fillna("None")
data1['9_choice']=data1['9_choice'].fillna("None")
data1['10_choice']=data1['10_choice'].fillna("None")

# For Understanding place the item_price at the last

data1.loc[:,['order_id','quantity','item_name','1_choice','2_choice','3_choice','4_choice','5_choice','6_choice','7_choice','8_choice','9_choice','10_choice','item_price']]


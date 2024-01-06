# -*- coding: utf-8 -*-
"""Week4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RS6-WCXkiPr51tnsYLK8nxIx2ToA-D2x
"""

# Importing Libraries

import pandas as pd
import numpy as np

# Import the datsets ---- population, fertility and life expectancy

population=pd.read_csv("/content/country_population.csv")
fertility=pd.read_csv("/content/fertility_rate.csv")
life_expectancy=pd.read_csv("/content/life_expectancy.csv")

# drop the column Indicator Code

del population['Indicator Code']

# drop the columns indicator name and country name

population.drop(['Country Name','Indicator Name'],axis =1,inplace=True)

# display the head of the data--- first five rows of the data

population.head()

# check for null values in the data

population.isna().any()

# drop the rows where the values are null

population.dropna(axis=0,inplace=True)

# display the shape of the data

population.shape

# create a years string list to merge the datasets

years=[str(i) for i in range(1960,2016)]

# melt the population dataset where the years 1960, 1961,1962,..........2016 are placed in a single column called 'years'

population=pd.melt(population,id_vars='Country Code',value_vars=years,var_name='Year',value_name='Population')

#display the melted dataset

population.head()

# check if any null values are present

population.isna().any()

# display the head of the second dataset called fertility

fertility.head()

# drop the columns country name, indicator name, indicator code

fertility.drop(['Country Name','Indicator Name','Indicator Code'],axis=1,inplace=True)

# check for null values

fertility.isna().sum()

# drop th eorws consisting null values

fertility.dropna(axis=0,inplace=True)

# display the shape of the dataset

fertility.shape

# melt the dataset all the columns 1960,1961,1962,.......2016 into one column called years

fertility=pd.melt(fertility,id_vars='Country Code',value_vars=years,var_name='Year',value_name='Fertility Rate')

# display first five rows of the dataset

fertility.head()

# display first five rows of the dataset life expectancy

life_expectancy.head()

# drop the columns country name, indicator name, indicator code

life_expectancy.drop(['Country Name','Indicator Name','Indicator Code'],axis=1,inplace=True)

# check for null values

life_expectancy.isna().sum()

# drop the rows having null values

life_expectancy.dropna(axis=0,inplace=True)

# melt the dataset the columns 1960,1961,.......2016 are converted into a single column year

life_expectancy=pd.melt(life_expectancy,id_vars='Country Code',value_vars=years,var_name='Year',value_name='Life Expectancy Rate')

# display first five rows of the dataset

life_expectancy.head()

# load the metadata dataset

region=pd.read_csv("/content/Metadata_Country.csv")

# drop the columns incomegroup,specialnotes,tablename and unnamed: 5

region.drop(['IncomeGroup','SpecialNotes','TableName','Unnamed: 5'],axis=1,inplace=True)

# merge the dataset Region with preprocessed dataset population

data=pd.merge(region,population,how='left',on='Country Code')

# merge the dataset data with preprocessed fertility and population

data1=pd.merge(population,fertility,how='left',on=['Country Code','Year'])

# merge the first merged data with fertility

data=pd.merge(data,fertility,how='left',on=['Country Code','Year'])

# merge the merged dataset of population,region and fertility with life life_expectancy

data=pd.merge(data,life_expectancy,how='left',on=['Country Code','Year'])

data1=pd.merge(data1,life_expectancy,how='left',on=['Country Code','Year'])

# display first five rows of the merger dataset

data.head()

data1.head()

# drop the null values containng rows from the merged dataset

data.dropna(axis=0,inplace=True)

data.head()

# check for null values

data.isna().any()

# import matplotlib library

import matplotlib.pyplot as plt

#group the data with region and year

df = data.groupby(['Region','Year'])['Population'].sum().reset_index()

df

# show the grow of the population along the years---the graph is constantly across years

plt.plot(data1['Year'],data1['Population'])
plt.show()

# mport seaboorn library

import seaborn as sns

# plot a distribution plot for the fertility rate with region

sns.displot(data,x='Fertility Rate',kind='kde',hue='Region')

# group the life expectancy with year

life_expectancy_variation = data.groupby('Year')['Life Expectancy Rate'].mean()


# Plotting the data----variation of life expectancy is shown in the figure
plt.figure(figsize=(10, 6))
plt.plot(life_expectancy_variation.index, life_expectancy_variation.values, marker='o')
plt.title('Life Expectancy Variation Over the Years')
plt.xlabel('Year')
plt.ylabel('Life Expectancy')
plt.grid(True)
plt.show()

# scattr plot for region and fertility

ax=sns.scatterplot(x='Region',y='Fertility Rate',data=data)
ax.set_title("Region vs. Fertility Rate")

# scatter plot for region and life expectancy

ax=sns.scatterplot(x='Region',y='Life Expectancy Rate',data=data)
ax.set_title("Region vs. Life Expectency Rate")

# scatter plot for region and population

ax=sns.scatterplot(x='Region',y='Population',data=data)
ax.set_title("Region vs. Population")

data.head()

# import plotly into the environment

import plotly.express as plt

"""As we can see that normal scatter plots and bar charts are not deciding the variations and difficult to understand. So, we use animations for the clarity."""

# animation bar plot for region and population across different countries over years.

plt.bar(data,
            x='Region',
            y='Population',
            animation_frame="Year",
            animation_group='Country Code',
            color='Region',
            hover_name='Country Code',
        title='Region Vs Population',
            range_y=[0,2500000000])

# Scatter plot for Fertility Rate and Life Expectancy rate for every region for every country over the years

plt.scatter(data,
            x='Fertility Rate',
            y='Life Expectancy Rate',
            animation_frame="Year",
            animation_group='Country Code',
            size='Population',
            hover_name='Country Code',
            color='Region',
            log_x=True,
            size_max=55,
            title='Fertility Rate vs Life Expectancy rate',
            range_x=[1,10],
            range_y=[10,100])

#plot the geographical data for countries with fertility rate

plt.choropleth(data,
                           featureidkey='properties.name',
                           locations='Country Code',
                           color='Fertility Rate',
                           hover_name='Region',
                           animation_frame='Year',
                      animation_group='Country Code',
                          scope='asia',
               title="Fertility rate in Different countries in Asia"
                          )

#plot the geographical data for countries with fertility rate

plt.choropleth(data,
                           featureidkey='properties.name',
                           locations='Country Code',
                           color='Life Expectancy Rate',
                           hover_name='Region',
                           animation_frame='Year',
                      animation_group='Country Code',
                          scope='asia',
               title="Life Expectancy rate in Different countries in Asia"
                          )

# line chart for region and fertility rate.

plt.line(data,
         x='Region',
         y='Fertility Rate',
         title='Region vs Fertility Rate',
         animation_frame='Year',
         animation_group='Region',
         hover_name='Region',
         range_y=[1,10],
         )
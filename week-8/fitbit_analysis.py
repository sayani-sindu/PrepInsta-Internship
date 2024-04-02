# -*- coding: utf-8 -*-
"""FitBit_Analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1n64y912b9G5hjvLZK2fKZ9FWJtGUXt8D
"""

#import libraries--numpy, pandas, matplotlib and seaborn

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

"""#DAILY ACTIVITY DATA"""

#Read the dataset from the drive---daily_activity_merged.csv

Daily_Activity=pd.read_csv("/content/drive/MyDrive/drive-download-20240122T075004Z-001/dailyActivity_merged.csv")

#print the firstt five rows of the data

Daily_Activity.head()

#Check for null values in the daily activity data.
#------------------There are no null values present in the dataset----the data is clean from null values.

Daily_Activity.isnull().sum()

#Check for unique values in the data-----there are 33 different dates in the data----for the analysis.

Daily_Activity['ActivityDate'].unique()

#Determine the datatype and entries in the data---information of the data.

#there are 940 rows and 15 columns in our data------7 float values, 7 int values, 1 object value.

Daily_Activity.info()

# From the information of the data we can see that the 'ActivityDate' is object--convert the column into datetime by using datetime in pandas.

Daily_Activity['ActivityDate']=pd.to_datetime(Daily_Activity['ActivityDate'])

#Information of the Daily activity data

Daily_Activity.info()

#Know the shape of the data----(rows,columns)

Daily_Activity.shape

#Observed that there are multiple columns based on distance----LightActiveDistance, ModeratelyActiveDistance, VeryActiveDistance-----------
#For our analysis we combine them together by adding to form-------'ActiveDistance'.

Daily_Activity['ActiveDistance']=Daily_Activity['LightActiveDistance']+Daily_Activity['ModeratelyActiveDistance']+Daily_Activity['VeryActiveDistance']

#Observed there are multiple columns based on minutes in the data--- FairlyActiveMinutes, LightlyActiveMinutes, VeryActiveMinutes
#For our analysis we combine them together by adding values to form----'ActiveMinutes'

Daily_Activity['ActiveMinutes']=Daily_Activity['FairlyActiveMinutes']+Daily_Activity['LightlyActiveMinutes']+Daily_Activity['VeryActiveMinutes']

#Again check the columns in the data---we can observe there are more two columns that are added to the data.

Daily_Activity.shape

#Delete columns that are used to calculate ActiveDistance--LoggedActivitiesDistance, LightActiveDistance, ModeratelyActiveDistance, VeryActiveDistance

#Delete columns that are used to calculate ActiveMinutes---FairlyActiveMinutes, LightlyActiveMinutes, VeryActiveMinutes

del Daily_Activity['LoggedActivitiesDistance'],Daily_Activity['LightActiveDistance']
del Daily_Activity['ModeratelyActiveDistance'],Daily_Activity['FairlyActiveMinutes']
del Daily_Activity['LightlyActiveMinutes'],Daily_Activity['VeryActiveDistance'],Daily_Activity['VeryActiveMinutes']

#The shape of the dataset---(rows,columns)

Daily_Activity.shape

#Detect the duplicates in the dataset

Daily_Activity.duplicated().any()

#know the information of the dataset---after removing columns

Daily_Activity.info()

#create another dataset as--'grouped_on_Id_Activity'--->By Grouping Ids of the data--->Accessing each Id /person activity or performance and calries noticed on the system.

grouped_on_Id_Activity = Daily_Activity.groupby('Id').agg({
    'TotalSteps': 'sum',
    'TotalDistance': 'sum',
    'TrackerDistance': 'sum',
    'ActiveDistance': 'sum',
    'SedentaryActiveDistance': 'sum',
    'ActiveMinutes': 'sum',
    'SedentaryMinutes': 'sum',
    'Calories': 'sum'
}).reset_index()

#For convenience of the analysis---round all the values upto two decimals


grouped_on_Id_Activity["TrackerDistance"]=grouped_on_Id_Activity["TrackerDistance"].round(2)
grouped_on_Id_Activity["TotalDistance"]=grouped_on_Id_Activity["TotalDistance"].round(2)
grouped_on_Id_Activity["ActiveDistance"]=grouped_on_Id_Activity["ActiveDistance"].round(2)
grouped_on_Id_Activity["ActiveMinutes"]=grouped_on_Id_Activity["ActiveMinutes"].round(2)

from google.colab import drive
drive.mount('/content/drive')

#Review the grouped data

grouped_on_Id_Activity

#Read 'Daily Calories' dataset--->DailyCalories_merged.csv'

Daily_Calories=pd.read_csv("/content/drive/MyDrive/drive-download-20240122T075004Z-001/dailyCalories_merged.csv")

#Dispaly first five rows of the data
Daily_Calories.head()

#Dispaly the information of the dataset--->daily Calories

Daily_Calories.info()

#Convert the datatype of the column--ActivityDay to datetime using pandas

Daily_Calories['ActivityDay']=pd.to_datetime(Daily_Calories['ActivityDay'])

#check whether the data is converted or not

Daily_Calories.info()

#check for null values in the daily calories data

Daily_Calories.isnull().sum()

#display the shape of the dataset---(rows,columns)

Daily_Calories.shape

#Check for duplicates for the data-->There are no uplicates in the data-->FALSE is the output

Daily_Calories.duplicated().any()

#For consistency of the data with 'Daily Activity' lets rename the column 'ActivityDay' to 'ActivityDate'.

Daily_Calories = Daily_Calories.rename(columns={'ActivityDay': 'ActivityDate'})

#Group the dataset and form a datset 'grouped_on_Id_Calories' by grouping 'Id' with sum of 'Calories' in the data.

grouped_on_Id_Calories=Daily_Calories.groupby("Id").agg({'Calories': 'sum'}).reset_index()

#check the grouped dataset

grouped_on_Id_Calories

#Read the dataset named---'Daily Intensities'--->'dailyintensities_merged.csv'

Daily_Intensities=pd.read_csv("/content/drive/MyDrive/drive-download-20240122T075004Z-001/dailyIntensities_merged.csv")
Daily_Intensities.head()

#check for null values in the dataset--->there are no null values in the data

Daily_Intensities.isnull().sum()

#Display the shape of the data-->(rows,columns)

Daily_Intensities.shape

#Display the information of the data

Daily_Intensities.info()

#Convert the datatype of the 'ActivityDay' to datetime from object for consistency in the data

Daily_Intensities['ActivityDay']=pd.to_datetime(Daily_Intensities['ActivityDay'])

#There are multiple columns naming--'FairlyActiveMinutes', 'LightlyActiveMinutes', 'VeryActiveMinutes'-->and merge them to form 'ActiveMinutes'

Daily_Intensities['ActiveMinutes']=Daily_Intensities['FairlyActiveMinutes']+Daily_Intensities['LightlyActiveMinutes']+Daily_Intensities['VeryActiveMinutes']

#There are multiple columns naming---'LightActiveDistance', 'ModeratelyActiveDistance', 'VeryActiveDistance'--->and merge them to form 'ActiveDistance'.

Daily_Intensities['ActiveDistance']=Daily_Intensities['LightActiveDistance']+Daily_Intensities['ModeratelyActiveDistance']+Daily_Intensities['VeryActiveDistance']

#Delete the columns---'LightActiveDistance', 'FairlyActiveMinutes', 'LightlyActiveMinutes',VeryActiveDistance','VeryActiveMinutes','ModeratelyActiveDistance'

del Daily_Intensities['LightActiveDistance'],Daily_Intensities['FairlyActiveMinutes'],Daily_Intensities['LightlyActiveMinutes']
del Daily_Intensities['VeryActiveDistance'],Daily_Intensities['VeryActiveMinutes'],Daily_Intensities['ModeratelyActiveDistance']

#check for the shape of the data--->(rows,columns)-->after deleting the columns

Daily_Intensities.shape

#check for duplicate values in the dataset-->FALSE

Daily_Intensities.duplicated().any()

#Group the intensities dataset--->'grouped_on_Id_Intensities' by grouping 'Id' and aggregating the remaining columns

grouped_on_Id_Intensities=Daily_Intensities.groupby('Id').agg({
    'SedentaryMinutes':'sum',
    'ActiveMinutes' : 'sum',
    'SedentaryActiveDistance' : 'sum',
    'ActiveDistance' : 'sum'
}).reset_index()

#Round the float columns for consistency and easy understanding of the data

grouped_on_Id_Intensities['SedentaryActiveDistance']=grouped_on_Id_Intensities['SedentaryActiveDistance'].round(2)
grouped_on_Id_Intensities['ActiveDistance']=grouped_on_Id_Intensities['ActiveDistance'].round(2)

#check the grouped data

grouped_on_Id_Intensities

#Observe that there are similar columns and values in activity data and intensity data

grouped_on_Id_Activity

#Read the dataset 'dailysteps_merged.csv'

Daily_Steps=pd.read_csv("/content/drive/MyDrive/drive-download-20240122T075004Z-001/dailySteps_merged.csv")

#Read first five columns of the data
Daily_Steps.head()

#check for null values in the data

Daily_Steps.isnull().sum()

#check the infomation of the data--->shape,Datatypes of the data

Daily_Steps.info()

#Convert the datatype of the column 'ActivityDay' to datetime using pandas.

Daily_Steps['ActivityDay']=pd.to_datetime(Daily_Steps['ActivityDay'])

#check the shape of the data-->(rows,columns)

Daily_Steps.shape

#check for he duplicate values in the data

Daily_Steps.duplicated().any()

#Rename the column ActivityDay to ActivityDate.

Daily_Steps=Daily_Steps.rename(columns={'ActivityDay':'ActivityDate'})

#Group the data with 'Id' and aggregating 'StepTotal'

grouped_on_id_Steps=Daily_Steps.groupby('Id').agg({
    'StepTotal' : 'sum'
}).reset_index()

#Display the grouped dataset

grouped_on_id_Steps

#Display the information of the dataset

Daily_Activity.info()

#display the information of the 'DailyCalories' data

Daily_Calories.info()

#merge the Daily Activity and Daily Calories datasets on 'Id' and 'ActivityDate' using inner join concept.

Merged_Daily_Activities = pd.merge(Daily_Activity, Daily_Calories, on=['Id','ActivityDate','Calories'], how='inner')

#Now merge the above dataset with Daily_steps i=on 'Id','ActivityDate' using inner join.

Merged_Daily_Activities=pd.merge(Merged_Daily_Activities,Daily_Steps,on=['Id','ActivityDate'],how='inner')

#Display the information of the data

Merged_Daily_Activities.head()

"""#ANALYSIS OF DAILY ACTIVITY

##Histograms

1.Distribution plots for Total steps,Distance and Calories of the users of Fitbit.

2.There are less number of people with more number of stepa and Total Distance.

3.There are more users with an average number of calories burnt.
"""

# Histogram plot for 'Total Steps'

sns.histplot(data=Merged_Daily_Activities,x="TotalSteps",kde=True)
plt.title("Histogram for total steps for all users")
plt.xlabel("Total Steps")
plt.show()

# Histogram plot for 'Total Distance'

sns.histplot(data=Merged_Daily_Activities,x="TotalDistance",kde=True)
plt.title("Histogram for total distance recorded for all users]")
plt.xlabel("Total Distance")
plt.show()

# Histogram plot for 'Tracker Distance'

sns.histplot(data=Merged_Daily_Activities,x="TrackerDistance",kde=True)
plt.title("Histogram for total distance recorded for all users]")
plt.xlabel("Tracker Distance")
plt.show()

# Histogram plot for 'Calories'

sns.histplot(data=Merged_Daily_Activities,x="Calories",kde=True)
plt.title("Histogram for total calories burnt by all users]")
plt.xlabel("Calories")
plt.show()

"""##Box Plots

1.The boxplots for Total Steps and Distance both contain outliers, but the data is generally well-distributed.
"""

#box plot for Active Minutes

sns.boxplot(x=Merged_Daily_Activities["ActiveMinutes"])
plt.title("Statistical Information for Active Minutes")
plt.xlabel("Minutes")

#box plot for Active Distance
sns.boxplot(x=Merged_Daily_Activities["ActiveDistance"])
plt.title("Statistical Information for Active Distance")
plt.xlabel("Distance")

#box plot for Sendentary Active Distance
sns.boxplot(x=Merged_Daily_Activities["SedentaryMinutes"])
plt.title("Statistical Information for Sedentary Minutes")
plt.xlabel("Sedentary Minutes")

#box plot for Total Steps
sns.boxplot(x=Merged_Daily_Activities["StepTotal"])
plt.title("Statistical Information for Total Steps")
plt.xlabel("Total Steps")

"""##HeatMap

1.Total Distance,Total steps and Active minutes are strongly correlated.

2.Calories is strongly corelated with Distance travelled and total steps taken by the user.
"""

Merged_Daily_Activities.columns

correlation_data=Merged_Daily_Activities[['TotalSteps', 'TotalDistance', 'TrackerDistance',
       'SedentaryActiveDistance', 'SedentaryMinutes', 'Calories',
       'ActiveDistance', 'ActiveMinutes', 'StepTotal']]

correlation_data.corr()

sns.heatmap(correlation_data.corr(),annot=True,fmt=".1f",linewidth=.5,cmap="crest")
plt.title("Heat Map for Correlation")

"""##BI VARIATE ANALYSIS

##Scatter Plots

1.We can observe the positive variation between steps taken by the user and calories burnt by the user.

2.The Total Distance travelled by the user and active minutes also affect the calories burnt by the user.
"""

#Scatter plot for Calories and StepTotal

plt.figure(figsize=(26,8))
sns.scatterplot(Merged_Daily_Activities,x='Calories',y='StepTotal')
plt.title('scatter plot Calories Vs StepTotal')
plt.xlabel('Calories')
plt.ylabel('StepTotal')
plt.xticks(rotation=45)
plt.show()

#Scatter plot for Calories and Active Distance

plt.figure(figsize=(26,8))
sns.scatterplot(Merged_Daily_Activities,x='Calories',y='ActiveDistance')
plt.title('scatter plot Calories Vs Active Distance')
plt.xlabel('Calories')
plt.ylabel('Active Distance')
plt.xticks(rotation=45)
plt.show()

#Scatter plot for Calories and Sendentary Minutes

plt.figure(figsize=(26,8))
sns.scatterplot(Merged_Daily_Activities,x='Calories',y='SedentaryMinutes',hue='ActiveDistance',color='green')
plt.title('scatter plot Calories Vs Sendentary Minutes')
plt.xlabel('Calories')
plt.ylabel('Sendentary Minutes')
plt.xticks(rotation=45)
plt.show()

"""##Bar Plots

1.There are very less number of users with very high amount of calories burnt.

2.Ther are maximum with more Active Minutes.

2.There are maximum people with most distance recorded by the device.
"""

#Bar plot for Id  and Calories
plt.figure(figsize=(26,8))
sns.barplot(grouped_on_Id_Activity, x="Id", y="Calories")
plt.xlabel("Id")
plt.ylabel("Calories")
plt.xticks(rotation=45)
plt.title("Id Vs Calories")

#Bar plot for Id  and Active Minutes
plt.figure(figsize=(26,8))
sns.barplot(grouped_on_Id_Activity, x="Id", y="ActiveMinutes")
plt.xlabel("Id")
plt.ylabel("Active Minutes")
plt.xticks(rotation=45)
plt.title("Id Vs Active Minutes")

#Bar plot for Id  and Active Minutes
plt.figure(figsize=(26,8))
sns.barplot(grouped_on_Id_Activity, x="Id", y="TotalSteps")
plt.xlabel("Id")
plt.ylabel("Total Steps")
plt.xticks(rotation=45)
plt.title("Id Vs Total Steps")

#Bar plot for Id  and Total Distance
plt.figure(figsize=(26,8))
sns.barplot(grouped_on_Id_Activity, x="Id", y="TotalDistance")
plt.xlabel("Id")
plt.ylabel("Total Distance")
plt.xticks(rotation=45)
plt.title("Id Vs Total Distance")

"""#HEART RATE ANALYSIS"""

#read the dataset -->heartrate_seconds_mreged.csv

heart_rate=pd.read_csv("/content/drive/MyDrive/drive-download-20240122T075004Z-001/heartrate_seconds_merged.csv")

#Display first five rows of the dataset

heart_rate.head()

#Display the information of the dataset

heart_rate.info()

#Convert the dattaype of the Time from object to datetime by using pandas.

heart_rate['Time']=pd.to_datetime(heart_rate['Time'])

#Display the information of the data

heart_rate.info()

#Check for the duplicates of the data

heart_rate.duplicated().sum()

#Check for the null values of the data

heart_rate.isnull().sum()

"""##UNIVARIATE ANALYSIS

1.The normal heart rate is between--60-75 per minute, but some users have heart rate more than or less than this rate varying time and date.

2.There are heart rate points that are beyond the statistics[IQR]--->Outliers

3.The distribution of heart rate based on date for all users follows trend.
"""

# Histogram plot for 'Heart Rate'

sns.histplot(data=heart_rate,x="Value",kde=True)
plt.title("Histogram for total heart rate for all users")
plt.xlabel("Heart Rate")
plt.show()

#box plot for Heart Rate

sns.boxplot(x=heart_rate["Value"])
plt.title("Statistical Information for Heart Rate")
plt.xlabel("Heart Rate")

# Histogram plot for 'Heart Rate'

sns.histplot(data=heart_rate,x="Time",kde=True)
plt.title("Histogram for total heart rate for all users")
plt.xlabel("Heart Rate")
plt.show()

#Rename the column in the Merged dataset of Activities,Steps,Calories and intensities--->ActivityDate column to Date.

Merged_Daily_Activities.rename(columns={"ActivityDate": "Date"}, inplace=True)

#Rename the column Time in the heart_rate date to Date.

heart_rate.rename(columns={"Time": "Date"}, inplace=True)

#check for the compatibility of the columns with heart_data to merge the data.

Merged_Daily_Activities.info()

#Check for compatibility of the data-->To merge the datasets

heart_rate.info()

#Merge the datasets---'Merged_Daily_Activities', 'heart_rate' on 'Id' and 'Date' using inner jpin.
merged_activities_heart_rate=pd.merge(Merged_Daily_Activities,heart_rate,on=['Id','Date'],how='inner')

#Display first five rows of the data.

merged_activities_heart_rate.head()

#Rename the column Value with Heart rate for consistency in the data

merged_activities_heart_rate.rename(columns={"Value": "Heart Rate"}, inplace=True)

"""###HEAT MAP"""

#The data to be taken to find correlation.

correlation_data=merged_activities_heart_rate[['TotalSteps', 'TotalDistance', 'TrackerDistance',
       'SedentaryActiveDistance', 'SedentaryMinutes', 'Calories',
       'ActiveDistance', 'ActiveMinutes', 'StepTotal','Heart Rate']]

#correlation of the data

correlation_data.corr()

#HeatMap for the merged dataset for heart rate and other columns.

sns.heatmap(correlation_data.corr(),annot=True,fmt=".1f",linewidth=.5,cmap="crest")
plt.title("Heat Map for Correlation")

"""##BIVARIATE ANALYSIS

1.From the analysis, we can observe if calories are inversely proportional to Heart Rate.

2.Heart rate of maximum people is in normal range.
"""

#Scatter plot for Calories and heart rate

plt.figure(figsize=(26,8))
sns.scatterplot(merged_activities_heart_rate,x='Calories',y='Heart Rate')
plt.title('scatter plot Calories Vs Heart Rate')
plt.xlabel('Calories')
plt.ylabel('Heart Rate')
plt.xticks(rotation=45)
plt.show()

#Bar Plot for Id and Heart rate


plt.figure(figsize=(26,8))
sns.barplot(merged_activities_heart_rate,x='Id',y='Heart Rate')
plt.title('Bar plot Id Vs Heart Rate')
plt.xlabel('Id')
plt.ylabel('Heart Rate')
plt.xticks(rotation=45)
plt.show()

"""#SLEEP DATA ANALYSIS

"""

#Read the data-->sleepDay_merged.csv dataset

sleep_data=pd.read_csv("/content/drive/MyDrive/drive-download-20240122T075004Z-001/sleepDay_merged.csv")

#Display the information of the dataset

sleep_data.info()

#Display first five rows of the dataset

sleep_data.head()

#Convert the 'SleepDay' datatype from object to datetime using pandas.

sleep_data['SleepDay']=pd.to_datetime(sleep_data['SleepDay'])

#check for duplicate values in the data

sleep_data.duplicated().sum()

#Drop the duplicates and reset index using 'reset-index' parameter.

sleep_data.drop_duplicates(subset=['Id','SleepDay','TotalSleepRecords','TotalMinutesAsleep','TotalTimeInBed'],
                     keep=False, inplace=True)

#Again check for duplicates

sleep_data.duplicated().sum()

#check for null values in the data

sleep_data.isnull().sum()

#Convert the 'TotalMinutesAsleep' to Datetime format from interger format.

sleep_data['TotalMinutesAsleep'] =pd.to_datetime(sleep_data['TotalMinutesAsleep'], unit='m').dt.strftime('%H:%M')

#Convert the 'TotaltimeBed' to datetime format from integer format.

sleep_data['TotalTimeInBed'] =pd.to_datetime(sleep_data['TotalTimeInBed'], unit='m').dt.strftime('%H:%M')

#sleep_data['TotalMinutesAsleep']=pd.to_timedelta(sleep_data['TotalMinutesAsleep'], unit='min')

#Display first five rows of the data

sleep_data.head()

#Rename the columns SleepDay with Date

sleep_data.rename(columns={'SleepDay':'Date'},inplace=True)

"""##UNIVARIATE ANALYSIS

1.There are less people who slep two times a day.

2.Sleep Distribution of the data varies and follows different trends.
"""

# Histogram plot for 'Total Sleep Records'

sns.histplot(data=sleep_data,x="TotalSleepRecords",kde=True)
plt.title("Histogram for Sleep Record of all users")
plt.xlabel("Sleep Record")
plt.show()

# Histogram plot for 'Sleep Records'
plt.figure(figsize=(26,8))
sns.histplot(data=sleep_data,x="TotalMinutesAsleep",kde=True)
plt.title("Histogram for Total Minutes Sleep by all users")
plt.xlabel("Sleep Record")
plt.xticks(rotation=45)
plt.show()

"""##BIVARIATE ANALYSIS

1.There is a small relation TotalSleepRecords and Calories.
"""

#Scatter plot for Id and TotalSleep Records

plt.figure(figsize=(26,8))
sns.barplot(sleep_data,x='Id',y='TotalSleepRecords')
plt.title('Bar plot Id Vs Total Sleep Records')
plt.xlabel('Id')
plt.ylabel('Total Sleep Records')
plt.xticks(rotation=45)
plt.show()

#Merge the Sleep data with the before merged data sets

merged_activities_heart_rate_sleep=pd.merge(merged_activities_heart_rate,sleep_data,on=['Id','Date'],how='inner')

#Display the first five rows of the data

merged_activities_heart_rate_sleep.head()

#Bar Plot for Id and Total Minutes Sleep

plt.figure(figsize=(26,8))
sns.barplot(merged_activities_heart_rate_sleep,x='Calories',y='TotalMinutesAsleep')
plt.title('Bar plot Id Vs Total Minutes Sleep')
plt.xlabel('Calories')
plt.ylabel('Total Minutes Sleep')
plt.xticks(rotation=45)
plt.show()

"""#WEIGHT LOG ANALYSIS"""

#read the Weight data--->weightLogInfo_Merged.csv

weight_data=pd.read_csv("/content/drive/MyDrive/drive-download-20240122T075004Z-001/weightLogInfo_merged.csv")

#Display first five rows of the data

weight_data.head()

#Dispaly the information of the dataset

weight_data.info()

#Convert the Date column from object to datetime format using pandas

weight_data['Date']=pd.to_datetime(weight_data['Date'])

#check for null values in the data

weight_data.isnull().sum()

#There are only two non-null values in 'Fat' column--->So,Delete the column Fat

del weight_data['Fat']

#Check for the duplicates in the data

weight_data.duplicated().sum()

#Display the first five rows of the data

weight_data.head()

#Round the float values in the data to 2 decimal places for consistency

weight_data['WeightKg'] = weight_data['WeightKg'].round(2)
weight_data['BMI'] = weight_data['BMI'].round(2)
weight_data['WeightPounds'] = weight_data['WeightPounds'].round(2)

#Display first five rows in the data

weight_data.head()

"""##UNI VARIATE ANALYSIS

###HISTOGRAMS
"""

# Histogram plot for 'Weight in KG'

sns.histplot(data=weight_data,x="WeightKg",kde=True)
plt.title("Histogram for Weight Distribution")
plt.xlabel("Weights")
plt.show()

# Histogram plot for 'Weight in Pounds'

sns.histplot(data=weight_data,x="WeightPounds",kde=True)
plt.title("Histogram for Weight Distribution")
plt.xlabel("Weights")
plt.show()

# Histogram plot for 'Weight in Pounds'

sns.histplot(data=weight_data,x="WeightPounds",kde=True)
plt.title("Histogram for Weight Distribution")
plt.xlabel("Weights")
plt.show()

"""###BOX PLOTS"""

# Histogram plot for 'BMI'

sns.boxplot(data=weight_data,x="BMI")
plt.title("Histogram for BMI Distribution")
plt.xlabel("BMI")
plt.show()

# Histogram plot for 'Weight in Kg'

sns.boxplot(data=weight_data,x="WeightKg")
plt.title("Histogram for Weight Distribution")
plt.xlabel("Weights")
plt.show()

# Histogram plot for 'Weight in Kg'

sns.boxplot(data=weight_data,x="BMI")
plt.title("Histogram for BMI Distribution")
plt.xlabel("BMI")
plt.show()

"""##BI VARIATE ANALYSIS"""

#Display the Id and weight relation using Bar Plot

plt.figure(figsize=(26,8))
sns.barplot(weight_data, x="Id", y="WeightKg")
plt.title("Id vs Weight in kg")
plt.xlabel("Id")
plt.ylabel("Weight in kg")


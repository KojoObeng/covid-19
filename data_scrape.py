# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 19:24:37 2020

@author: Jason
"""
import os
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

os.chdir('C:\\Users\\User\\Documents\\School\\code\\COVID-19\\covid-19')

url = 'https://data.ontario.ca/dataset/f4112442-bdc8-45d2-be3c-12efae72fb27/resource/455fd63b-603d-4608-8216-7d8647f43350/download/conposcovidloc.csv'

r = requests.get(url)
with open('confirmed_cases_ontario.csv', 'wb') as f:
    f.write(r.content) 


df = pd.read_csv('confirmed_cases_ontario.csv')

df.info()

sns.countplot(df['Client_Gender'],palette='coolwarm')
sns.countplot(df['Age_Group'],palette='coolwarm')
sns.countplot(df['Outcome1'],palette='coolwarm')
sns.countplot(df['Reporting_PHU_City'],palette='coolwarm')
plt.xticks(rotation=90)

df['Virus'] = 1

df.groupby(['Test_Reported_Date']).count()

dff.plot()

dff = df.groupby(['Test_Reported_Date'])['Virus'].count()
dff.set_index('Test_Reported_Date', inplace=True)

plt.plot(dff)

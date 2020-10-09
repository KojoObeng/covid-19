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

links = ['https://data.ontario.ca/dataset/f4f86e54-872d-43f8-8a86-3892fd3cb5e6/resource/ed270bb8-340b-41f9-a7c6-e8ef587e6d11/download/covidtesting.csv',
         'https://data.ontario.ca/dataset/f4112442-bdc8-45d2-be3c-12efae72fb27/resource/455fd63b-603d-4608-8216-7d8647f43350/download/conposcovidloc.csv']


def get_csv(links):
    for link in links:
        r = requests.get(link)
        with open(str(link).split('/')[8]), 'wb') as f:
            f.write(r.content)

if __name__ == '__main__':
    get_csv(links)

'''
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
'''

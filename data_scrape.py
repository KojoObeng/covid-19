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

links = ['https://data.ontario.ca/dataset/f4112442-bdc8-45d2-be3c-12efae72fb27/resource/455fd63b-603d-4608-8216-7d8647f43350/download/conposcovidloc.csv',
         'https://data.ontario.ca/dataset/f4f86e54-872d-43f8-8a86-3892fd3cb5e6/resource/ed270bb8-340b-41f9-a7c6-e8ef587e6d11/download/covidtesting.csv']


def get_csv(links):
    for link in links:
        r = requests.get(link)
        with open(str(link).split('/')[8], 'wb') as f:
            f.write(r.content)

def read_in_csv(links):
    csv=get_csv(links)
    files = []
    for link in links:
        files.append(str(link).split('/')[8])
    df = pd.read_csv(files[0])
    df1 = pd.read_csv(files[1])
    return (df,df1)
    
def plot_graphs(links):
    df, df1 = read_in_csv(links)
    lst = ['Age_Group','Case_AcquisitionInfo','Outcome1','Client_Gender']
    for i in lst:
        ax = pd.pivot_table(df, index='Accurate_Episode_Date', values='Row_ID', columns=i, aggfunc='count').plot.bar(stacked=True,figsize=(14,8))
        every_nth=30
        for n, label in enumerate(ax.xaxis.get_ticklabels()):
            if n % every_nth != 0:
                label.set_visible(False)
        plt.xticks(rotation=45)
        plt.xlabel('Date')
        plt.ylabel('Count')
        plt.tight_layout()
        plt.show()

if __name__ == '__main__':
    plot_graphs(links)



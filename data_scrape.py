# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 19:24:37 2020

@author: Jason
"""
import os
import requests
import pandas as pd
<<<<<<< HEAD
from pandas.plotting import autocorrelation_plot
from statsmodels.graphics.tsaplots import plot_pacf, plot_acf
from statsmodels.tsa.arima_model import ARIMA
=======
from matplotlib.dates import DateFormatter
>>>>>>> a42f81e9550d072f952e7a18ff2100c3299035cd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta
import seaborn as sns
from sklearn.metrics import mean_squared_error

links = ['https://data.ontario.ca/dataset/f4f86e54-872d-43f8-8a86-3892fd3cb5e6/resource/ed270bb8-340b-41f9-a7c6-e8ef587e6d11/download/covidtesting.csv',
         'https://data.ontario.ca/dataset/f4112442-bdc8-45d2-be3c-12efae72fb27/resource/455fd63b-603d-4608-8216-7d8647f43350/download/conposcovidloc.csv']


def get_csv(links):
    for link in links:
        r = requests.get(link)
        with open((str(link).split('/')[8]), 'wb') as f:
            f.write(r.content)
# os.chdir('C:\\Users\\User\\Documents\\School\\code\\COVID-19\\covid-19')

# url = 'https://data.ontario.ca/dataset/f4112442-bdc8-45d2-be3c-12efae72fb27/resource/455fd63b-603d-4608-8216-7d8647f43350/download/conposcovidloc.csv'

# r = requests.get(url)
# with open('confirmed_cases_ontario.csv', 'wb') as f:
#     f.write(r.content)


months = mdates.MonthLocator()

df = pd.read_csv('confirmed_cases_ontario.csv')
dff = df.groupby(['Test_Reported_Date'])['Test_Reported_Date'].count()

X = dff.values
size = int(len(X) * 0.66)
train, test = X[0:size], X[size:len(X)]
history = [x for x in train]
predictions = list()

for t in range(len(test)):
	model = ARIMA(history, order=(3,0,0))
	model_fit = model.fit(disp=0)
	output = model_fit.forecast()
	yhat = output[0]
	predictions.append(yhat)
	obs = test[t]
	history.append(obs)
	print('predicted=%f, expected=%f' % (yhat, obs))


# residuals = pd.DataFrame(model_fit.resid)
# residuals.plot()
# residuals.plot(kind='kde')
# plt.show()


#plt.show()
#residuals.describe()


# plot_acf(dff, lags = 50)            
# plot_pacf(dff)
# Shows lags 1 and 2 are significant




if __name__ == '__main__':
    get_csv(links)

'''


series = df.groupby(['Case_Reported_Date'])['Case_Reported_Date'].count()

date_form = DateFormatter("%mmmm-%dd")
plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
plt.plot(series)
plt.show()


# df.info()

# sns.countplot(df['Client_Gender'], palette='coolwarm')

# sns.countplot(df['Age_Group'], palette='coolwarm')
# sns.countplot(df['Outcome1'], palette='coolwarm')
# sns.countplot(df['Reporting_PHU_City'], palette='coolwarm')
# plt.xticks(rotation=90)

# df['Virus'] = 1


# df.plot()

# df = df.groupby(['Test_Reported_Date'])['Virus'].count()
# df.set_index('Test_Reported_Date', inplace=True)

plt.plot(dff)
'''

from sklearn.metrics import mean_squared_error
import seaborn as sns
from datetime import datetime, timedelta
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_pacf, plot_acf
from pandas.plotting import autocorrelation_plot
import os
import requests
import pandas as pd

<<<<<<< HEAD
# Settings
# os.chdir('C:\\Users\\User\\Documents\\School\\code\\COVID-19\\covid-19')
os.chdir('C:\\Users\\Kwadw\\OneDrive\\Documents\\Grind\\Projects\\\Python Projects\\Covid-19\\covid-19')


links = ['https://data.ontario.ca/dataset/f4112442-bdc8-45d2-be3c-12efae72fb27/resource/455fd63b-603d-4608-8216-7d8647f43350/download/conposcovidloc.csv',
         'https://data.ontario.ca/dataset/f4f86e54-872d-43f8-8a86-3892fd3cb5e6/resource/ed270bb8-340b-41f9-a7c6-e8ef587e6d11/download/covidtesting.csv',
         'https://data.ontario.ca/dataset/f4112442-bdc8-45d2-be3c-12efae72fb27/resource/455fd63b-603d-4608-8216-7d8647f43350/download/conposcovidloc.csv']
=======
os.chdir('C:\\Users\\User\\Documents\\School\\code\\COVID-19\\covid-19')

links = ['https://data.ontario.ca/dataset/f4112442-bdc8-45d2-be3c-12efae72fb27/resource/455fd63b-603d-4608-8216-7d8647f43350/download/conposcovidloc.csv',
         'https://data.ontario.ca/dataset/f4f86e54-872d-43f8-8a86-3892fd3cb5e6/resource/ed270bb8-340b-41f9-a7c6-e8ef587e6d11/download/covidtesting.csv']
>>>>>>> a48c4e63678361bea4a5d0fb0d278bde190a88ca


# Download CSV
def get_csv(links):

    for link in links:
        r = requests.get(link)
<<<<<<< HEAD
        with open((str(link).split('/')[8]), 'wb') as f:
            f.write(r.content)


def create_model():
    months = mdates.MonthLocator()

    df = pd.read_csv('confirmed_cases_ontario.csv')
    dff = df.groupby(['Test_Reported_Date'])['Test_Reported_Date'].count()

    X = dff.values
    size = int(len(X) * 0.66)
    train, test = X[0:size], X[size:len(X)]
    history = [x for x in train]
    predictions = []

    for t in range(len(test)):
        model = ARIMA(history, order=(4, 0, 0))
        yhat = model.fit().forecast()[0]
        predictions.append(yhat)
        obs = test[t]
        history.append(obs)

        # print('predicted=%f, expected=%f' % (yhat, obs))
    difference = []
    for i in range(0, len(predictions)):
        difference.append((predictions[i] - history[-(len(test))])**2)
    mse = sum(difference)/len(difference)
    print('MSE:', mse)

    # evaluate combinations of p, d and q values for an ARIMA model

    def evaluate_models(dataset, p_values, d_values, q_values):
        dataset = dataset.astype('float32')
        best_score, best_cfg = float("inf"), None
        for p in p_values:
            for d in d_values:
                for q in q_values:
                    order = (p, d, q)
                    try:
                        model = ARIMA(history, order=order)
                        model_fit = model.fit().mle_retvals()
                        print(model_fit)
                        # mse = evaluate_arima_model(dataset, order)
                        # if mse < best_score:
                        #     best_score, best_cfg = mse, order
                        # print('ARIMA%s MSE=%.3f' % (order, mse))
                    except:
                        continue
        print('Best ARIMA%s MSE=%.3f' % (best_cfg, best_score))

    p_values = range(0, 15)
    d_values = range(0, 15)
    q_values = range(0, 15)

    evaluate_models(X, p_values, d_values, q_values)

    def plot_acfs():
        # Residuals
        model = ARIMA(history, order=(3, 0, 0))
        residuals = pd.DataFrame(model.fit().resid)
        residuals.plot(kind='kde')
        residuals.describe()
        plt.show()

        plot_acf(dff, lags=50)
        plot_pacf(dff)
        plt.show()
        # Shows lags 1 and 2 are significant

    # plot_acfs()


def read_in_csv(links):
    csv = get_csv(links)
    files = []
    for link in links:
        files.append(str(link).split('/')[8])
    df = pd.read_csv(files[0])
    df1 = pd.read_csv(files[1])
    return (df, df1)


def plot_graphs(links):
    df, df1 = read_in_csv(links)
    lst = ['Age_Group', 'Case_AcquisitionInfo', 'Outcome1', 'Client_Gender']
    for i in lst:
        ax = pd.pivot_table(df, index='Accurate_Episode_Date', values='Row_ID',
                            columns=i, aggfunc='count').plot.bar(stacked=True, figsize=(14, 8))
        every_nth = 30
        for n, label in enumerate(ax.xaxis.get_ticklabels()):
            if n % every_nth != 0:
                label.set_visible(False)
        plt.xticks(rotation=45)
        plt.xlabel('Date')
        plt.ylabel('Count')
        plt.tight_layout()
        plt.show()


if __name__ == '__main__':
    # get_csv(links)
    create_model()
    # read_in_csv(links)
    # plot_graphs(links)
=======
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


>>>>>>> a48c4e63678361bea4a5d0fb0d278bde190a88ca

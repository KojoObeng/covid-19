# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 19:24:37 2020

@author: Jason
"""

import pandas as pd
import requests


url = 'https://data.ontario.ca/dataset/'
data_set = ['status-of-covid-19-cases-in-ontario', 
            'confirmed-positive-cases-of-covid-19-in-ontario']


def fetch_data(url):
    

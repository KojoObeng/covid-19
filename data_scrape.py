# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 19:24:37 2020

@author: Jason
"""
import os
import requests


os.chdir('C:\\Users\\User\\Documents\\School\\code\\COVID-19\\covid-19')

url = 'https://data.ontario.ca/dataset/f4112442-bdc8-45d2-be3c-12efae72fb27/resource/455fd63b-603d-4608-8216-7d8647f43350/download/conposcovidloc.csv'

r = requests.get(url)
with open('confirmed_cases_ontario.csv', 'wb') as f:
    f.write(r.content) 


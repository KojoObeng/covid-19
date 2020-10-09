from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import requests

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# Selenium Settings
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options = Options()
# chrome_options.add_argument("--headless")

browser = webdriver.Chrome('Settings/chromedriver.exe', options=chrome_options)
# enable_download_headless(driver, download_dir)

options = Options()
options.add_experimental_option("prefs", {
    "download.default_directory": "./",
    "savefile.default_directory": "./"
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})

home_url = "https://data.ontario.ca/en/dataset/confirmed-positive-cases-of-covid-19-in-ontario/resource/455fd63b-603d-4608-8216-7d8647f43350?fbclid=IwAR3KDZBIdLyjuNzLdMHNOfEhmDdihGz5vwOCrTek-aoSvfBx8BCJ3HzXEgw"
download_url = "https://data.ontario.ca/dataset/f4112442-bdc8-45d2-be3c-12efae72fb27/resource/455fd63b-603d-4608-8216-7d8647f43350/download/conposcovidloc.csv"
browser.get(download_url)

# browser.get(home_url)
# browser.find_element_by_class_name('btn btn-primary dropdown-toggle').click()

requests.get(download_url)
# browser.quit()


def download_csv():

    r = requests.get(page_url)  # returns a response
    content = r.text
    soup = BeautifulSoup(content, features="html.parser")

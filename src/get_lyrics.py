#!/usr/bin/env python3
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = 'https://utanet.com'

DATA_FILE = 'data.json'

# # setup selenum using docker images for the Selenium Grid Server
# # REF: https://github.com/SeleniumHQ/docker-selenium
# options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# driver = webdriver.Remote(
#     command_executor='http://localhost:4444/wd/hub',
#     desired_capabilities=options.to_capabilities(),
#     options=options,
# )
# try:
#     driver.get(BASE_URL)

#     # wait for xhr request
#     time.sleep(3)

#     kw_input = driver.find_elements_by_css_selector('#search_form input[name="Keyword"]')
#     kw_input.send_keys('嵐')

#     time.sleep(3)
# finally:
#     driver.quit()


with open(DATA_FILE, 'r') as file:
    data = json.load(file)['data']

sample = data[-1]
list_white = sample['listWhite']
list_red = sample['listRed']

for song in list_white:
    artist = song['artist'].replace(' ', '')
    print(artist)

# count = 0
# for d in data:
#     count += len(d['listwhite'])
#     count += len(d['listRed'])
# print(count)
#!/usr/bin/env python3
import json
import re
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BASE_URL = 'https://www.nhk.or.jp/kouhaku/history/history.html'
OUTPUT_PATH = 'data.json'

# The 71st Kohaku was held in 2020.
MAX_COUNT = 71

# setup selenum using docker images for the Selenium Grid Server
# REF: https://github.com/SeleniumHQ/docker-selenium
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    desired_capabilities=options.to_capabilities(),
    options=options,
)

set_lists = {'data': []}

try:
    for i in range(1, MAX_COUNT + 1):
        print('get the set list for the {}st/nd/th kohaku...'.format(i))
        driver.get('{}?count={}'.format(BASE_URL, i))

        # wait for xhr request
        time.sleep(3)

        # parse html content
        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml')

        # get time information
        time_info = soup.find('div', {'id': 'time'}).find('img', {'class': 'year'}).get('alt')
        result = re.search('[0-9]{4}', time_info)

        data = {
            'count': i,
            'year': time_info[result.start():result.end()],
            'listRed': [],
            'listWhite':[],
        }
        # get set list
        for team in ('listRed', 'listWhite'):
            set_list = soup.find('ul', {'id': team})
            for li in set_list.find_all('li'):
                artist = li.find('span', {'class': 'name'}).get_text()
                song = li.find('span', {'class': 'song'}).get_text()
                data[team].append({'artist': artist, 'song': song})

        set_lists['data'].append(data)
finally:
    driver.quit()

print('output to {}...'.format(OUTPUT_PATH))
with open(OUTPUT_PATH, mode='wt', encoding='utf-8') as file:
    json.dump(set_lists, file, ensure_ascii=False, indent=2)

print('finish')

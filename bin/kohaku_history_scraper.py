#!/usr/bin/env python3
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BASE_URL = 'https://www.nhk.or.jp/kouhaku/history/history.html'

# The 71st Kohaku was held in 2020.
MAX_COUNT = 71

options = webdriver.ChromeOptions()
options.add_argument('--headless')

driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    desired_capabilities=options.to_capabilities(),
    options=options,
)

driver.get(BASE_URL)

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'lead'))
)

html = driver.page_source
soup = BeautifulSoup(html, 'lxml')
list_red = soup.find('ul', {'id': 'listRed'})
for li in list_red.find_all('li'):
    artist = li.find('span', {'class': 'name'}).get_text()
    song = li.find('span', {'class': 'song'}).get_text()
    print('{}, {}'.format(artist, song))

driver.quit()

# for i in range(MAX_COUNT + 1):
# for i in range(1, 2):
#     res = requests.get(BASE_URL + '?count={}'.format(i))
#     soup = BeautifulSoup(res.text, 'html.parser')
#     print(res.text)
#     descriprion = soup.find('h2', {'id': 'lead'}).get_text()
#     print(descriprion)
#     print()
#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://www.nhk.or.jp/kouhaku/history/history.html'

# The 71st Kohaku was held in 2020.
MAX_COUNT = 71

# for i in range(MAX_COUNT + 1):
for i in range(1, 2):
    res = requests.get(BASE_URL + '?count={}'.format(i))
    soup = BeautifulSoup(res.text, 'html.parser')
    print(res.text)
    descriprion = soup.find('h2', {'id': 'lead'}).get_text()
    print(descriprion)
    print()
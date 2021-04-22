#!/usr/bin/env python3
import json

DATA_FILE = 'data.json'

with open(DATA_FILE, 'r') as file:
    data = json.load(file)['data']

print(data[0].keys())

#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests

url = "https://www.biqukan.com/0_790/"
req = requests.get(url)
bs = BeautifulSoup(req.text,'html.parser')
div = bs.find_all('div', class_='listmain')
# print(div[0])

server = "https://www.biqukan.com"

a_bf = BeautifulSoup(str(div[0]))

a = a_bf.find_all('a')

for each in a:
    print(each.string, server + each.get('href'))
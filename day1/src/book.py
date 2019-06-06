#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from bs4 import BeautifulSoup

import requests


url = "https://www.biqukan.com/0_790/70449712.html"
req = requests.get(url)
# print(req.text)
bs = BeautifulSoup(req.text, 'html.parser')
html = bs.find_all('div', class_='showtxt')
# 过滤结果中的br,等标签
text = html[0].text
# print(text)
noblanktext = text.replace('\xa0'*8, '\n\n')
print(noblanktext)
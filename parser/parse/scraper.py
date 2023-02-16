import xlrd
import requests
from bs4 import BeautifulSoup
import pandas as pd
from xlsxwriter import Workbook

for t in range(100):
    url = f'https://peopletalk.ru/category/news/page/{t}/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find_all('div', class_='h3 article-title font-weight-normal')

    for i in items:
        ps = i.find_all('a')
        for p in ps:
            print(p.get('href'))





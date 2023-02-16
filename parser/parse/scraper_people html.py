# importing the libraries 
from bs4 import BeautifulSoup 
import requests 
import pandas as pd
from xlsxwriter import Workbook
import xlrd


urls =['https://peopletalk.ru/article/novyj-trejler-seriala-uensdej-pro-semejku-addams-kto-sygraet-dyadyu-festera/', 'https://peopletalk.ru/article/megan-foks-rezko-otvetila-na-obvineniya-v-tom-chto-ona-plohaya-mat/', 'https://peopletalk.ru/article/trend-na-makiyazh-imitiruyushhij-poboi-vyzval-volnu-kritiki-v-seti/']

for i in urls:
    url=i
    html_content = requests.get(url).text

    soup = BeautifulSoup(html_content, "html5lib")

    divs = soup.find_all('div')
    for div in divs:
        ps = div.find_all('p')
        for p in ps:
            print(p.get_text()) 

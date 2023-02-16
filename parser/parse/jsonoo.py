
import requests
from bs4 import BeautifulSoup
import sys 
import pandas as pd
from xlsxwriter import Workbook
import xlrd
import re
import json




urls = ['https://peopletalk.ru/article/emili-ratakovski-publichno-podderzhala-ember-herd/',
    'https://peopletalk.ru/article/plany-na-vyhodnye-3-4-sentyabrya-vecherinka-rovesnik-h-sign-breakfast-weekend-v-folk-i-vystavka-sacred-theory-v-leveldva/',
'https://peopletalk.ru/article/ya-ne-opravdala-ego-ozhidanij-kak-mat-britni-spirs-otreagirovala-na-obvineniya-detej/',
'https://peopletalk.ru/article/na-aleka-bolduina-podali-v-sud-s-aktera-trebuyut-25-mln/',
'https://peopletalk.ru/article/emili-ratakovski-publichno-podderzhala-ember-herd/',
'https://peopletalk.ru/article/hanna-i-pashu-stanut-roditelyami-vo-vtoroj-raz/',
'https://peopletalk.ru/article/lili-dzhejms-snova-ne-uznat-aktrisa-kardinalno-smenila-obraz-radi-novoj-roli/']


tables, reds = [], []
for url in urls:
    source = requests.get(url)
    html = source.text
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find_all("div", class_="row d-flex justify-content-between top-info")
    urli = url
    texts = soup.find_all('div', class_='col-lg-6 col-xl-7 news-content-inner js__nativeroll-1-5908781 js__buzzoola js__buzzoola-1-5908781 js__nativeroll-2-5908781 js__buzzoola-2-5908781')
    textss = soup.find('div', class_=(re.compile('copy-pegi-wrap-mob'))).get_text()
    for text in textss:
        text = str(soup.find_all('p'))
        h1 = str(soup.find_all('h1'))
        reds.append({'h1': text, 'text': h1})
        print(h1)
#    with open('resulty.json', 'w', encoding='utf-8-sig') as file:
#        json.dump(reds, file)


    
    #table = soup.select('div', ) 
##    table2 = soup.find_all('h1')
##    for u in table2:
##        tables.append(u.get_text)
##       print(f'H1: {u.get_text(strip=False)}')


#    for i in table:
#        c = soup.find_all('p')
#        d = soup.find_all('h1')
#        count=0
#        for r in d:
#            count += 1
#            print(f'h1,{count} {r.get_text(strip=False)}')
#            tables.append(r.get_text)

#        for i in c:
#            reds['i']=i.get_text()
#            print(f'{i.get_text()}')





#    df = pd.DataFrame()
#    df['fg'] = tables
#    df['fg3'] = reds
#    writer = pd.ExcelWriter('./def2678.xls', engine = 'xlsxwriter')
#    df.to_excel(writer, sheet_name='yt', index=False)

#    writer.close()

#            print(f'TEXT{i.get_text()}')
    
        
    
    #        league = soup.find_all("span", class_="c-events__liga")
#            spisok_sta= i.get_text().split('peopletalk.ru. Мы вдохновляем людей через истории звезд. Свидетельство о регистрации СМИ ЭЛ № ФС 77 — 82664На этом сайте мы используем файлы cookies. Продолжая использование сайта,вы даете свое согласие на использование ваших файлов cookies. Подробнее о файлах cookies и обработке ваших данных - в Политике конфиденциальности.')

#            for i in spisok_sta:
#                print(i[1])



#python scraper_mail.py > myoutp.txt
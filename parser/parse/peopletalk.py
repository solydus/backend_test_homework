import requests
from bs4 import BeautifulSoup
import time
from random import randrange
import json


articles_urls_list = []
def get_articles_urls(url):
    url = 'https://peopletalk.ru/category/news/'
    response = requests.get(url)
    with open('index.html', 'w') as file:
        file.write(response.text)
 
    articles_urls_list = []

    for t in range(2): 
        url = f'https://peopletalk.ru/category/news/page/{t}/'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        items = soup.find_all('div', class_='h3 article-title font-weight-normal')

    for i in items:
        ps = i.find_all('a')
        for p in ps:
            articles_urls_list.append(p.get('href'))


    with open('articles_urls_people.txt', 'w') as file:
        for url in articles_urls_list:
            file.write(f'{url}\n')


def get_data(file_path):
    with open(file_path) as file:
        urls_list = [line.strip() for line in file.readlines()]
    result_data = []
    print(result_data)

    for url in (urls_list):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')

        article_h1 = soup.find_all('h1')
        text_content = soup.find_all('div', class_='row justify-content-center mb-5')
        img_articles = soup.find('img', class_='lazy loaded')

        for text in text_content:
            text = soup.find('p').text.strip()
        for h1 in article_h1:
            h1 = soup.find('h1').text.strip()
#        for img in img_articles:
#            img = soup.find('img').get('src')

            print(f'URL:{url}, H1:{h1}, TEXT:{text} \n')

        result_data.append({
                                'url': str(url),
                                'h1': str(h1),
                                'content': str(text),
                                "key": '\n'
#                                'img': str(img)
                                })
        
        with open('resultsss.json', 'w') as file:
            json.dump(result_data, file, ensure_ascii=False)


def main():
    get_articles_urls(url='https://peopletalk.ru/category/news/')
    get_data('articles_urls_people.txt')
if __name__ == '__main__':
    main()
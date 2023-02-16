import requests
from bs4 import BeautifulSoup
import time
from random import randrange
import json



def get_articles_urls(url):
    url = 'https://lifehacker.ru/topics/news/'
    response = requests.get(url)
    with open('index.html', 'w') as file:
        file.write(response.text)
 
    articles_urls_list = []
    for page in range(1, 2):
        url = f'https://lifehacker.ru/topics/news/?page={page}/'
        response = requests.get(url=f'https://lifehacker.ru/topics/news/?page={page}/')
        soup = BeautifulSoup(response.text, 'lxml')

        articles_urls=soup.find_all('a', class_='lh-small-article-card__link')


        for au in articles_urls:
            art_url = au.get('href')
            articles_urls_list.append(f'https://lifehacker.ru{art_url}')


        with open('articles_urls_zvezdi.txt', 'w') as file:
            for url in articles_urls_list:
                file.write(f'{url}\n')
        article_title = soup.find('h1')


def get_data(file_path):
    with open(file_path) as file:
        urls_list = [line.strip() for line in file.readlines()]
    result_data = []

    for url in (urls_list):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')

        article_h1 = soup.find('div', class_='article-card__above-cover').find('h1').text.strip()
        text_content = soup.find('div', class_='single-article__container').find('article').get_text()
        img_articles = soup.find('img', class_='wp-image-6184061 lazy__img')
        print(f'URL:{url}, {article_h1}, {text_content}', {img_articles})


        result_data.append(

            {'url': url,
            'h1': article_h1,
            'content': text_content,
            'img': img_articles
            }
        )
        
    with open('resultss.json', 'w') as file:
        json.dump( result_data, file, ensure_ascii=False)


def main():
    get_articles_urls(url='https://lifehacker.ru/topics/news/')
    get_data('articles_urls_zvezdi.txt')
if __name__ == '__main__':
    main()
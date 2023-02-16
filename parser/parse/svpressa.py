import requests
from bs4 import BeautifulSoup
import time
from random import randrange
import json


articles_urls_list = []
def get_articles_urls(url):
    url = 'https://svpressa.ru/all/news-archive/?page=1'
    response = requests.get(url)
    with open('index.html', 'w') as file:
        file.write(response.text)
 
    articles_urls_list = []
    for page in range(1, 2):
        url = f'https://svpressa.ru/all/news-archive/?page={page}'
        response = requests.get(url=f'https://svpressa.ru/all/news-archive/?page={page}')
        soup = BeautifulSoup(response.text, 'lxml')

        articles_urls=soup.find_all('a', class_='b-article__title b-article__title_item')

        for au in articles_urls:
            art_url = au.get ('href')
            articles_urls_list.append(f'https://svpressa.ru{art_url}')

        

        with open('svpressa_urls.txt', 'w') as file:
            for url in articles_urls_list:
                file.write(f'{url}\n')
        article_title = soup.find('h1')
#        print(f'{article_title}, {url}')

def get_data(file_path):
    with open(file_path) as file:
        urls_list = [line.strip() for line in file.readlines()]
    result_data = []

    for url in (urls_list):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')

        article_h1 = soup.find('h1', class_='b-text__title').text.strip()
        text_content = soup.find('div', class_='b-text__block b-text__block_text b-text__block_offset_large').text.strip().replace('Все материалы по теме', '')
#        img_articles = soup.find('div', class_='material-7days__images_click').find('img').get('src')
        print(f'{url}, {article_h1}, {text_content}')


        result_data.append(

            {'url': url,
            'h1': article_h1,
            'content': text_content
#            'img': f'http:{img_articles}'
            }
        )
        
    with open('results_svpressa.json', 'w') as file:
        json.dump( result_data, file, ensure_ascii=False)


def main():
    get_articles_urls(url='https://svpressa.ru/all/news-archive/')
    get_data('svpressa_urls.txt')
if __name__ == '__main__':
    main()
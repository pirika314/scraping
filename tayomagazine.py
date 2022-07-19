#ライブラリのインポート
from time import sleep

import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://magazine.tayo.jp/page/{}'
max_page_index = 4
d_list = []

for i in range(max_page_index):
    access_url = url.format(i+1)

    sleep(3)
    r = requests.get(access_url)
    r.raise_for_status()

    soup = BeautifulSoup(r.content, 'lxml')
    archives = soup.select("article")

    for archive in archives:
        sleep(3)

        article_name = archive.find('h1', class_='entry-title').text
        article_url = archive.find('a', class_='post-list__link').get('href')
        article_label = archive.find('span', class_='osusume-label').text

        d_list.append({
            'article_name': article_name,
            'article_label': article_label,
            'article_url': article_url
            })

df = pd.DataFrame(d_list)
df.to_csv('tayomagazine_articles.csv', index=None, encoding='utf-8-sig')
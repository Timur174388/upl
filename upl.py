import requests
from bs4 import BeautifulSoup
import sqlite3
# requests, bs4




connection = sqlite3.connect('upl.db')
cursor = connection.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS upl( 
    name TEXT,
    description TEXT,
    time TEXT,
    comments_count TEXT,
    img_link TEXT
 

    );
''')
connection.commit()
base_url = "https://upl.uz"
upl_data = requests.get(base_url).json()

wrapper = soup.find('div', class_='main-story')
articles = wrapper.find_all('div', class_='short-story')

result = []
for article in articles:
    name = article.find('h2', class_='sh-tit').get_text()
    description = article.find('div', class_='sh-pan').get_text(strip=True)
    time = article.find('div', class_='sh-dat').get_text(strip=True)
    if article.find('span', class_='icom'):
        comments_count = article.find('span', class_='icom').get_text(strip=True)
    else:
        comments_count = 0
    img_link = article.find('img')['data-src']

    cursor.executemany('''INSERT INTO upl(name, description, time, comments_count, img_link) 
    VALUES (?,?,?,?,?)
    ''',(name, description, time, comments_count, img_link))
    connection.commit()
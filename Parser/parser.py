import requests
from bs4 import BeautifulSoup
import dateparser

# Загрузка страницы
def get_html(url):
    r = requests.get(url)
    return r.text

# Получение всех ссылок на новости
def get_links(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='main-news-item')
    links = []
    for item in items:
        link = item.find('a').get('href')
        links.append(link)
    return links

# Получение информации о новости
def get_article_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    try:
        title = soup.find('h1', class_='article__title').text.strip()
    except:
        title = ''
    try:
        date = soup.find('span', class_='article__date-time').text.strip()
        date = dateparser.parse(date)
    except:
        date = None
    try:
        content = ''
        blocks = soup.find_all('div', class_='article__body-block')
        for block in blocks:
            content += block.text.strip() + '\n'
    except:
        content = ''
    return (title, date, content)

# Получение информации о всех новостях
def parse_nur():
    url = 'https://www.nur.kz/'
    html = get_html(url)
    links = get_links(html)
    articles = []
    for link in links:
        article_html = get_html(link)
        article_data = get_article_data(article_html)
        articles.append(article_data)
    return articles

# Пример использования
articles = parse_nur()
for article in articles:
    print(article)

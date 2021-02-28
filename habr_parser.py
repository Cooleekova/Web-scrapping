import requests
from bs4 import BeautifulSoup


def get_posts(keys: list):
    response = requests.get('https://habr.com/ru/all/')
    if response.status_code != 200:
        raise Exception('bad response')
    text = response.text

    soup = BeautifulSoup(text, features="html.parser")
    articles = soup.find_all('article', class_='post')

    for article in articles:
        texts = [x.text.strip().lower() for x in article.find_all('div', class_='post__text')]
        for text in texts:
            if any(word in text for word in keys):
                post_date = article.find('span', class_='post__time')
                date = post_date.text.strip()
                title_el = article.find('a', class_='post__title_link')
                title = title_el.text.strip()
                href = title_el['href']
                print(f'Статья опубликована {date}, название: "{title}", ссылка: {href}')

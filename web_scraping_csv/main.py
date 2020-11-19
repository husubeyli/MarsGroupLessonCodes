import requests
from bs4 import BeautifulSoup


response = requests.get('https://apa.az/az/butun-xeberler?page=1')


with open('dayaz.html', 'w') as f:
    f.write(response.text)

soup = BeautifulSoup(response.text, "html.parser" )

parent= soup.findAll("div", {'class': 'news-text'})[0]
news_paragraph = parent.findChildren("p" , recursive=False)

# image, title, published_date, published_time, link, content

print(news_paragraph[0].text)

# print(response.text)

import requests
from bs4 import BeautifulSoup


response = requests.get('https://apa.az/az/butun-xeberler?page=1')


with open('dayaz.html', 'w') as f:
    f.write(response.text)

soup = BeautifulSoup(response.text, "html.parser" )

parent= soup.findAll("div", {'class': 'news-text'})
news_paragraph = parent.findChildren("p" , recursive=False)



print(news_paragraph[0].text)

# print(response.text)

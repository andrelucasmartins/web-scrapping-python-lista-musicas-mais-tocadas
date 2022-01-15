import requests
from bs4 import BeautifulSoup

url = "https://maistocadas.mus.br/pagode-samba/"

headers =  {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}

site = requests.get(url, headers=headers)

soup = BeautifulSoup(site.content, 'html5lib')

videos =  soup.find('div', attrs = {'class': 'lista'}).find('ol')

print(videos.text)
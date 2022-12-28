import requests
from bs4 import BeautifulSoup

review_url = "https://pastebin.com/raw/kU4sqcN5"
resp = requests.get(review_url)
soup = BeautifulSoup(resp.text, 'html.parser')
print(soup)
print(soup.find("pre"))
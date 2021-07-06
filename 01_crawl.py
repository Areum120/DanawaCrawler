import requests
from bs4 import BeautifulSoup
url = 'http://auto.danawa.com/newcar/?Work=record&Tab=Top10&Brand=303&Month=2021-06-00&MonthTo=2021-06-00'
print(url)
headers = {'User-Agent': 'Chrome/74.0.3729.131'}
data = requests.get(url, headers=headers).content
bsobj = BeautifulSoup(data, 'html.parser')

print(bsobj)

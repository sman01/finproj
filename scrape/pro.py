#Python program to scrape website 
#and save quotes from website 
import requests 
from bs4 import BeautifulSoup 
import json

url = "https://www.cardekho.com/maruti/swift"
URL = []
URL.append(url)

for u in URL:
    r = requests.get(u) 
    soup = BeautifulSoup(r.content, 'html5lib') 
    quotes=[] # a list to store quotes 
    table = soup.find('div', attrs = {'class':'rightthings wrongthings'}) 
    for row in table.findAll('li'): 
            quote = {}
            quote['stat']="right"
            quote['pont'] = row.text
            quotes.append(quote)
    tabl = soup.find('div', attrs = {'class':'rightthings wrongthings'}) 
    for ro in tabl.findAll('li'): 
            quote = {}
            quote['stat']="wrong"
            quote['pont'] = ro.text
            quotes.append(quote)
    with open("pro.json", "w") as writeJSON:
        json.dump(quotes, writeJSON, ensure_ascii=False)

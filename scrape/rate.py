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
    table = soup.find('ul', attrs = {'class':'hidden-xs'}) 
    for row in table.findAll('li'): 
            quote = {} 
            quote['category'] = row.div.text
            quote['rating'] = row.span.text
            quotes.append(quote)

    with open('rate.json', 'w', encoding='utf-8') as f:
        json.dump(quotes, f, ensure_ascii=False, indent=4)
print("done")

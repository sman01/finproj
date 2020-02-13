#Python program to scrape website 
#and save quotes from website 
import requests 
from bs4 import BeautifulSoup 
import json

url = "https://auto.ndtv.com/reviews/kia-carnival-mpv-first-drive-review-1878415"
URL = []
URL.append(url)

for u in URL:
    r = requests.get(u) 
    soup = BeautifulSoup(r.content, 'html5lib') 
    quotes=[] # a list to store quotes 
    table = soup.find('div', attrs = {'class':'article__content h__mb40'}) 
    for row in table.findAll('p'): 
            quote = {} 
            quote['review'] = row.text
            quotes.append(quote)
            print (quote)

    with open('pre.json', 'w', encoding='utf-8') as f:
        json.dump(quotes, f, ensure_ascii=False, indent=4)
print("done")

#Python program to scrape website 
#and save quotes from website 
import requests 
from bs4 import BeautifulSoup 
import json
from lxml import html
import requests
url = "https://www.cardekho.com/maruti/swift/user-reviews/"
URL = []
URL.append(url)

for page in range(2,21):
    r = url + str(page)
    URL.append(r)
for u in URL:
    r = requests.get(u) 
    soup = BeautifulSoup(r.content, 'html5lib') 
    quotes=[] # a list to store quotes 
    table = soup.find('ul', attrs = {'class':'reviewList'}) 
    for row in table.findAll('div', attrs = {'class':'contentspace'}): 
            quote = {} 
            quote['title'] = row.h3.text
            quote['review'] = row.p.text
            quotes.append(quote)

        
    with open('scrape.json', 'w', encoding='utf-8') as f:
        json.dump(quotes, f, ensure_ascii=False, indent=4)
print("done")

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

for page in range(2,10):
    r = url + str(page)
    print(r)
    URL.append(r)
print(URL)
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

    with open("textbooks.json", "a") as writeJSON:
        json.dump(quotes, writeJSON, ensure_ascii=False)

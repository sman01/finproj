import time
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

page_url = "https://www.youtube.com/watch?v=utrpyyaUWtg"  

driver = webdriver.Chrome('/Users/shree/OneDrive/Desktop/finproj/chromedriver.exe')
driver.get(page_url)
time.sleep(2)  
title = driver.find_element_by_xpath('//*[@id="container"]/h1/yt-formatted-string').text
print(title)

SCROLL_PAUSE_TIME = 2
CYCLES = 7

html = driver.find_element_by_tag_name('html')
html.send_keys(Keys.PAGE_DOWN)  
html.send_keys(Keys.PAGE_DOWN)  
time.sleep(SCROLL_PAUSE_TIME * 3)
for i in range(CYCLES):
    html.send_keys(Keys.END)
    time.sleep(SCROLL_PAUSE_TIME)
   
comment_elems = driver.find_elements_by_xpath('//*[@id="content-text"]')
all_comments = [elem.text for elem in comment_elems]

with open('ytc.json', 'w', encoding='utf-8') as f:
        json.dump(all_comments, f, ensure_ascii=False, indent=4)
print("all done")

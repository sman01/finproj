# -*- coding: utf-8 -*-
import scrapy
import nltk
from textblob import TextBlob
class CarsSpider(scrapy.Spider):
    name = 'cars'
    allowed_domains = ['https://auto.ndtv.com/reviews/tata-altroz-review-2145527']
    start_urls = ['https://auto.ndtv.com/reviews/tata-altroz-review-2145527/']

    def parse(self, response):
        orders=response.xpath("//div[@class='article__content h__mb40']/p/text()").extract()
        order=" "
#        blob=TextBlob(order)
 #       print(format(blob.sentiment))
       # print (order +"beep")
        with open('analyse.txt', 'w') as f:
            for item in orders:
                f.write("%s\n" % item)

       

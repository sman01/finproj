# -*- coding: utf-8 -*-
import scrapy


class CardeSpider(scrapy.Spider):
    name = 'carde'
    allowed_domains = ['https://www.cardekho.com/user-reviews/maruti-alto-800']
    start_urls = ['https://www.cardekho.com/user-reviews/maruti-alto-800/']

    def parse(self, response):
        orders=response.xpath("//div[@class='contentspace']/p[@class='contentheight']/text()").extract()
        order=" "
        print(orders)
        with open('analyse.txt', 'w') as f:
            for item in orders:
                f.write("%s\n" % item)

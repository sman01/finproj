#!/usr/bin/python
# filename: run.py
import re
from test import Crawler, CrawlerCache

if __name__ == "__main__":
    # Using SQLite as a cache to avoid pulling twice
    crawler = Crawler(CrawlerCache('crawler.db'))
    root_re = re.compile('^/$').match
    crawler.crawl('http://https://www.team-bhp.com//', no_cache=root_re)
#run file change crawler to test

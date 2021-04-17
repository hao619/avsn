import scrapy


class AvsnSpider(scrapy.Spider):
    name = 'avsn'
    allowed_domains = ['javlibrary.com']
    start_urls = ['http://javlibrary.com/']

    def parse(self, response):
        pass

# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class ClothingSpider(scrapy.Spider):
    name = 'clothing'
    allowed_domains = ['www.amazon.com']
    start_urls = ['https://www.amazon.com/s/ref=lp_1040660_ex_n_3?rh=n%3A7141123011%2Cn%3A7147440011%2Cn%3A1040660%2Cn%3A1045024&bbn=1040660&ie=UTF8&lo=fashion']
    
    # Get link for each items and query
    def parse(self,response):
        for item in response.css('div.s-item-container'):
            link = item.css('a.a-link-normal.a-text-normal ::attr(href)').extract()[0]
            print(link)
            scrapy.Request(link, callback=self.parse_item)     

    def parse_item(self, response):
        print("HERE")
        for title in response.css('#productTitle::text').extract():
            print("HERE")
            print(title.strip())
            yield title.strip()
        return;
        # brand
        #response.css('#brand').attrib['href'].split("/")[1]

        # for next_page in response.css('a.next-posts-link'):
        #     yield response.follow(next_page, self.parse)
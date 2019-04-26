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
            yield scrapy.Request(link, callback=self.parse_item)     

    def parse_item(self, response):
        title = response.css('#productTitle::text').extract_first().strip()
        brand = response.css('#brand').attrib['href'].split("/")[1]
        price = response.css('#priceblock_ourprice::text').extract()[0]
        rate = response.css('span.a-icon-alt::text').extract_first().split(" ")[0]
        category = response.xpath("//div[@id='wayfinding-breadcrumbs_feature_div']/ul/li/span[@class='a-list-item']/a/text()").extract()[-1].strip()
        features = [x.strip() for x in response.xpath("//div[@id='feature-bullets']/ul/li/span[@class='a-list-item']/text()").extract()]


# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import csv

class ClothingSpider(scrapy.Spider):
    name = 'clothing'
    allowed_domains = ['www.amazon.com']
    start_urls = ["https://www.amazon.com/Mens-Shirts/b?ie=UTF8&node=2476517011"]
    # with open('../../../category_to_link_men.txt', 'r') as f:
    # 	for row in f:
    # 		print(row)
    # 		start_urls.append(row)
    # with open('../../../category_to_link_men.txt', 'r') as f:
    # 	for row in f:
    # 		print(row)
    # 		start_urls.append(row)
    
    # Get link for each items and query
    def parse(self,response):
        for item in response.css('div.s-item-container'):
            link = item.css('a.a-link-normal.a-text-normal ::attr(href)').extract()[0]
            print(link)
            yield scrapy.Request(link, callback=self.parse_item)

    def parse_item(self, response):
    	# brand = response.css('#brand').attrib['href'].split("/")[1]
    	brand = response.xpath("//div[@id='bylineInfo_feature_div']/div[@class='a-section a-spacing-none']/a/@href").extract()[0].split("/")[1]
    	title = response.css('#productTitle::text').extract_first().strip()
    	price = response.css('#priceblock_ourprice::text').extract()[0]
    	rate = response.css('span.a-icon-alt::text').extract_first().split(" ")[0]
    	category = response.xpath("//div[@id='wayfinding-breadcrumbs_feature_div']/ul/li/span[@class='a-list-item']/a/text()").extract()[-1].strip()
    	features = [x.strip() for x in response.xpath("//div[@id='feature-bullets']/ul/li/span[@class='a-list-item']/text()").extract()]
    	colors = [x.split(" ")[-1] for x in response.xpath("//div[@id='variation_color_name']/ul/li/@title").extract()]
    	with open('items.txt', 'a') as f:
    		f.write(brand+','+title+','+price+','+rate+','+category+','+str(features) + ',' + str(colors) + '\n')
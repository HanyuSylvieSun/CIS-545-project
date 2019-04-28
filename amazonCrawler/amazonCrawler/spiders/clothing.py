# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import csv

class ClothingSpider(scrapy.Spider):
    name = 'clothing'
    allowed_domains = ['www.amazon.com']
    start_urls = []
    with open('men.csv', 'r') as f:
		reader = csv.reader(f)
    	for row in reader:
        	start_urls.append(row.split(",")[1])
    with open('women.csv', 'r') as f:
		reader = csv.reader(f)
    	for row in reader:
        	start_urls.append(row.split(",")[1])
    
    # Get link for each items and query
    def parse(self,response):
        for item in response.css('div.s-item-container'):
            link = item.css('a.a-link-normal.a-text-normal ::attr(href)').extract()[0]
            print(link)
            yield scrapy.Request(link, callback=self.parse_item)     

    def parse_item(self, response):
<<<<<<< HEAD
        title = response.css('#productTitle::text').extract_first().strip()
        brand = response.css('#brand').attrib['href'].split("/")[1]
        price = response.css('#priceblock_ourprice::text').extract()[0]
        rate = response.css('span.a-icon-alt::text').extract_first().split(" ")[0]
        category = response.xpath("//div[@id='wayfinding-breadcrumbs_feature_div']/ul/li/span[@class='a-list-item']/a/text()").extract()[-1].strip()
        features = [x.strip() for x in response.xpath("//div[@id='feature-bullets']/ul/li/span[@class='a-list-item']/text()").extract()]

=======
    	# brand = response.css('#brand').attrib['href'].split("/")[1]
    	brand = response.xpath("//div[@id='bylineInfo_feature_div']/div[@class='a-section a-spacing-none']/a/@href").extract()[0].split("/")[1]
    	title = response.css('#productTitle::text').extract_first().strip()
    	price = response.css('#priceblock_ourprice::text').extract()[0]
    	rate = response.css('span.a-icon-alt::text').extract_first().split(" ")[0]
    	category = response.xpath("//div[@id='wayfinding-breadcrumbs_feature_div']/ul/li/span[@class='a-list-item']/a/text()").extract()[-1].strip()
    	features = [x.strip() for x in response.xpath("//div[@id='feature-bullets']/ul/li/span[@class='a-list-item']/text()").extract()]
    	colors = [x.split(" ")[-1] for x in response.xpath("//div[@id='variation_color_name']/ul/li/@title").extract()]
		with open('items.txt', 'w') as f:
    		f.write(brand+','+title+','+price+','+rate+','+category+','+str(features) + ',' + str(colors))
>>>>>>> 2c7e589879ba0db94706ba729130038ccdf9ac76

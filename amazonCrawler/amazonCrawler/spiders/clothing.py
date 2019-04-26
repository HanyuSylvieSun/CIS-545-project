# -*- coding: utf-8 -*-
import scrapy


class ClothingSpider(scrapy.Spider):
    name = 'clothing'
    allowed_domains = ['www.amazon.com']
    start_urls = ['https://www.amazon.com/gp/product/B07HN3ZCS1/ref=s9_acsd_newrz_hd_bw_b2hbDCl_c_x_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-11&pf_rd_r=2N3V3PDNRKF16P1NF9W7&pf_rd_t=101&pf_rd_p=e1e9ee3d-e9cf-5b00-b9b2-4c2862506279&pf_rd_i=2476517011']

    def parse(self, response):
    	title = response.css('#productTitle::text').extract_first().strip()
    	brand = response.css('#brand').attrib['href'].split("/")[1]
    	price = response.css('#priceblock_ourprice::text').extract()[0]
    	rate = response.css('span.a-icon-alt::text').extract_first().split(" ")[0]
    	category = response.xpath("//div[@id='wayfinding-breadcrumbs_feature_div']/ul/li/span[@class='a-list-item']/a/text()").extract()[-1].strip()
    	features = [x.strip() for x in response.xpath("//div[@id='feature-bullets']/ul/li/span[@class='a-list-item']/text()").extract()]

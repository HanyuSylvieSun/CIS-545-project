# -*- coding: utf-8 -*-
import scrapy


class ClothingSpider(scrapy.Spider):
    name = 'clothing'
    allowed_domains = ['www.amazon.com']
    start_urls = ['https://www.amazon.com/gp/product/B07HN3ZCS1/ref=s9_acsd_newrz_hd_bw_b2hbDCl_c_x_w?pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-11&pf_rd_r=2N3V3PDNRKF16P1NF9W7&pf_rd_t=101&pf_rd_p=e1e9ee3d-e9cf-5b00-b9b2-4c2862506279&pf_rd_i=2476517011']

    def parse(self, response):
    	# title
        for title in response.css('#productTitle::text').extract():
            print(title.strip())
        # brand
        response.css('#brand').attrib['href'].split("/")[1]

        # for next_page in response.css('a.next-posts-link'):
        #     yield response.follow(next_page, self.parse)
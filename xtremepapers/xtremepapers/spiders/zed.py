# -*- coding: utf-8 -*-
import scrapy
from ..items import XtremepapersItem


class ZedSpider(scrapy.Spider):
    name = 'xpap'
    # allowed_domains = ['https://papers.xtremepape.rs/CAIE/IGCSE/Biology%20(0610)/']
    start_urls = ['https://papers.xtremepape.rs/CAIE/IGCSE/Biology%20(0610)/']

    def parse(self, response):
        items = XtremepapersItem()
        table = response.css('table.autoindex_table td.autoindex_td')
        for con in table:
            text = con.css('a.autoindex_a::text').extract()
            links = con.css('a.autoindex_a').xpath('@href').extract

            items['text'] = text
            items['links'] = links
            yield items

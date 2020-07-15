# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class XtremepapersItem(scrapy.Item):
    # define the fields for your item here like:
    links = scrapy.Field()
    text = scrapy.Field()
    pass

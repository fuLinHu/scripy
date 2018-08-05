# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyfirstItem(scrapy.Item):
    name=scrapy.Field()
    url=scrapy.Field()
    nextUrl=scrapy.Field()
    content=scrapy.Field()
    imageUrl=scrapy.Field()
    # define the fields for your item here like:
    # name = scrapy.Field()
class IpItem(scrapy.Item):
    ip=scrapy.Field()
    port = scrapy.Field()
    httpType = scrapy.Field()
    speed = scrapy.Field()

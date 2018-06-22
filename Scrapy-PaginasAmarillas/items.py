# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PaginasAmarillasItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    nombre = scrapy.Field()
    sitio = scrapy.Field()
    des = scrapy.Field()
    pass

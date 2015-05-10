# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class WatchaliveItem(scrapy.Item):
    # define the fields for your item here like:
    platform = scrapy.Field()
    game = scrapy.Field()
    link = scrapy.Field()
    watchpeople = scrapy.Field()
    playerName = scrapy.Field()
    playerTitle = scrapy.Field()
    playerThumb = scrapy.Field()
    playerStatus = scrapy.Field()

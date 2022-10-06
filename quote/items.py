# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class QuoteItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #文本
    text = scrapy.Field()
    #作者
    author = scrapy.Field()
    # 标签
    tags = scrapy.Field()
    #作者出生日期
    author_born_date = scrapy.Field()
    #作者出生地址
    author_born_location = scrapy.Field()
    #作者介绍
    author_description = scrapy.Field()
    pass

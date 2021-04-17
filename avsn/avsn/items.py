# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AvsnItem(scrapy.Item):
    # define the fields for your item here like:
    avsn = scrapy.Field()
    av_tittle = scrapy.Field()
    av_description = scrapy.Field()
    # 
    av_tags = scrapy.Field()
    # 演员
    av_performers = scrapy.Field()
    # 分类
    av_classifys = scrapy.Field()
    # 评分
    score = scrapy.Field()
    # 开发商 发行商
    publisher = scrapy.Field()
    # 生产者
    producers = scrapy.Field()
    # 导演
    director = scrapy.Field()
    # 时长
    length = scrapy.Field()
    # 发行时间
    issue_date = scrapy.Field()
    pass

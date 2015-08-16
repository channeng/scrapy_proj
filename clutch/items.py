# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ClutchItem(scrapy.Item):
    company_name = scrapy.Field()
    tagline = scrapy.Field()
    review_rating = scrapy.Field()
    review_count = scrapy.Field()
    country = scrapy.Field()
    region = scrapy.Field()
    region_code = scrapy.Field()
    employees = scrapy.Field()
    rates = scrapy.Field()
    phone = scrapy.Field()
    logo_img_link = scrapy.Field()
    company_link = scrapy.Field()
    founded_at = scrapy.Field()

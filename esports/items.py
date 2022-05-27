# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EsportsItem(scrapy.Item):
    """
        Criação de classe para padronização e manipulação dos dados vindo dos spiders.
    """
    site = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    date = scrapy.Field()
    tags = scrapy.Field()
    extract_date = scrapy.Field()


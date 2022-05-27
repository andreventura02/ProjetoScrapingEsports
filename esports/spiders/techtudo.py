import scrapy
from ..items import EsportsItem
from datetime import datetime, date


class TechTudoEsports(scrapy.Spider):
    """
        Classe para fazer requisições e extrações dos dados. 
        Essa classe herda do módulo scrapy a classe Spider, que é usada como base para
        os spiders do nosso crawler.
    """
    
    name="techtudoesports"
    start_urls = ['https://www.techtudo.com.br/tudo-sobre/counter-strike-global-offensive/',
                  'https://www.techtudo.com.br/tudo-sobre/league-of-legends/']
    
    def parse(self,response):
        directories = response.xpath("*//div/a[@class='feed-post-link gui-color-primary gui-color-hover']/@href").getall()
        for url in directories:
            yield scrapy.Request(url, callback=self.parse_noticias)
    
    def parse_noticias(self,response) -> EsportsItem:
        item = EsportsItem()
        
        if self.settings.getbool('ITEM_DAY') == True:
            date_today = date.today().strftime('%d/%m/%Y')
            date_news = response.xpath("*//div/p[@class='content-publication-data__updated']/time/text()").get().strip()[0:10]
            print(date_today,date_news)
            
            if date_news == date_today:
                item['site'] = 'Techtudo Esports'
                item['url'] = response.url
                item['title'] = response.xpath("*//div/h1[@class='content-head__title']/text()").get()
                item['author'] = response.xpath("*//div/p[@class='content-publication-data__from']/text()").get()
                item['date'] = response.xpath("*//div/p[@class='content-publication-data__updated']/time/text()").get().strip()
                item['tags'] = response.xpath("*//div/ul/li/a[@class='entities__list-itemLink']/text()").getall()
                item['extract_date'] = datetime.now()
                yield item
            else:
                pass
            
        elif self.settings.getbool('ITEM_DAY') == False:
            item['site'] = 'Techtudo Esports'
            item['url'] = response.url
            item['title'] = response.xpath("*//div/h1[@class='content-head__title']/text()").get()
            item['author'] = response.xpath("*//div/p[@class='content-publication-data__from']/text()").get()
            item['date'] = response.xpath("*//div/p[@class='content-publication-data__updated']/time/text()").get().strip()
            item['tags'] = response.xpath("*//div/ul/li/a[@class='entities__list-itemLink']/text()").getall()
            item['extract_date'] = datetime.now()
            yield item
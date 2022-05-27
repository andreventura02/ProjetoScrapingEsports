import scrapy
import locale
from ..items import EsportsItem
from datetime import datetime, date


class MaisEsports(scrapy.Spider):
    """
        Classe para fazer requisições e extrações dos dados. 
        Essa classe herda do módulo scrapy a classe Spider, que é usada como base para
        os spiders do nosso crawler.
    """
    
    name = "maisesports"
    start_urls = ['https://maisesports.com.br/cs-go/',
                  'https://maisesports.com.br/league-of-legends/']
    custom_settings = {'DOWNLOD_DELAY': 2}
    
    def __init__(self) -> None:
        locale.setlocale(locale.LC_ALL, "Portuguese_Brazil.1252")
    
    def parse(self,response):
        directories = response.xpath("*//div/a[@class='HomeNewsstyled__LinkBox-sc-1eb8h4r-0 eYDRBy']/@href").getall()
        for dir in directories:
            url = f"https://maisesports.com.br{dir}"
            yield scrapy.Request(url, callback=self.parse_noticias)
            
    def parse_noticias(self,response) -> EsportsItem:
        item = EsportsItem()
        
        if self.settings.getbool('ITEM_DAY') == True:
            date_today = date.today().strftime('%d %B %Y')
            date_news = item['date'] = response.xpath("*//div/h6[@class='AuthorAndDate__Date-sc-1r26ybx-3 jjXOhf']/text()").getall()[1].replace('de ','')
            print(date_today,date_news)
            
            if date_news == date_today:
                item['site'] = 'MaisEsports'
                item['url'] = response.url
                item['title'] = response.xpath("*//div/h1[@class='Title__StyledTitle-uyx0nb-0 dkGaqn']/text()").get()
                item['author'] = response.xpath("*//div/a[@class='AuthorAndDate__AuthorLink-sc-1r26ybx-2 ceZoXE']/text()").get()
                item['date'] = response.xpath("*//div/h6[@class='AuthorAndDate__Date-sc-1r26ybx-3 jjXOhf']/text()").getall()[1]
                item['tags'] = response.xpath("*//div/a[@class='Tagsstyled__TagButton-horb37-1 ddJvox']/text()").getall()
                categoria = response.xpath("*//div/a[@class='Category__StyledCategory-sc-11an80w-0 bevJpS']/text()").get()
                item['tags'].append(categoria)
                item['extract_date'] = datetime.now()
                yield item
            else:
                pass
            
        elif self.settings.getbool('ITEM_DAY') == False:
            item['site'] = 'MaisEsports'
            item['url'] = response.url
            item['title'] = response.xpath("*//div/h1[@class='Title__StyledTitle-uyx0nb-0 dkGaqn']/text()").get()
            item['author'] = response.xpath("*//div/a[@class='AuthorAndDate__AuthorLink-sc-1r26ybx-2 ceZoXE']/text()").get()
            item['date'] = response.xpath("*//div/h6[@class='AuthorAndDate__Date-sc-1r26ybx-3 jjXOhf']/text()").getall()[1]
            item['tags'] = response.xpath("*//div/a[@class='Tagsstyled__TagButton-horb37-1 ddJvox']/text()").getall()
            categoria = response.xpath("*//div/a[@class='Category__StyledCategory-sc-11an80w-0 bevJpS']/text()").get()
            item['tags'].append(categoria)
            item['extract_date'] = datetime.now()
            yield item
            
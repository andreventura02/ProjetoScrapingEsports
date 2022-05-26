import pymongo
import locale
from scrapy.exceptions import DropItem
from datetime import datetime


class EsportsPipeline:
        
    collection_name = 'esports'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
    
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
        )
        
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()
        
    def process_item(self, item, spider):
        if spider.name in ["techtudoesports"]:
            #Transformação e limpeza dos dados 'date','tags' e 'author'
            item['date'] = item['date'].replace('h',':')
            item['date'] = datetime.strptime(item['date'], r'%d/%m/%Y %H:%M')
            item['tags'] = [x.strip() for x in item['tags']]
            item['author'] = item['author'].strip().split(',')[0].replace('Por','').strip()
            
            #Caso possua 2 autores, transforme a string em uma lista de autores(str)
            if ' e ' in item['author']:
                item['author'] = item['author'].split(' e ')
            else:
                pass
            #Caso valor das tags seja nulo, defina o valor de None para ela.
            if item['tags'] == []:
                item['tags'] = None
            else:
                pass
            
            #Inserir o item no MongoDb
            try:
                self.db[self.collection_name].insert_one(dict(item))
            except Exception:
                raise DropItem("Item já armazenado no Banco de Dados")
            return item
        
        
        elif spider.name in ["maisesports"]:
            #Transformação dos dados 'date'
            locale.setlocale(locale.LC_ALL, "Portuguese_Brazil.1252")
            item['date'] = item['date'].replace('de ','')
            item['date'] = datetime.strptime(item['date'], '%d %B %Y')
            
            #Inserir o item no MongoDb
            try:
                self.db[self.collection_name].insert_one(dict(item))
            except Exception:
                raise DropItem("Item já armazenado no Banco de Dados")
            return item

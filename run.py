from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from esports.spiders.maisesports import MaisEsports
from esports.spiders.techtudo import TechTudoEsports


if __name__ == '__main__':
    configure_logging()
    settings = get_project_settings()
    runner = CrawlerRunner(settings)
    runner.crawl(TechTudoEsports)
    runner.crawl(MaisEsports)
    d = runner.join()
    d.addBoth(lambda _: reactor.stop())

    reactor.run()
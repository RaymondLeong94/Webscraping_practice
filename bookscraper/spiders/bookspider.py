import scrapy


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    #good for crawling with different links
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    #function to extract data from page itself
    def parse(self, response):
       #run scrapy shell
        pass

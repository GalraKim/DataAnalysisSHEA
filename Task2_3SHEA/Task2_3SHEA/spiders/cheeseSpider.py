from urllib import response
import scrapy
import time

class cheeseSpider(scrapy.Spider):
    name = "cheeseSpider"
    start_urls = ["https://pro-syr.ru/zakvaski-dlya-syra/mezofilnye/"]

    def parse(self, response):
        links = response.css("div.row.grid-july a::attr(href)")
        for link in links:
            time.sleep(3)
            yield response.follow(link, self.parse_cheese)
        link = response.css("ul.pagination a::attr(href)")[-1].get()
        if link!="https://pro-syr.ru/zakvaski-dlya-syra/mezofilnye/":
            yield response.follow(link, self.parse)

    def parse_cheese(self, response):
        yield {
            "name": response.css("div.col-md-9.col-sm-12 h1::text").get(),
            "price":response.css('li.price span.autocalc-product-price::text').get()[:-5],
            "instoke": response.css('b.outstock::text').get()
        }

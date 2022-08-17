import scrapy


class WhiskeySpider(scrapy.Spider):
    name = 'whiskey'
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response):
        title = response.css('title::text')[0].extract()
        quotes = response.css('span.text::text').extract()
        author = response.css('.author::text').extract()
        tags = response.css('.tag::text').extract()
        yield {
            'titletext' : title,
            'quotes' : quotes,
            'author' : author,
            'tags' : tags
        }

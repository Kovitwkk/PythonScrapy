import scrapy


class RedditSpider(scrapy.Spider):
    name = 'reddit'
    start_urls = ['https://www.reddit.com/r/SingaporeRaw/']

    def parse(self, response):
        #divInfo = response.css('.nU4Je7n-eSXStTBAPMYt8::text')[0:5].extract()
        timeAgo = response.css('._2VF2J19pUIMSLJFky-7PEI::text')[0:5].extract()
        postTitle = response.css('._eYtD2XCVieq6emjKBH3m::text')[0:5].extract()
        username = response.css('.oQctV4n0yUb0uiHDdGnmE::text()[1]').extract()
        yield {
            'username': username,
            'timeAgo': timeAgo,
            'postTitle': postTitle,
        }

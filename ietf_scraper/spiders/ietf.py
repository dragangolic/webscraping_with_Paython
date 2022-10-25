import scrapy


class IetfSpider(scrapy.Spider):
    name = 'ietf'
    allowed_domains = ['pythonscraping.com']
    start_urls = ['http://pythonscraping.com/linkedin/ietf.html']

    def parse(self, response):
        return {
        'number': response.xpath('//span[@class="rfc-no"]/text()').get(),
        # title = response.css('span.title::text'.get)
        'title': response.xpath('//meta[@name="DC.Title"]/@content').get(),
        'date': response.xpath('//span[@class="date"]/text()').get(),
        'description': response.xpath('//meta[@name=DC.Description.Abstract"]/@content').get(),
        'author': response.xpath('//meta[@name=DC.Creator"]/@content').get(),
        'company': response.xpath('//span[@class="author-company"]/text()').get(),
        'address': response.xpath('//span[@class="address"]/text()').get(),
        'headings': response.x.path('//span[@class="subheading"]/text()').getall()
    }

       

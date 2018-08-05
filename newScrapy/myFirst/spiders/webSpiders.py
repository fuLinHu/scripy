import scrapy
from  myFirst.items import MyfirstItem
from  scrapy import Request
from  scrapy import Selector

class WebScrapy(scrapy.Spider):
    name="myfirst"
    allowed_domains = ["douban.com"]
    start_urls = [
        "https://movie.douban.com/"
    ]

    def parse(self, response):
        root = response.xpath('//div[@id="screening"]/div[@class="screening-bd"]/ul/li')
        for i in root:
            nextUrl = i.xpath("ul/li[@class='poster']/a/@href")
            imageUrl= i.xpath("ul/li[@class='poster']/a/img/@src").extract()
            ite = MyfirstItem()
            ite['name'] = i.xpath("@data-title").extract()
            ite['url'] = i.xpath("@data-trailer").extract()
            ite['imageUrl']=imageUrl
            if nextUrl.extract():
                ite['nextUrl']=nextUrl.extract()[0]
            yield Request(url=ite['nextUrl'],meta={'item': ite}, callback=self.parse_item)

    def parse_item(self,response):
        ite=response.meta['item']
        selector=Selector(response)
        content=selector.xpath("//div[@class='indent']/span/text()").extract()
        ite['content']=content
        yield ite
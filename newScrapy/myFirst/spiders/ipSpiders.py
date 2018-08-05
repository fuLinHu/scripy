import scrapy
from myFirst.items import IpItem
from scrapy import Request
from myFirst.util.ScripyUtil import ScripyUtil


class ipScrapy(scrapy.Spider):

    name="myIP"
    allowed_domains = ["xicidaili.com"]
    start_urls = [
        "http://www.xicidaili.com/nn/"
    ]
    custom_settings = {
        'ITEM_PIPELINES': {'myFirst.IpPipeline.IpPipeline': 300}
    }

    def parse(self, response):
        scripyUtil=ScripyUtil()
        root = response.xpath("//table[@id='ip_list']/tr")
        ite = IpItem()
        for i in root[1:]:
            td = i.xpath("td/text()").extract()
            ip = td[0]
            port = td[1]
            httpType = td[5]
            speed_str = i.xpath("td/div[@class='bar']/@title").extract()[0]
            if speed_str:
                speed = float(speed_str.split("秒")[0])
                ite['speed'] = speed
            ite['ip'] = ip
            ite['port'] = port
            ite['httpType'] = httpType

            if scripyUtil.judge_ip(ip, port):
                yield ite
        nextUrl=response.xpath("//a[@class='next_page']/@href").extract()
        if nextUrl:
            nextUrlParam='http://www.xicidaili.com{0}'.format(nextUrl[0])
            yield Request(url=nextUrlParam, callback=self.parse)
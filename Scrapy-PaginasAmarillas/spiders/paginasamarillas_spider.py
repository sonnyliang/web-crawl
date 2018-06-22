from scrapy import Request
from scrapy.spiders import Spider
from paginasamarillas.items import PaginasAmarillasItem
import time

class PaginasAmarillasSpider(Spider):
    name = "empaque_flexible"

    def start_requests(self):
        url = 'http://www.paginasamarillas.com.co/servicios/empaque-flexible'
        yield Request(url)

    def parse(self,response):
        empresas = response.xpath('//div[@class="col-sm-10"]')
        for empresa in empresas:
            item = PaginasAmarillasItem()
            item['nombre']=empresa.xpath('.//span[@class="semibold"]/text()').extract()[0]
            item['sitio']=empresa.xpath('.//div[@class="url"]/a/@href').extract_first()
            item['des']=empresa.css('div.col-sm-12.infoBox p::text').extract_first()
            yield item

        for i in range(2,35):
            time.sleep(5)
            next_url = "http://www.paginasamarillas.com.co/servicios/empaques-y-envases-flexibles?page="+str(i)
            yield Request(next_url)
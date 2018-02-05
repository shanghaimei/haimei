# -*- coding: utf-8 -*-
import scrapy
from mySpider.items import ItcastItem

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ["http://www.itcast.cn/channel/teacher.shtml"]

    def parse(self, response):
        # filename = 'teacher.html'
        # open(filename,'w').write(response.body)
        items = []
        for each in response.xpath("//div[@class='li_txt']"):
            item = ItcastItem()
            name = each.xpath('h3/text()').extract()[0]
            level = each.xpath('h4/text()').extract()[0]
            info = each.xpath('p/text()').extract()[0]
            items.append(item)
        return items




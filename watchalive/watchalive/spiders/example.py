# -*- coding: utf-8 -*-
import scrapy

class ExampleSpider(scrapy.Spider):
    name = "douyu"
    allowed_domains = ["http://www.douyutv.com/"]
    start_urls = (
        'http://www.douyutv.com/directory/game/dota2',
        'http://www.douyutv.com/directory/game/sc',
        'http://www.zhanqi.tv/games/dota2',
        'http://www.zhanqi.tv/games/sc2',
        'http://www.huomaotv.com/live_list?gid=23',
        'http://www.huomaotv.com/live_list?gid=11',
    )

    def parse(self, response):
        # Douyu
        if 'douyutv'in response.url:
            if 'dota2' in response.url:
                print "斗鱼TV  Dota2主播："
            elif 'sc' in response.url:
                print "斗鱼TV  SC2主播："
            print "-" * 50
            for user in response.xpath('//*[@id="item_data"]/ul/li'):
                name = user.xpath('a/div[1]/p/span[2]/text()').extract()[0]
                title = user.xpath('a/@title').extract()[0]
                # name = response.xpath('//*[@id="item_data"]/ul/li/a/div[1]/p/span[2]/text()').extract()
                print name + '\t' + title

        # Zhanqi
        if 'zhanqi' in response.url:
            if 'dota2' in response.url:
                print "战旗TV  Dota2 主播："
            elif 'sc2' in response.url:
                print "战旗TV  SC2 主播："
            print "-" * 50
            for user in response.xpath('//*[@id="hotList"]/li'):
                status = ""
                try:
                    status = user.xpath('div[1]/i/text()').extract()[0]
                    if status.encode('utf8') == '休息':
                        continue
                except:
                    pass
                name = user.xpath('div[2]/div/a[1]/text()').extract()[0]
                title = user.xpath('div[2]/a/text()').extract()[0]
                print name + '\t' + title
        print '\n'

        # Huomao
        if 'huomao' in response.url:
            if 'gid=23' in response.url:
                print "火猫TV  Dota2 主播："
            elif 'gid=11' in response.url:
                print "火猫TV  SC2 主播："
            print "-" * 50
            for user in response.xpath('//*[@id="live_list"]/div'):
                name = user.xpath('dl[2]/dd/a/text()').extract()[0]
                title = user.xpath('dl[2]/dt/a/@title').extract()[0]
                print name + '\t' + title
        print '\n'

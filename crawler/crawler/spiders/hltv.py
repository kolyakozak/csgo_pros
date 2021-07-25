import re
from urllib.parse import urljoin

from scrapy import Selector
from scrapy.spiders import Spider, Request

import time


class HltvSpider(Spider):
    name = 'hltv'
    allowed_domains = ['hltv.org']
    start_urls = ['https://www.hltv.org/stats/players/']

    fields = {
        'player_links': '//td[contains(@class, "playerCol")]/a/@href',
        'nickname': '//h1[contains(@class, "summaryNickname")]/text()',
        'real_name': '//div[contains(@class, "summaryRealname")]/div/text()',
        'country': '//div[contains(@class, "summaryRealname")]/img/@alt',
        'team': '//div[contains(@class, "SummaryTeamname")]/a/text()',
        'age': '//div[contains(@class, "summaryPlayerAge")]/text()',
        'main_stats': '//div[contains(@class, "summaryStatBreakdownDataValue")]/text()',
        'other_stats': '//div[contains(@class , "col stats-rows standard-box")]/div/span[2]/text()'
    }

    def parse(self, response):
        root = Selector(response)

        counter = 0
        for link in root.xpath(self.fields['player_links']).getall():
            # counter += 1
            # if counter > 10:
            #     break
            time.sleep(2)
            yield Request(urljoin(response.url, link), callback=self.parse_player_page)

    def parse_player_page(self, response):
        root = Selector(response)
        item = {}

        item['id'] = int(remove_non_digit(response.url))

        item['nickname'] = root.xpath(self.fields['nickname']).get()
        item['real_name'] = root.xpath(self.fields['real_name']).get()
        item['country'] = root.xpath(self.fields['country']).get()
        item['team'] = root.xpath(self.fields['team']).get()
        item['age'] = int(remove_non_digit(root.xpath(self.fields['age']).get()))
        
        main_stats = root.xpath(self.fields['main_stats'])
        item['rating'] = float(main_stats[0].get())
        item['dpr'] = float(main_stats[1].get())
        item['kast'] = float(remove_non_numeric(main_stats[2].get()))
        item['impact'] = float(main_stats[3].get())
        item['adr'] = float(main_stats[4].get())
        item['kpr'] = float(main_stats[5].get())

        other_stats = root.xpath(self.fields['other_stats'])
        item['total_kills'] = int(other_stats[0].get())
        item['headshot_percentage'] = float(remove_non_numeric(other_stats[1].get()))
        item['total_deaths'] = int(other_stats[2].get())
        item['kd'] = float(other_stats[3].get())

        return item



def remove_non_numeric(line):
    return re.sub('[^0-9.]', '', line)

def remove_non_digit(line):
    return re.sub('[^0-9]', '', line)
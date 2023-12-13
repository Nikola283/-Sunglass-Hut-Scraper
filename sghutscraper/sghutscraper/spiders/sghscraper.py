import scrapy
import json


class SghscraperSpider(scrapy.Spider):
    name = "sghscraper"
    allowed_domains = ["sunglasshut.com"]
    start_urls = ["https://www.sunglasshut.com/wcs/resources/plp/10152/byPartNumbers/8056597660426,8056597686099,8056597850834,8056597660143,8056597895453,725125399159,8056597829755,8056597829724,8056597883818,8056597851961,8056597829533,8056597861106,888392601599,8056597837187,8056597729970,8056597890632,8056597848961,8056597838528,8056597785303,8056597838511,8056597787505,725125399135,8056597848961,8056597690133,8056597838511,8056597849005,8056597852470,8056597792394,8056597712057,888392593412,888392597601,8056597720670,8056597720656,8056597681148,888392591043,888392590213,8056597684460"]

    def parse(self, response):
        data = json.loads(response.body)
        yield from data['plpView']['products']['products']['product']

        next_page = data['plpView']['nextPageURL']
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

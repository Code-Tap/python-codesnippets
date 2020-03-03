#initial setup
#scrapy startproject manheim
#scrapy genspider amxbot http://inspect.portal.manheim.co.uk/

#run code
#scrapy crawl amxbot

#settings
#Export as CSV Feed
#FEED_FORMAT = "CSV"
#FEED_URI = "amx.csv"



# -*- coding: utf-8 -*-
import scrapy


class QuoteScrapeSpider(scrapy.Spider):
    name = 'quote_scrape'
    start_urls = ['http://inspect.portal.manheim.co.uk/']
    #download_delay = 0.5

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={
                # "__VIEWSTATE":VIEWSTATE,
                # "__VIEWSTATEGENERATOR":VIEWSTATEGENERATOR,
                'ctl00$ContentPlaceHolder1$Login1$UserName' :'username',
                'ctl00$ContentPlaceHolder1$Login1$Password' : 'password',
                'ctl00$ContentPlaceHolder1$Login1$LoginButton' : 'Log In'
            },
            callback=self.parse_results
        )

    # def parse_tags(self, response):
    #     for tag in response.css('select#tag > option ::attr(value)').extract():
    #         yield scrapy.FormRequest.from_response(
    #             response,
    #             formdata={'tag': tag},
    #             callback=self.parse_results,
    #             )

    def parse_results(self, response):
        for quote in response.css("div.container"):
            yield {
                'quote': quote.css('span.sr-only ::text').extract_first(),
                # 'author': quote.css('span.author ::text').extract_first(),
                # 'tag': quote.css('span.tag ::text').extract_first(),
            }

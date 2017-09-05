#- * -coding: utf - 8 - * -
import scrapy
from scrapy.http import Request, TextResponse
from scrapy.spiders import Rule, CrawlSpider
from scrapy.linkextractors import LinkExtractor
import os
from rake_nltk import Rake

class InvestopediaSpider(CrawlSpider):
    name = 'investopedia'
    allowed_domains = ['http://www.investopedia.com/news/']
    start_urls = ['http://www.investopedia.com/news/']
    
    #rules = (
    #    Rule(LinkExtractor(allow=r"/news/?page=\d+$"), callback='parse'),
    #)
    

    def parse(self, response):
        
        self.parse_pages(response)
        all_pages = response.css(".pagination li a::text")[3].extract()
        for i in range(int(all_pages)):
            if i is not 0:
                new_url = 'http://www.investopedia.com/news/?page=' + str(i);
                next_page = response.urljoin(new_url)
                yield Request(next_page, self.parse_pages, dont_filter=True)
        #yield items

    def parse_pages(self, response):
        title = response.css(".item-title a::text").extract()
        url = response.css(".item-title a::attr('href')").extract()
        description = response.css(".item-description::text").extract()
        for item in zip(title, url, description):
            r = Rake()
            r.extract_keywords_from_text(item[0])
            newkey = r.get_ranked_phrases()
            newkey = ", ".join(newkey)

            scraped_info = {
                'title': item[0],
                'url': item[1],
                'description': item[2],
                'keyword': newkey
            }
            yield scraped_info



    def fake_response_from_file(file_name, url=None):
        """
        Create a Scrapy fake HTTP response from a HTML file
        @param file_name: The relative filename from the responses directory,
                          but absolute paths are also accepted.
        @param url: The URL of the response.
        returns: A scrapy text response which can be used for unittesting.
        """

        url = 'file:///home/samuel/investopeida/investopeida/index.html'
        request = Request(url=url)
        file = '/home/samuel/investopeida/investopeida/index.html'
        file_content = open(file, 'r').read()
        
        response = TextResponse(url=url, request=request, body=file_content, encoding='utf-8')
        #response.encoding = 'utf-8'
        return response
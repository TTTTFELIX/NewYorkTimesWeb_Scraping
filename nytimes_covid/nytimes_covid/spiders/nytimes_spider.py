import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class NytimesSpiderSpider(CrawlSpider):
    name = "nytimes"
    allowed_domains = ["nytimes.com"]
    start_urls = ["https://www.nytimes.com/sitemap/2022/"]

    rules = (
        Rule(LinkExtractor(restrict_css='a'), callback="parse_article", follow=True),
    )


    def parse_article(self, response):
        title = response.css("h1::text").get()
        if '/2022/' in response.url:
            content = " ".join(response.css("p::text").getall())
            if 'covid' in content.lower():
                yield {
                    "title": title,
                    "url": response.url
                }

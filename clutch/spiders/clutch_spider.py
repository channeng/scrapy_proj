import scrapy

from clutch.items import ClutchItem

class ClutchSpider(scrapy.Spider):
    name = "clutch"
    allowed_domains = ["clutch.co"]
    start_urls = [
        "https://clutch.co/web-developers/"
    ]

    def parse(self, response):
        href = response.xpath("//li[@class='pager-next last']/a/@href")
        url = response.urljoin(href.extract()[0])
        yield scrapy.Request(url, callback=self.parse_dir_contents)
    
    def parse_dir_contents(self, response):
        for sel in response.xpath("//div[@class='view-content']/div[@class='provider-row']"):
            item = ClutchItem()
            item['company_name'] = sel.xpath("div/div/h3[@class='company-name']/a/text()").extract()
            item['tagline'] = sel.xpath("div/div/h5[@class='tagline']/text()").extract()
            item['review_rating'] = sel.xpath("div/div/div[@class='rating-reviews']/a[2]/span[@class='rating']/text()").extract()
            yield item
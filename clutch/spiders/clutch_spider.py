import scrapy

from clutch.items import ClutchItem

class ClutchSpider(scrapy.Spider):
    name = "clutch"
    allowed_domains = ["clutch.co"]
    start_urls = [
        'https://clutch.co/web-developers?page=%s' % page for page in xrange(24)
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
            item['review_count'] = sel.xpath("div/div/div[@class='rating-reviews']/a[2]/span[@class='count']/text()").extract()
            item['country'] = sel.xpath("div/div/span[@class='location-country']/span[@class='country-name']/text()").extract()
            item['region'] = sel.xpath("div/div/span[@class='location-city']/span[@class='locality']/text()").extract()
            item['region_code'] = sel.xpath("div/div/span[@class='location-city']/span[@class='region']/text()").extract()
            item['employees'] = sel.xpath("div/div/span/span[@class='employees']/text()").extract()
            item['rates'] = sel.xpath("div/div/span[@class='hourly-rate']/text()").extract()
            item['phone'] = sel.xpath("div/div[@class='col-xs-12 visible-xs phone feature']/span[@class='location-phone']/text()").extract()
            item['logo_img_link'] = sel.xpath("div/div/div/a/img[@class='img-responsive']/@src").extract()
            yield item
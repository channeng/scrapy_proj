import scrapy

from clutch.items import ClutchItem

class ClutchSpider(scrapy.Spider):
    # Name the spider so you can run in bash 'scrapy crawl clutch1'
    name = "clutch1"
    # Define the boundaries of the playground
    allowed_domains = ["clutch.co"]
    # Start crawl from this urls
    start_urls = [
        'https://clutch.co/web-developers' 
    ]

    # Initiate parse logic
    def parse(self, response):   
        # For each row in the table
        for sel in response.xpath("//div[@class='view-content']/div[@class='provider-row']"):
            # Initiate srapy item object --> Make sure items declared are defined in items.py
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
            item['company_link'] = sel.xpath("div/div/span[@class='website-link']/a/@href").extract()
            
            # Extract sublink to follow within the result (in this case, the clutch profile page of the company)
            clutch_profile_link = response.urljoin(sel.xpath("div/div/h3[@class='company-name']/a/@href")[0].extract())
            # Initialize next scrapy request (i.e. second parse on the profile link)
            request = scrapy.Request(clutch_profile_link, callback=self.parse_subdir)
            # Pass 'item' object from first parse, along with request for second parse
            request.meta['item']= item
            # Run the request --> 'Yield' is the generator form of 'return'
            yield request
            
        # Get the url of the next page
        next_page = response.xpath("//li[@class='pager-next last']/a/@href")

        if next_page:
            url = response.urljoin(next_page[0].extract())
            # If next page url is found, callback parse (this function) again.
            yield scrapy.Request(url, callback=self.parse)

    # This function is the second parse. It parses the link obtained from first parse
    # to get the date the company was founded at.
    def parse_subdir(self,response):
        # Retrieves item object (dictionary) created from first parse
        item = response.meta['item']
        # Creates new key value pair for date company founded at
        item["founded_at"] = response.xpath("//div[@class='field field-name-field-pp-year-founded field-type-number-integer field-label-inline clearfix']/div/div/text()").extract()
        # generates the item (all the details of the company)
        yield item
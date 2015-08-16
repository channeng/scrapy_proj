company_name = response.xpath("div/div/h3[@class='company-name']/a/text()").extract()

tagline = response.xpath("div/div/h5[@class='tagline']/text()").extract()

review_rating = response.xpath("div/div/div[@class='rating-reviews']/a[2]/span[@class='rating']/text()").extract()


""" NOT CHECKED BELOW YET"""
"""
review_count = response.xpath("//div[@class='rating-reviews']/a[2]/span[@class='count']/text()").extract()

country = response.xpath("//span[@class='location-country']/span[@class='country-name']/text()").extract()
region = response.xpath("//span[@class='location-city']/span[@class='locality']/text()").extract()
region_code = response.xpath("//span[@class='location-city']/span[@class='region']/text()").extract()

employees = response.xpath("//span[@class='employees']/text()").extract()

rates = response.xpath("//span[@class='hourly-rate']/text()").extract()

phone = response.xpath("//div[@class='col-xs-12 visible-xs phone feature']/span[@class='location-phone']/text()").extract()
# Need to strip whitespaces

logo_img_link = response.xpath("//div[@class='col-xs-12 visible-xs phone feature']/span[@class='location-phone']/text()").extract()
#prepend 'https:'

next_page = response.xpath("//li[@class='pager-next last']/a/@href").extract()


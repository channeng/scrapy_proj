# scrapy_proj
Scrapy project to scrap website data from www.clutch.co

Pull repo
Run in bash: 'scrapy crawl clutch -o items.json'

This will initiate clutch_spider to crawl for 24 pages of results and return a json file with the following fields:
- company_name
- tagline
- review_rating
- review_count
- country
- region
- region_code
- employees
- rates
- phone
- logo_img_link

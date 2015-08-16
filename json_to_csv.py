import json
import csv

with open('items2.json','r') as f:
	json_data = json.load(f)

cleaned_data = []
for company in json_data:
	cleaned_row = {}
	for i in company:
		try:
			cleaned_row[i] = company[i][0].encode('utf-8').strip()
		except IndexError:
			cleaned_row[i] = ""
	cleaned_data.append(cleaned_row)

csv_headers = ["company_name", "tagline", "review_rating", "review_count", "country", "region", "region_code", "employees", "rates", "phone", "logo_img_link","company_link","founded_at"]

with open('items2.csv','wb+') as wb:
	writer = csv.writer(wb)
	writer.writerow(csv_headers)
	for company in cleaned_data:
	    writer.writerow([
	    	company["company_name"], 
	        company["tagline"],
	        company["review_rating"],
	        company["review_count"],
	        company["country"], 
	        company["region"], 
	        company["region_code"], 
	        company["employees"], 
	        company["rates"], 
	        company["phone"], 
	        company["logo_img_link"],
	        company["company_link"],
	        company["founded_at"]
	        ])
Sunglass Hut Scraper
This repository features a Scrapy web scraper designed to extract product information from Sunglass Hut's website. The spider, named "sghscraper," navigates through a predefined list of product URLs, parses JSON responses, and collects relevant data. The scraper is built to handle pagination, ensuring comprehensive coverage of the product listings.
Highlights
•	Scrapy Framework: Utilizes the Scrapy Python framework for efficient web crawling and scraping.
•	Targeted Domain: Focused on the sunglasshut.com domain to retrieve sunglasses product details.
•	Pagination Handling: Automatically follows pagination links to gather information from multiple pages.

Usage: 
1.	Prerequisites:
•	Ensure you have Python (3.7 or higher) installed.
•	Install Scrapy using pip install scrapy.
•	Set the virtual enviroment
3.	Run the Scraper:
•	Execute the scraper using the command scrapy runspider sghscraper.py -o output.json.
•	Replace output.json with the desired output file name.
Output
The scraped data, containing product details, is saved in JSON format in the specified output file.


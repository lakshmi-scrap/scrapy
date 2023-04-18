import scrapy


class FirstScrpy(scrapy.Spider):
    name = 'meta'
    
    start_urls = ['https://www.metacareers.com/jobs?page=1&results_per_page=100#search_result',
                'https://www.metacareers.com/jobs/?is_leadership=0&page=2&results_per_page=100&is_in_page=0',
                'https://www.metacareers.com/jobs/?is_leadership=0&page=3&results_per_page=100&is_in_page=0']
    custom_settings = {
        'FEED_FORMAT': 'json',
        'FEED_URI': 'output.json'
    }
    def parse(self,response):

        all_div_quotes = response.css('a._8sef')
        
        for div_quote in all_div_quotes:
            job_title = div_quote.css('div._8sel::text').extract()
            location = div_quote.css('._8see::text').extract()
            # location = div_quote.css('._97fe > ._8sed ._97fe::text').extract()
            yield { 
                'job_title' : job_title,
                'location,University and Skills' : location
            }

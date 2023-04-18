# import scrapy


# class FirstScrpy(scrapy.Spider):
#     name = 'quotes'
    
#     start_urls = ['https://quotes.toscrape.com/']
    
#     def parse(self,response):
#         # title = response .css('title::text').extract()
#         # yield {'titletext' : title }
        
#         all_div_quotes = response.css('div.quote')
#         title = all_div_quotes.css('span.text::text').extract()
#         author = all_div_quotes.css('.author::text').extract()
#         tag = all_div_quotes.css('.tag::text').extract()
        
#         yield { 'title' : title, 'author' : author, 'tags': tag }
        
        
import scrapy

class FirstScrpy(scrapy.Spider):
    name = 'quotes'
    start_urls = ['https://quotes.toscrape.com/']
    
    def parse(self, response):
        all_div_quotes = response.css('div.quote')
        for quote in all_div_quotes:
            title = quote.css('span.text::text').extract_first()
            author = quote.css('.author::text').extract_first()
            tag = quote.css('.tag::text').extract()

            yield {
                'title': title,
                'author': author,
                'tags': tag
            }

        # follow the link to the next page and repeat the parsing process
        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

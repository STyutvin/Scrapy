import scrapy


class KleineSpinneSpider(scrapy.Spider):
    name = "kleine_spinne_3"
    allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/List_of_best-selling_books"]
    custom_settings = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

    def parse(self, response):
        rows = response.xpath('//table[3][contains(@class, "wikitable")]//tbody/tr')
        for row in rows:
            book_name = row.xpath('.//td[1]/i/a/text()').get()
            author = row.xpath('.//td[2]/a/text()').get()
            original_language = row.xpath('.//td[3]/text()').get()
            first_published = row.xpath('.//td[4]/text()').get()
            approximate_sales = row.xpath('.//td[5]/text()').get()
            genre = row.xpath('.//td[6]/a/text()').get()
            
            yield{
                'book_name': book_name,
                'author': author,
                'original_language': original_language,
                'first_published': first_published,
                'approximate_sales': approximate_sales,
                'genre': genre
            }

import requests
from bs4 import BeautifulSoup

BASE_URL = 'https://quotes.toscrape.com'


class Spider:
    def parse(self, response):
        raise NotImplementedError


class AuthorsSpider(Spider):
    def __init__(self):
        self.author_urls_list = []

    def _get_author_urls(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        links = soup.select("div[class=quote] span a")
        prefix = '/author'
        urls = [BASE_URL + link['href'] for link in links if link['href'].startswith(prefix)]
        new_urls = [url for url in urls if url not in self.author_urls_list]
        self.author_urls_list.extend(new_urls)
        return new_urls

    def _get_author_info(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        fullname = soup.select("div[class=author-details] h3[class=author-title]")[0].text.strip()
        born_date = soup.select("div[class=author-details] span[class=author-born-date]")[0].text.strip()
        born_location = soup.select("div[class=author-details] span[class=author-born-location]")[0].text.strip()
        description = soup.select("div[class=author-description]")[0].text.strip()

        if fullname == 'Alexandre Dumas-fils':
            fullname = 'Alexandre Dumas fils'

        author_info = {
            "fullname": fullname,
            "born_date": born_date,
            "born_location": born_location,
            "description": description
        }
        return author_info

    def parse(self, response):
        urls = self._get_author_urls(response)
        result = [self._get_author_info(url) for url in urls]
        return result


class QuotesSpider(Spider):
    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')
        quote_blocks = soup.select('div[class=quote]')
        result = []

        for quote in quote_blocks:
            quote_text = quote.select('span[class=text]')[0].text.strip('"\u201c\u201d')
            quote_author = quote.select('span small[class=author]')[0].text.strip()
            quote_tags = [tag.text.strip() for tag in quote.select('div[class=tags] a')]
            result.append({
                'tags': quote_tags,
                'author': quote_author,
                'quote': quote_text
            })

        return result


class QuotesParser:
    def __init__(self, quotes_spider=QuotesSpider(), authors_spider=AuthorsSpider()):
        self.quotes_spider = quotes_spider
        self.authors_spider = authors_spider

    @staticmethod
    def _has_next_page(response):
        html = response.text
        soup = BeautifulSoup(html, 'lxml')
        next_page_tag = soup.select('li[class="next"]')
        return bool(next_page_tag)

    def parse(self, url: str):
        page = 1
        authors = []
        quotes = []

        while True:
            if page == 1:
                page_url = url
            else:
                page_url = f'{url}/page/{page}/'

            response = requests.get(page_url)

            if response.status_code != 200:
                print('Error while fetching page, status: {}'.format(response.status_code))
                continue

            try:
                quotes_result = self.quotes_spider.parse(response)
                authors_result = self.authors_spider.parse(response)
                quotes.extend(quotes_result)
                authors.extend(authors_result)
            except Exception as err:
                print(err, f'on page {page}')

            if not self._has_next_page(response):
                break

            page += 1

        return quotes, authors
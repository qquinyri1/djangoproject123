import os
import json
from datetime import datetime
import django

from scraper.scraper import QuotesParser, BASE_URL
from quotes_app.models import Quote, Tag, Author

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quotes.settings')
django.setup()


def load_quotes(parser=QuotesParser()):
    quotes, authors = parser.parse(BASE_URL)

    for author in authors:
        author['born_date'] = datetime.strptime(author['born_date'], '%B %d, %Y').date()
        Author.objects.get_or_create(**author)

    for quote in quotes:
        tags = [Tag.objects.get_or_create(name=tag)[0] for tag in quote['tags']]
        author = Author.objects.filter(fullname=quote['author']).first()

        if author and not Quote.objects.filter(quote=quote['quote']).exists():
            new_quote = Quote.objects.create(
                quote=quote['quote'],
                author=author,
            )
            new_quote.tags.add(*tags)

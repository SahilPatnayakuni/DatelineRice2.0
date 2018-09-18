import feedparser
from enum import Enum

class ArticleAttributes(Enum):
    URL = 0,
    TITLE = 1,
    DESCRIPTION = 2,
    PUBLICATION_DATE = 3,
    AUTHORS = 4

class Article:
    def __init__(self, url=None, title=None, description=None, publicationDate=None, authors=None):
        self.url = url
        self.title = title
        self.description = description
        self.publicationDate = publicationDate
        self.authors = authors

    def set_url(self, url):
        self.url = url

    def set_title(self, title):
        self.title = title

    def set_description(self, description):
        self.description = description

    def set_publicationDate(self, publicationDate):
        self.publicationDate = publicationDate

    def set_authors(self, authors):
        self.authors = authors

    def get_url(self):
        return self.url

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_publicationDate(self):
        return self.publicationDate

    def get_authors(self):
        return self.authors

rss_feed_url = "https://us.vocuspr.com/Publish/523718/DatelineRice.xml"

rss_mapping = {
    ArticleAttributes.URL: "link",
    ArticleAttributes.TITLE: "title",
    ArticleAttributes.DESCRIPTION: "description",
    ArticleAttributes.PUBLICATION_DATE: "published",
    ArticleAttributes.AUTHORS: "authors",
}

feed = feedparser.parse(rss_feed_url)
articles = []

for entry in feed.entries:
    url, title, description, publicationDate, authors = (None, None, None, None, None)
    if ArticleAttributes.URL in rss_mapping:
        url = entry[rss_mapping[ArticleAttributes.URL]]
    if ArticleAttributes.TITLE in rss_mapping:
        title = entry[rss_mapping[ArticleAttributes.TITLE]]
    if ArticleAttributes.DESCRIPTION in rss_mapping:
        description = entry[rss_mapping[ArticleAttributes.DESCRIPTION]]
    if ArticleAttributes.PUBLICATION_DATE in rss_mapping:
        publicationDate = entry[rss_mapping[ArticleAttributes.PUBLICATION_DATE]]
    if ArticleAttributes.AUTHORS in rss_mapping:
        authors = entry[rss_mapping[ArticleAttributes.AUTHORS]]
    articles.append(Article(url, title, description, publicationDate, authors))

print(len(articles))
print(articles)
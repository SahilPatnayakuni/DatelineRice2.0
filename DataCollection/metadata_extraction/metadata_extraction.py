from newspaper import Article
from urllib.parse import urlparse
import sys

sys.path.append("..")
import shared_types
sys.path.pop()

class MetadataExtractor:
    def __init__(self, url, article_data=None):
        self.url = url
        self.article_data = article_data
        if self.article_data is None:
            self.article_data = ArticleData(url=url)

        self.article = Article(url)
        self.article.download()
        self.article.parse()

    def extract_missing(self):
        if self.article_data.url is None:
            self.article_data.url = self.url

        if self.article_data.headline is None:
            self.article_data.headline = self.extract_headline()

        if self.article_data.publication_date is None:
            self.article_data.publication_date = self.extract_pubdate()

        if self.article_data.authors is None:
            self.article_data.authors = self.extract_authors()

        if self.article_data.outlet is None:
            self.article_data.outlet = self.extract_outlet()
        

    def extract_headline(self):
        return self.article.title

    def extract_pubdate(self):
        return self.article.publish_date

    def extract_authors(self):
        return self.article.authors

    def extract_outlet(self):
        outletUrl = urlparse(self.url).netloc
        return outletUrl

    def extract_bodytext(self):
        return self.text


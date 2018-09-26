from newspaper import Article
from urllib.parse import urlparse
import re
import sys

# Workaround to import a file from an outer directory
sys.path.append("..")
from shared_types import ArticleData, Outlet
sys.path.pop()

class MetadataExtractor:
    def __init__(self, article_data):
        self.article_data = article_data
        if article_data.url is None:
            raise ValueError("Provided ArticleData object has no url")
            return

        self.url = article_data.url
        if self.article_data is None:
            self.article_data = ArticleData(url=self.url)

        self.article = Article(self.url)
        self.article.download()
        self.article.parse()

    def extract_missing(self):
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
        np_result = self.article.publish_date
        if np_result is None:
            body = self.extract_bodytext()
            
            re.search("[0-9]+\/[0-9]+\/[0-9]+", body)
        else:
            return np_result

    def extract_authors(self):
        return self.article.authors

    def extract_outlet(self):
        outlet_domain = urlparse(self.url).netloc
        # A lookup will happen here
        outlet = Outlet(domain=outlet_domain)
        return outlet

    def extract_bodytext(self):
        return self.article.text
        



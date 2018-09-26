import feedparser
import os, sys
sys.path.append('..') # Note: this doesn't work if the relative class structure changes
from shared_types import ArticleData, Outlet

class CisionFeed:
    """
    CisionFeed is a wrapper around the Cision RSS feed.
    """

    # The URL of the RSS feed. This URL updates every time the update is
    # MANUALLY triggered by the dateline team.
    rss_feed_url = "https://us.vocuspr.com/Publish/523718/DatelineRice.xml"

    def __init__(self):
        """
        Initialize a new instance of the CisionFeed class.
        There's no reason to ever do this more than once.
        """
        self.feed = feedparser.parse(self.rss_feed_url)

    def parse(self):
        """
        Parse the current state of the feed.
        This fills in URL, title, description, publication date,
        and authors.
        """
        articles = []
        for entry in self.feed.entries:
            print(entry)
            url = entry["link"]
            title = entry["title"]
            description = entry["description"]
            publicationDate = entry["published"]
            authors = [a['name'] for a in entry["authors"] if 'name' in a]
            articles.append(ArticleData(url, title, description, publicationDate, authors))
        return articles

# Testing please ignore :)
# c = CisionFeed()
# c.parse()
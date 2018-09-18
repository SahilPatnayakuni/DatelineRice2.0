import json 

class ArticleData:
    def __init__(self, url=None, headline=None, description=None, publication_date=None, authors=None, outlet=None, body_text=None):
        self.url = url
        self.headline = headline
        self.description = description
        self.publication_date = publication_date
        self.authors = authors
        self.body_text = body_text
        self.outlet = outlet

    def to_json(self):
        jsonOutput = {}
        jsonOutput["url"] = self.url
        jsonOutput["headline"] = self.headline
        jsonOutput["coverageDate"] = self.publication_date
        jsonOutput["authors"] = self.authors
        jsonOutput["mediaOutletName"] = self.outlet.name
        jsonOutput["mediaType"] = self.outlet.media_type
        jsonOutput["category"] = self.outlet.category
        jsonOutput["locale"] = self.outlet.locale

        return json.dumps(jsonOutput)


class Outlet:
    def __init__(self, name=None, media_type=None, locale=None, category=None, domain=None):
        self.name = name
        self.media_type = media_type
        self.locale = locale
        self.category = category
        self.domain = domain # Base domain for the outlet, not for a particular article


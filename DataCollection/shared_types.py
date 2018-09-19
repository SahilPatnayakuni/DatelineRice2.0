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
        """
        Exports metadata in a flat JSON structure, as a string. 
        Use json.loads() to inflate the output of this function into an accessbile JSON object.
        """
        json_output = {}
        json_output["url"] = self.url
        json_output["headline"] = self.headline if self.headline is not None else "unknown"
        json_output["coverageDate"] = self.publication_date.strftime("%Y-%m-%d") if self.publication_date is not None else "unknown"
        json_output["authors"] = self.authors if self.authors is not None else "unknown"
        json_output["mediaOutletName"] = self.outlet.name if self.outlet.name else "unknown"
        json_output["mediaType"] = self.outlet.media_type if self.outlet.media_type  is not None else "unknown"
        json_output["category"] = self.outlet.category if self.outlet.category is not None else "unknown"
        json_output["locale"] = self.outlet.locale if self.outlet.locale is not None else "unknown"

        return json.dumps(json_output)

    def __str__(self):
        return json.dumps(json.loads(self.to_json()), sort_keys=True, indent=4)



class Outlet:
    def __init__(self, name=None, media_type=None, locale=None, category=None, domain=None):
        self.name = name
        self.media_type = media_type
        self.locale = locale
        self.category = category
        self.domain = domain # Base domain for the outlet, not for a particular article


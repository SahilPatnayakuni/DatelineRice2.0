CREATE TABLE IF NOT EXISTS 'mediamentions' (
    'mention_id' int NOT NULL auto_increment PRIMARY KEY,
    'related_mention_id' int auto_increment,
    'headline' varchar(255),
    'media_outlet_name' varchar(255),
    'media_type' enum('web', 'newspaper', 'radio', 'tv') NOT NULL,
    'scope' enum('national', 'international', 'local/state'),
    'locale' varchar(255) NOT NULL DEFAULT 'USA',
    'language' varchar(255) NOT NULL DEFAULT 'en',
    'coverage_date' DATETIME NOT NULL,
    'dateline_publish_date' DATETIME,
    'category' enum('featured', 'sports', 'trade/professional', 'broadcast', 'houston/texas', 'national/international', 'othernews', 'releases'),
    'orgs_mentioned' json,
    'description' varchar(255),
    'url' varchar(255) UNIQUE,
    'author' varchar(255),
    'status' boolean,

    FOREIGN KEY(related_mention_id) REFERENCES mediamentions(mention_id)
)

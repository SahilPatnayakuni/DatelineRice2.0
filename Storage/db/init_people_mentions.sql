CREATE TABLE IF NOT EXISTS 'peoplementions' (
    'mention_id' int NOT NULL,
    `person_id` int NOT NULL,
    FOREIGN KEY(mention_id) REFERENCES(mediamentions)
    FOREIGN KEY(person_id) REFERENCES(people)
);
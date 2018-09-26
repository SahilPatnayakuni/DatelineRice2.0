CREATE TABLE IF NOT EXISTS 'people' (
    'person_id' int NOT NULL auto_increment PRIMARY KEY,
    'net_id' varchar(255) UNIQUE NOT NULL,
    'first_name' varchar(255) NOT NULL,
    'last_name' varchar(255) NOT NULL,
    'title' varchar(255) NOT NULL,
    'type' enum('student', 'faculty', 'staff') NOT NULL,
    'organizations' json,
    'residential_college' varchar(255),
    'majors' json,
    'is_former' boolean,
    'graduation_year' int
)
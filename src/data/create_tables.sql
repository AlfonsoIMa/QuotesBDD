CREATE TABLE IF NOT EXISTS author(
    id                  INT  PRIMARY KEY,
    display_name        TEXT NOT NULL,
    full_name           TEXT NOT NULL,
    living_years        TEXT, -- TODO: IMPLEMENT
    biography           TEXT
);

CREATE TABLE IF NOT EXISTS publisher(
    id                  INT  PRIMARY KEY,
    name                TEXT NOT NULL
);

-- CREATE TABLE IF NOT EXISTS alternate_publisher();

CREATE TABLE IF NOT EXISTS book(
    id                  INT  PRIMARY KEY,
    author_id           INT  NOT NULL,
    year                INT,
    title               TEXT NOT NULL,
    publisher_id        INT  NOT NULL, 
    edition             INT,
    description         TEXT, -- TODO: ADD OTHER STUFF?
    FOREIGN KEY(author_id) REFERENCES author(id),
    FOREIGN KEY(publisher_id) REFERENCES publisher(id)
);

CREATE TABLE IF NOT EXISTS quote(
    id                  INT  PRIMARY KEY,
    book_id             INT,
    author_id           INT  NOT NULL,
    quote               TEXT NOT NULL,
    year                INT
);

DROP TABLE author;
DROP TABLE publisher;
DROP TABLE book;
DROP TABLE quote;

CREATE TABLE IF NOT EXISTS author(
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    display_name        TEXT NOT NULL,
    full_name           TEXT NOT NULL,
    living_years        TEXT, -- TODO: IMPLEMENT
    biography           TEXT
);

CREATE TABLE IF NOT EXISTS publisher(
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    name                TEXT NOT NULL
);

-- CREATE TABLE IF NOT EXISTS alternate_publisher();

CREATE TABLE IF NOT EXISTS book(
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    year                INTEGER,
    title               TEXT NOT NULL,
    author_id           INTEGER  NOT NULL, 
    publisher_id        INTEGER  NOT NULL, 
    edition             INTEGER,
    description         TEXT, -- TODO: ADD OTHER STUFF?
    FOREIGN KEY(author_id) REFERENCES author(id),
    FOREIGN KEY(publisher_id) REFERENCES publisher(id)
);

CREATE TABLE IF NOT EXISTS quote(
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    author_id           INTEGER NOT NULL,
    quote               TEXT NOT NULL,
    year                INTEGER
);

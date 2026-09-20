

CREATE TABLE Users (
    id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,
    password_hash TEXT
);

CREATE TABLE Posts (
    id INTEGER PRIMARY KEY,
    title TEXT,
    poster INTEGER,
    post_date DATETIME,
    image_data BLOB,
    image_format TEXT,
    image_width INTEGER, 
    image_height INTEGER
);

CREATE TABLE Tags (
    id INTEGER PRIMARY KEY,
    tag_name TEXT
);

CREATE TABLE TagMap (
    tag_id TEXT,
    image_id INTEGER
);

CREATE TABLE Comments (
    id INTEGER PRIMARY KEY,
    post_id INTEGER,
    commenter_id INTEGER,
    comment_date DATETIME,
    comment_data TEXT
);



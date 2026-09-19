

CREATE TABLE Users (
    id INTEGER PRIMARY KEY,
    user_name TEXT UNIQUE,
    password_hash TEXT
);

CREATE TABLE Posts (
    id INTEGER PRIMARY KEY,
    poster INTEGER,
    post_date DATETIME,
    image_data BLOB
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
    comment_date DATETIME,
    comment_data TEXT
);



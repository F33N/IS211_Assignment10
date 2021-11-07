CREATE TABLE Artist(
	id INTEGER PRIMARY KEY,
    artist_name TEXT
);

CREATE TABLE Albulm(
	id INTEGER PRIMARY KEY,
    album_name TEXT,
    FOREIGN KEY (artist_id)  REFERENCES Artist(id)
);

CREATE TABLE Song(
	id INTEGER PRIMARY KEY,
    song_name TEXT,
    track_number INTEGER,
    duration double,
    FOREIGN KEY (album_id) REFERENCES Album(id)
);
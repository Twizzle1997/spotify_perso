CREATE TABLE IF NOT EXISTS "album"
(
    [album_id] NVARCHAR(160) PRIMARY KEY NOT NULL,
    [name] NVARCHAR(160)  NOT NULL,
    [release_date] DATE  NOT NULL,
    [total_track] INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS "artist"
(
    [artist_id] NVARCHAR(160) PRIMARY KEY NOT NULL,
    [name] NVARCHAR(160) NOT NULL
);
CREATE TABLE IF NOT EXISTS "playlist"
(
    [playlist_id] NVARCHAR(160) PRIMARY KEY NOT NULL,
    [name] NVARCHAR(160) NOT NULL
);

CREATE TABLE IF NOT EXISTS "track"
(
    [track_id] NVARCHAR(160) PRIMARY KEY NOT NULL,
    [name] NVARCHAR(160)  NOT NULL,
    [duration] INTEGER,
    [popularity] INTEGER  NOT NULL,
    [track_number] INTEGER,
	[album_id] NVARCHAR(160),
    FOREIGN KEY ([album_id]) REFERENCES "album" ([album_id]) 
);

CREATE TABLE IF NOT EXISTS "track_features"
(
    [feature_id] INTEGER PRIMARY KEY AUTOINCREMENT,
    [danceability] DECIMAL,
	[energy] DECIMAL,
    [key_track] INTEGER,
    [loudness] DECIMAL,
    [speechiness] DECIMAL,
    [acousticness] DECIMAL,
	[instrumentalness] DECIMAL,
	[liveness] DECIMAL,
	[valence] DECIMAL,
	[tempo] DECIMAL,
	[time_signature] DECIMAL,
	[track_id] NVARCHAR(160),
    FOREIGN KEY ([track_id]) REFERENCES "track" ([track_id]) 
);

CREATE TABLE IF NOT EXISTS "track_playlist"
(
    [playlist_id] NVARCHAR(160) NOT NULL,
    [track_id] NVARCHAR(160)  NOT NULL,
    CONSTRAINT [PK_trackplaylist] PRIMARY KEY  ([playlist_id], [track_id]),
    FOREIGN KEY ([playlist_id]) REFERENCES "playlist" ([playlist_id]),
    FOREIGN KEY ([track_id]) REFERENCES "track" ([track_id])
);

CREATE TABLE IF NOT EXISTS "track_artist"
(
    [artist_id] NVARCHAR(160) NOT NULL,
    [track_id] NVARCHAR(160)  NOT NULL,
    CONSTRAINT [PK_trackartist] PRIMARY KEY  ([artist_id], [track_id]),
    FOREIGN KEY ([artist_id]) REFERENCES "artist" ([artist_id]),
    FOREIGN KEY ([track_id]) REFERENCES "track" ([track_id])
);





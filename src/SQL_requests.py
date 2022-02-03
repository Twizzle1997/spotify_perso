CREATE_PLAYLIST = """CREATE TABLE IF NOT EXISTS playlist (
    id          VARCHAR(22) NOT NULL PRIMARY KEY
  ,name         VARCHAR(50) NOT NULL
  ,total_tracks INTEGER  NOT NULL
  ,owner_id     VARCHAR(25) NOT NULL
  ,href         VARCHAR(60) NOT NULL
);"""

CREATE_TRACK_FEATURES = """CREATE TABLE IF NOT EXISTS track_features(
   id               VARCHAR(22) NOT NULL PRIMARY KEY
  ,danceability     NUMERIC(6,4) NOT NULL
  ,energy           NUMERIC(7,5) NOT NULL
  ,key              INTEGER  NOT NULL
  ,loudness         NUMERIC(7,3) NOT NULL
  ,mode             BIT  NOT NULL
  ,speechiness      NUMERIC(6,4) NOT NULL
  ,acousticness     NUMERIC(8,6) NOT NULL
  ,instrumentalness NUMERIC(11,6) NOT NULL
  ,liveness         NUMERIC(6,4) NOT NULL
  ,valence          NUMERIC(6,4) NOT NULL
  ,tempo            NUMERIC(7,3) NOT NULL
  ,duration_ms      INTEGER  NOT NULL
  ,time_signature   INTEGER  NOT NULL
);"""

CREATE_TRACK = """CREATE TABLE IF NOT EXISTS track(
   id         VARCHAR(22) NOT NULL PRIMARY KEY
  ,name       VARCHAR(255) NOT NULL
  ,artist     VARCHAR(255) NOT NULL
  ,year       INTEGER NOT NULL
  ,album      VARCHAR(255) NOT NULL
  ,album_img  VARCHAR(100)
  ,duration   INTEGER  NOT NULL
  ,explicit   BOOLEAN NOT NULL
  ,popularity INTEGER  NOT NULL
);"""

CREATE_CONTAINS = """CREATE TABLE IF NOT EXISTS contains(
    playlist_id VARCHAR(22) NOT NULL references playlist(id),
    track_id  VARCHAR(22) NOT NULL references track_features(id),
    PRIMARY KEY (playlist_id, track_id)
);"""

INSERT_PLAYLISTS = """INSERT OR IGNORE INTO playlist(id,name,total_tracks,owner_id,href) VALUES (?,?,?,?,?);"""

INSERT_TRACKS_FEATURES = """INSERT OR IGNORE INTO track_features(id,danceability,energy,key,loudness,mode,speechiness,acousticness,instrumentalness,liveness,valence,tempo,duration_ms,time_signature) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?);"""

INSERT_TRACKS = """INSERT OR IGNORE INTO track(id,name,artist,year,album,album_img,duration,explicit,popularity) VALUES (?,?,?,?,?,?,?,?,?);"""

INSERT_CONTAINS = """INSERT OR IGNORE INTO contains(playlist_id, track_id) VALUES (?,?);"""

SELECT_PLAYLIST = """SELECT id, danceability, energy, key, loudness, mode, speechiness, acousticness, instrumentalness, liveness, valence, tempo, duration_ms, time_signature 
    FROM track_features 
    LEFT JOIN contains 
    ON track_features.id = contains.track_id 
    WHERE contains.playlist_id ="""

SELECT_PLAYLIST_TITLES = """SELECT id, name, album_img FROM track LEFT JOIN contains ON track.id = contains.track_id WHERE contains.playlist_id ="""

SELECT_TRACKS_TITLES = """SELECT id, name, album_img FROM track"""

SELECT_TRACKS_FEATURES = """SELECT * FROM track_features"""

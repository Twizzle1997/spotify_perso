CREATE_PLAYLISTS = """CREATE TABLE IF NOT EXISTS playlists (
    id          VARCHAR(22) NOT NULL PRIMARY KEY
  ,name         VARCHAR(50) NOT NULL
  ,total_tracks INTEGER  NOT NULL
  ,owner_id     VARCHAR(25) NOT NULL
  ,href         VARCHAR(60) NOT NULL
  ,tracks       VARCHAR(2600) NOT NULL
);"""

CREATE_TRACKS = """CREATE TABLE IF NOT EXISTS tracks(
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
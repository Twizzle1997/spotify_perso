"""
This file contains classes and functionalities that manipulate and predict
popularity of a track
@author: Audrey
"""
SQL_GET_TRACKS = """SELECT track_id, name
FROM track"""

SQL_GET_POPULARITY = """SELECT popularity
        FROM track"""

SQL_GET_FEATURES = """SELECT duration,
        danceability,
        energy,
        key_track,
        loudness,
        speechiness,
        acousticness,
        liveness,
        valence,
        tempo,
        time_signature
        FROM tracks
        """

SQL_GET_TEST_CHARACTERISTICS = """SELECT duration,
        danceability,
        energy,
        key_track,
        loudness,
        speechiness,
        acousticness,
        liveness,
        valence,
        tempo,
        time_signature
        FROM tracks
        WHERE track_id='{}'"""

SQL_GET_TEST_POPULARITY = """SELECT popularity
        FROM tracks
        WHERE track_id='{}'"""
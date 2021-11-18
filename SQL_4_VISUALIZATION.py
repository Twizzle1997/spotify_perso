"""
This file contains SQL queries for required business functionalities
@author : Diem BUI
@Date : 30/06/2020: Add 4 SQL queries as first version
@Date : 06/07/2020: Update SQL_COUNT_SONGS_BY_PLAYLIST because of database change

"""

SQL_COUNT_SONGS_BY_ARTIST = """
            select at.name,  count(*) as 'count_song'
            from artist at
            join track_artist ta on at.artist_id = ta.artist_id
            join tracks tr on tr.track_id = ta.track_id
            group by at.name
            order by count_song desc
         --   limit 35
"""

SQL_AVG_DURATION_BY_SONG = """SELECT round (((avg(duration) / 1000)/60),2) as avg_duration,
                                     round((cast(max(duration)as float)/1000/60),2) as MAX_Duration,
                                     round((cast(min(duration)as float)/1000/60),2) as MIN_Duration
                              FROM tracks;
"""

SQL_COUNT_SONGS_BY_PLAYLIST = """
            SELECT t.name, count(*) AS count_playlist
            FROM TRACK t
            JOIN TRACK_PLAYLIST tp ON tp.track_id = t.track_id
            JOIN PLAYLIST p ON p.playlist_id = tp.playlist_id
            GROUP BY t.name
            HAVING count_playlist >= 2
            ORDER BY count_playlist DESC
         --   LIMIT 35
"""

SQL_COUNT_NUMBER_OF_SONGS_IN_PLAYLIST = """
            SELECT COUNT(*) AS count_songs
            FROM (
               SELECT t.name, count(*) AS count_playlist
               FROM TRACK t 
               JOIN TRACK_PLAYLIST tp ON tp.track_id = t.track_id
               JOIN PLAYLIST p ON p.playlist_id = tp.playlist_id
               GROUP BY t.name
               HAVING count_playlist >= 2
               ORDER BY count_playlist DESC
            )
"""

SQL_COUNT_SONGS_BY_BPM = """ SELECT CASE
                            WHEN  t.tempo BETWEEN 40 AND 60 THEN 'Largo'
                            WHEN  t.tempo BETWEEN 60 AND 66 THEN 'Larghetto'
                            WHEN  t.tempo BETWEEN 66 AND 76 THEN 'Adagio'
                            WHEN  t.tempo BETWEEN 76 AND 108 THEN 'Andante'
                            WHEN  t.tempo BETWEEN 108 AND 120 THEN 'Moderato'
                            WHEN  t.tempo BETWEEN 120 AND 168 THEN 'Allegro'
                            WHEN  t.tempo BETWEEN 168 AND 200 THEN 'Presto'
                            ELSE 'Prestissimo '
                            END AS 'bpm'   , count(*) as 'count_song'
                            FROM track_features t
                            GROUP BY bpm
                            ORDER by count_song desc 
                        """

SQL_SELECT_INTENSITY_ENERGY = """
                           SELECT loudness,  energy
                           FROM track_features
                           ORDER BY loudness,  energy
"""

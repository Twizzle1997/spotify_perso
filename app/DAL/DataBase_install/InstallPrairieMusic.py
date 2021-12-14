import sqlite3
from DAL.connect import db_connect 
conn = db_connect('DAL/DataBase_install/Prairie-Musique.db')
c = conn.cursor()
request =[]
request = ['DAL/DataBase_install/Install_prairie_music.sql',
           'DAL/DataBase_install/album.sql', 
           'DAL/DataBase_install/artist.sql',
           'DAL/DataBase_install/playlist.sql',
           'DAL/DataBase_install/track.sql',
           'DAL/DataBase_install/track_features.sql',
           'DAL/DataBase_install/tracks.sql',
           'DAL/DataBase_install/track_playlist.sql',
           'DAL/DataBase_install/track_artist.sql']

for reqst in request:
    print(reqst)
    query = open(reqst, 'r', encoding='utf-8')
    c.executescript(query.read())
    conn.commit()
    query.close()
c.close()
conn.close()
print("base de donnée installée")
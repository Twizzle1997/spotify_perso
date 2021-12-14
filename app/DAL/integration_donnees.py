""" fichier principal qui exécute toutes les requêtes et
    traitements à la génération des fichiers d'insertion SQL
"""

import json
import requests
import DAL.ParseXml as ParseXml
import DAL.Build_SQL_Data as Build_SQL_Data

xmlfile = ParseXml.get_xml("https://dlsandboxweu002.blob.core.windows.net/spotify?comp=list")
links_top, links_feature = ParseXml.get_url(xmlfile)

# ********** Récupération des données à exploiter **********

all_top_songs = []
# ajoute directement chaque son des différents top 50 dans all_top_songs
for link_top in links_top:
    try:
        liste_sons = requests.get(link_top).json()['items']
        for son in liste_sons:
            all_top_songs.append(son)
    except KeyError:
        pass

all_features = []
# ajoute tous les features des sons disponibles dans all_features
for link_feature in links_feature:
    try:
        liste_feature = requests.get(link_feature).json()["audio_features"]
        for feature in liste_feature:
            all_features.append(feature)
    except KeyError:
        pass
    except json.JSONDecodeError:
        pass

# ********** Preparation des tables pour les exploiter **********

# les tables SQL sont
PLAYLIST = "playlist"
ARTIST = "artist"
TRACK = "track"
ALBUM = "album"
FEATURES = "track_features"
TRACK_ARTIST = "track_artist"
TRACK_PLAYLIST = "track_playlist"

playlists_table = []
for url in links_top: #Données de la table playlist
    try:
        # recuperation dans une string de ce type: https://api.spotify.com/v1/playlists/37i9dQZEVXbJiZcmkrIHGU/tracks?offset=0&limit=100
        href = requests.get(url).json()['href']
        playlist_id = href[href.find('playlists/') + len('playlists/'):href.find('/track')]

        # recuperation dans une string de ce type: https://dlsandboxweu002.blob.core.windows.net/spotify/raw/spotify/playlists/2020/06/23/top_50_allemagne.json
        playlist_name = url[url.find('top_50'):url.find('.json')] # recupère le texte entre top_50 et .json

        playlists_table.append({
            'playlist_id': playlist_id,
            'name': playlist_name
        })
    except KeyError:
        pass
Build_SQL_Data.BuildSQLFile(PLAYLIST, playlists_table)

track_table = []
for song in all_top_songs:
    track_table.append({
        "track_id": song["track"]["id"],
        "name": song["track"]["name"],
        "duration": song["track"]["duration_ms"],
        "popularity": song["track"]["popularity"],
        "track_number": song["track"]["track_number"],
        "album_id": song["track"]["album"]["id"]
    })
Build_SQL_Data.BuildSQLFile(TRACK, track_table)

album_table = []
for song in all_top_songs:
    album_table.append({
        "album_id": song["track"]["album"]["id"],
        "name": song["track"]["album"]["name"],
        "release_date": song["track"]["album"]["release_date"],
        "total_track": song["track"]["album"]["total_tracks"]
    })
Build_SQL_Data.BuildSQLFile(ALBUM, album_table)

artist_table = []
for song in all_top_songs:
    for artist in song["track"]["artists"]:
        artist_table.append({
            "artist_id": artist["id"],
            "name": artist["name"]
        })
Build_SQL_Data.BuildSQLFile(ARTIST, artist_table)

features_table = []
for feature in all_features:
    features_table.append({
        "danceability": feature["danceability"],
        "energy": feature["energy"],
        "key_track": feature["key"],
        "loudness": feature["loudness"],
        "speechiness": feature["speechiness"],
        "acousticness": feature["acousticness"],
        "instrumentalness": feature["instrumentalness"],
        "liveness": feature["liveness"],
        "valence": feature["valence"],
        "tempo": feature["tempo"],
        "time_signature": feature["time_signature"],
        "track_id": feature["id"]
    })
Build_SQL_Data.BuildSQLFile(FEATURES, features_table)

track_playlist_table = []
for link_top in links_top:
    try:
        playlist = requests.get(link_top).json()
        href = playlist['href']

        playlist_id = href[href.find('playlists/') + len('playlists/'):href.find('/track')]
        liste_sons = playlist['items']
        for song in liste_sons:
            track_playlist_table.append({
                "playlist_id": playlist_id,
                "track_id": song["track"]["id"]
            })
    except KeyError:
        pass
Build_SQL_Data.BuildSQLFile(TRACK_PLAYLIST, track_playlist_table)

track_artist_table = []
for song in all_top_songs:
    for artist in song["track"]["artists"]:
        track_artist_table.append({
            "track_id": song["track"]["id"],
            "artist_id": artist["id"]
        })
Build_SQL_Data.BuildSQLFile(TRACK_ARTIST, track_artist_table)
print("fichiers sql uploades")

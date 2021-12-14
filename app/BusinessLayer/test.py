from bottle import static_file, run
import pandas as pd
import sqlite3
from matplotlib import pyplot as plt 
from matplotlib.pyplot import savefig
import pathlib
import os
import seaborn as sns
sns.set_style("whitegrid")
sns.set_palette("Set2")

conn = sqlite3.connect("MDB/Prairie-Musique.db")

# Nombre de chansons par artiste
def nb_tracks_by_artist():
    df = pd.read_sql_query("\
        SELECT a.name, COUNT(track_id) as nbTracks \
        FROM artist a \
        JOIN track_artist t ON a.id = t.artist_id \
        GROUP BY a.id", conn)
    print(df)
    
    data = {"Count" : [5, 10, 20, 22]}
    df1 = pd.DataFrame(data = data
                    , columns = ["Count"]
                    , index = ["Artist 1", "Artis 2", "Artist 3", "Artist 4"] )

    df1.plot(kind = "bar", figsize = (3, 2))
    plt.legend("")
    plt.ylabel("Count")

    print(os.getcwd())
    current_path = os.getcwd()
    fig_path = current_path + os.sep + "static" + os.sep + "assets" + os.sep + "img" + os.sep + "plot.png"
    print(fig_path)
    plt.savefig(fig_path, bbox_inches='tight', dpi=150)
#   plt.show()
    print(current_path)
    return static_file("plot.png", root = current_path + os.sep + "static" + os.sep + "assets" + os.sep + "img")


# Temps moyen des morceaux
def average_track_time():
    df = pd.read_sql_query("SELECT AVG(duration) FROM track", conn)
    return df


# Nombre de morceaux qui sont dans plusieurs playlists
def tracks_in_many_playlists():
    df = pd.read_sql_query("SELECT track_id, COUNT(playlist_id) FROM track_playlist GROUP BY track_id HAVING COUNT(playlist_id) > 1", conn)
    return df


# Nombre de morceaux par bpm
def track_by_bpm(): 
    df = pd.read_sql_query("SELECT tempo, COUNT(id) FROM track GROUP BY tempo", conn)
    return df


# Analyser et afficher la relation entre l’énergie et l’intensité
def energy_intensity():
    df = pd.read_sql_query("SELECT * FROM track", conn)
    df.describe()

# Prédire la popularité en fonction des caractéristiques d’un morceau (libre choix)
# BONUS : analyser les images d'une pochette d'album pour en extraire les objets (ressource en cours de construction)


if __name__ == "__main__":
    # execute only if run as a script
    run(host='localhost', port=8080, debug=True)

"""
This file contains classes and functionalities that manipulate and visualizate
the data
@author: Diem BUI
@Date : 30/06/2020: Created DashBoard class and tested its functions
@Date : 01/07/2020: Return svg file name at the end of function's execution

"""
"""
Data Manipulation tools
"""
import pandas as pd
from pandas import read_sql
from pandas import read_sql_query

"""
Data Visualization Tools
"""
import seaborn as sns
import matplotlib
sns.set_style("whitegrid")
sns.set_palette("Set2")
from matplotlib import pyplot as plt
from matplotlib.pyplot import savefig
"""
Database sqlite connection
"""
import sqlite3

"""
System
"""
import os
"""
SQL queries
"""
from SQL_4_VISUALIZATION import SQL_COUNT_SONGS_BY_ARTIST
from SQL_4_VISUALIZATION import SQL_COUNT_SONGS_BY_BPM
from SQL_4_VISUALIZATION import SQL_AVG_DURATION_BY_SONG
from SQL_4_VISUALIZATION import SQL_COUNT_SONGS_BY_PLAYLIST
from SQL_4_VISUALIZATION import SQL_SELECT_INTENSITY_ENERGY
from SQL_4_PREDICTION import SQL_GET_TRACKS, SQL_GET_TEST_POPULARITY
"""
svg file names defined
"""
from SVG_FILE_NAME import FILE_NAME_COUNT_SONGS_BY_ARTIST
from SVG_FILE_NAME import FILE_NAME_COUNT_SONGS_BY_BPM
from SVG_FILE_NAME import FILE_NAME_COUNT_SONGS_BY_PLAYPLIST
from SVG_FILE_NAME import FILE_NAME_REGRESSION_INTENSITY_ENERGY
from SVG_FILE_NAME import SVG_LARGE_SIZE_WIDTH
from SVG_FILE_NAME import SVG_LARGE_SIZE_HEIGTH
from SVG_FILE_NAME import SVG_MEDIUM_SIZE_WIDTH
from SVG_FILE_NAME import SVG_MEDIUM_SIZE_HEIGTH
from SVG_FILE_NAME import SVG_SMALL_SIZE_HEIGTH
from SVG_FILE_NAME import SVG_SMALL_SIZE_WIDTH
"""
SQL queries
"""
from SQL_4_VISUALIZATION import SQL_COUNT_SONGS_BY_ARTIST
from SQL_4_VISUALIZATION import SQL_COUNT_SONGS_BY_BPM
from SQL_4_VISUALIZATION import SQL_AVG_DURATION_BY_SONG
from SQL_4_VISUALIZATION import SQL_COUNT_SONGS_BY_PLAYLIST
from SQL_4_VISUALIZATION import SQL_SELECT_INTENSITY_ENERGY
from SQL_4_VISUALIZATION import SQL_COUNT_NUMBER_OF_SONGS_IN_PLAYLIST
"""
The file path of database file
"""
SQLITE_FILE =  os.getcwd() + os.sep + "DAL" +  os.sep + "Database_install" +  os.sep + "Prairie-Musique.db"
"""
The path to keep the images
"""
IMAGE_PATH = os.getcwd() + os.sep + "static" + os.sep + "assets" + os.sep + "img" + os.sep


class DashBoard:

    def __init__(self, dbFile=SQLITE_FILE):
        self.dbFile = dbFile
        self.conn = self.__connection__()
        self.conn.text_factory = lambda b: b.decode(errors='ignore')
        print("DashBoard class is initiated")

    def __connection__(self):
        """
        This function will return SQL Lite connection
        @ Agr:
            - sqlFile : string : name of database file
        """
        conn = sqlite3.connect(self.dbFile)
        return conn

    def __saveimage__(self):
        return None

    def get_data(self, sql):
        """
        - Connect to the database and query the data
        - the data is returned in pandas dataframe
        """
        return pd.read_sql_query(sql, self.conn)

    def count_songs_by_artist(self):
        """
        Count the numer of songs written by artists and export the data into SVG
        Return the svg's file name
        """
        count_songs = self.get_data(SQL_COUNT_SONGS_BY_ARTIST)
        """
        sns_plot = sns.barplot(x= "name", y= "count_song", data =count_songs, size=5)
        fig = sns_plot.get_figure()
        fig.savefig(IMAGE_PATH + FILE_NAME_COUNT_SONGS_BY_ARTIST)
        """
        count_songs.set_index(['name']).plot(kind="bar", figsize=(SVG_LARGE_SIZE_WIDTH, SVG_LARGE_SIZE_HEIGTH))
        plt.title("The Number of Songs By Artist")
        plt.legend("")
        plt.ylabel("Count")
        plt.xlabel("")
        plt.xticks(count_songs.index.values, rotation=45)
        savefig(IMAGE_PATH + FILE_NAME_COUNT_SONGS_BY_ARTIST)
        return FILE_NAME_COUNT_SONGS_BY_ARTIST

    def count_songs_by_artist_table_version(self):
        return self.get_data(SQL_COUNT_SONGS_BY_ARTIST).to_numpy()

    def count_songs_by_bpm(self):
        """
        Count the number of songs by BPM and export the data into SVG
        Return svg file name

        """
        count_songs = self.get_data(SQL_COUNT_SONGS_BY_BPM)
        count_songs.set_index(['bpm']).plot(kind ="barh",  figsize=(SVG_SMALL_SIZE_WIDTH, SVG_SMALL_SIZE_HEIGTH))
        plt.title("Number of Songs by BPM")
        plt.legend("")
        plt.ylabel("")
        plt.xlabel("Count")
        savefig(IMAGE_PATH + FILE_NAME_COUNT_SONGS_BY_BPM)
        return FILE_NAME_COUNT_SONGS_BY_BPM

    def avg_duration_songs(self):
        """
        Return the average duration of songs
        """
        avg_duration = self.get_data(SQL_AVG_DURATION_BY_SONG)
        print("avg_duration : ", avg_duration)
        return avg_duration.values

    def count_nb_songs_in_playlists(self):
        """
        Return the the number of songs added in more than 2 playlists
        """
        count_songs = self.get_data(SQL_COUNT_NUMBER_OF_SONGS_IN_PLAYLIST)
        print("the number of songs added into more than 2 playlists:", count_songs)
        return str(count_songs.values[0][0])

    def count_songs_by_playlist(self):
        """
        Count the number of songs added into playlist and export the data into SVG
        Return the svg file name
        """
        count_songs_playlist = self.get_data(SQL_COUNT_SONGS_BY_PLAYLIST)
        """
        sns_plot = sns.barplot(x = 'name', y = 'count_playlist', data = count_songs_playlist)
        fig = sns_plot.get_figure()
        fig. savefig(IMAGE_PATH + FILE_NAME_COUNT_SONGS_BY_PLAYPLIST, figsize  = (SVG_LARGE_SIZE_WIDTH, SVG_LARGE_SIZE_HEIGTH))
        """
        count_songs_playlist.set_index(['name']).plot(kind="bar", figsize=(SVG_MEDIUM_SIZE_WIDTH, SVG_MEDIUM_SIZE_HEIGTH))
        plt.title("Number of Songs by Playlist")
        plt.legend("")
        plt.ylabel("Count")
        plt.xlabel("")
        savefig(IMAGE_PATH + FILE_NAME_COUNT_SONGS_BY_PLAYPLIST)
        return FILE_NAME_COUNT_SONGS_BY_PLAYPLIST

    def regression_intensity_energy(self):
        intensity_energy = self.get_data(SQL_SELECT_INTENSITY_ENERGY)
        plt.figure(figsize=(SVG_SMALL_SIZE_WIDTH, SVG_SMALL_SIZE_HEIGTH))
        sns.pairplot(intensity_energy)
        plt.savefig(IMAGE_PATH + FILE_NAME_REGRESSION_INTENSITY_ENERGY)
        return FILE_NAME_REGRESSION_INTENSITY_ENERGY

    def get_tracks(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        tracks = self.get_data(SQL_GET_TRACKS)
        return tracks

    def get_pop(self, id):
        """[summary]
        """
        pop = self.get_data(SQL_GET_TEST_POPULARITY.format(id))

        for item in pop.itertuples():
            return item.popularity
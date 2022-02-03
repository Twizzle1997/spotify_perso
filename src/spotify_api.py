import spotipy
import credentials as cr
import pandas as pd
import ast
from spotipy.oauth2 import SpotifyClientCredentials

class Spotify_api():

    def __init__(self):

        # Credentials
        self.client_id = cr.CLIENT_ID
        self.client_secret = cr.CLIENT_SECRET
        self.auth = cr.TOKEN

        self.client_credentials_manager = SpotifyClientCredentials(client_id=self.client_id, client_secret=self.client_secret)
        self.sp = spotipy.Spotify(client_credentials_manager=self.client_credentials_manager, auth=self.auth)
        

    def get_user_playlists(self):
        """
        Get the current user's spotify playlists with a limit at 50.
        ****
        returns: pandas.DataFrame playlists
        """

        # Get json playlists using spotipy api
        playlistsJson = self.sp.current_user_playlists(limit=50, offset=0)

        playlists = {'id': [], 'name': [], 'total_tracks': [], 'owner_id': [], 'href': []}
        
        for i, playlist in enumerate(playlistsJson['items']):
            playlists['id'].append(playlist['id'])
            playlists['name'].append(playlist['name'])
            playlists['total_tracks'].append(playlist['tracks']['total'])
            playlists['owner_id'].append(playlist['owner']['id'])
            playlists['href'].append(playlist['href'])

        print('Found playlists : ', i+1)

        return pd.DataFrame.from_dict(playlists).set_index('id')


    def get_playlist_tracks(self, playlist_id):
        """
        Get the selected playlist's tracks using its id with a maximum of 100.
        ****
        returns: list of tracks of the playlist
        """

        playlistJson = self.sp.playlist(playlist_id)

        # Create the list to initialize the dataframe
        tracks_list = []

        for _, track in enumerate(playlistJson['tracks']['items']):
            tracks_list.append(track['track']['id'])

        return tracks_list


    def get_playlists_with_tracks(self):
        """
        Set the 100 first tracks ids to the user's playlists
        ****
        returns: dataframe with playlists and related tracks ids
        """
        playlists = self.get_user_playlists()

        playlists_tracks = {'id': [], 'tracks': []}

        for _, playlist in playlists.T.iteritems():
            playlists_tracks['id'].append(playlist.name)
            playlists_tracks['tracks'].append(self.get_playlist_tracks(playlist.name))


        df_to_merge = pd.DataFrame.from_dict(playlists_tracks).set_index('id')

        return playlists.merge(df_to_merge, left_index=True, right_index=True)


    def get_features(self, track_id):
        """
        Get the selected track's features.
        ****
        returns: dict of track features"""

        track_features = self.sp.audio_features(track_id)    
        features = {}


        for _, feature in enumerate(track_features):
            features['id'] = feature['id']
            features['danceability'] = feature['danceability']
            features['energy'] = feature['energy']
            features['key'] = feature['key']
            features['loudness'] = feature['loudness']
            features['mode'] = feature['mode']
            features['speechiness'] = feature['speechiness']
            features['acousticness'] = feature['acousticness']
            features['instrumentalness'] = feature['instrumentalness']
            features['liveness'] = feature['liveness']
            features['valence'] = feature['valence']
            features['tempo'] = feature['tempo']
            features['duration_ms'] = feature['duration_ms']
            features['time_signature'] = feature['time_signature']

        return features


    def get_playlist_features(self, playlist_df):
        """
        Get a dataframe with the features of the 100 firsts tracks of the given playlist dataframe.
        ****
        returns: dataframe of the playlist's tracks' features.
        """

        features = {'id': [], 'danceability': [], 'energy': [], 'key': [], 'loudness': [], 'mode': [], 'speechiness': [], 'acousticness': [], 
                    'instrumentalness': [], 'liveness': [], 'valence': [], 'tempo': [], 'duration_ms': [], 'time_signature': []}

        # Iter throught playlists
        for _, playlist in playlist_df.T.iteritems():
            print(playlist['name'])
            # Iter throught tracks ids of the playlist
            for track_id in playlist['tracks']:
            #for track_id in ast.literal_eval(playlist['tracks']):

                track_features = self.get_features(track_id)

                # Append tracks features to the features dict 
                for key in features.keys():
                    features[key].append(track_features[key])


        return pd.DataFrame.from_dict(features).set_index('id')


    def get_tracks(self, features_dataframe):

        track_ids = []
        tracks = {'id':[], 'name':[], 'artist':[], 'year':[], 'album':[], 'album_img':[], 'duration':[], 'explicit':[], 'popularity':[] }

        # Select all the tracks ids of the dataframe
        for _, track in features_dataframe.T.iteritems():
            track_ids.append(track.name)


        for id in track_ids:
            trackJson = self.sp.track(id)

            list_artists = []
            
            for artist in trackJson['artists']:
                list_artists.append(artist['name'])

            tracks['id'].append(trackJson['id'])
            tracks['name'].append(trackJson['name'])
            tracks['artist'].append(list_artists)
            tracks['year'].append(trackJson['album']['release_date'][:4])
            tracks['album'].append(trackJson['album']['name'])
            tracks['album_img'].append(trackJson['album']['images'][1]['url'])
            tracks['duration'].append(trackJson['duration_ms'])
            tracks['explicit'].append(trackJson['explicit'])
            tracks['popularity'].append(trackJson['popularity'])
    
        return pd.DataFrame.from_dict(tracks).set_index('id')

    def get_contains(self, playlist_df):

        contains = {'playlist_id': [], 'track_id': []}

        for i, playlist in playlist_df.iterrows():
            for track_id in ast.literal_eval(playlist['tracks']):
                contains['playlist_id'].append(playlist.id)
                contains['track_id'].append(track_id)

        playlist_df.drop(columns=['tracks'], inplace=True)
        
        return pd.DataFrame.from_dict(contains).reset_index(drop=True)

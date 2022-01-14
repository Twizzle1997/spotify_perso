from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler
from skimage import io
import pandas as pd
import matplotlib.pyplot as plt

class Recommendation():

    def process_data(self, track_features):
        track_features_copy = track_features.copy()

        mode_OHE = pd.get_dummies(track_features_copy['mode'], prefix="mode")
        key_OHE = pd.get_dummies(track_features_copy['key'], prefix="key")
        time_signature_OHE = pd.get_dummies(track_features_copy['time_signature'], prefix="time_signature")

        scaled_features = MinMaxScaler().fit_transform([
        track_features_copy['acousticness'].values,
        track_features_copy['danceability'].values,
        track_features_copy['duration_ms'].values,
        track_features_copy['energy'].values,
        track_features_copy['instrumentalness'].values,
        track_features_copy['liveness'].values,
        track_features_copy['loudness'].values,
        track_features_copy['speechiness'].values,
        track_features_copy['tempo'].values,
        track_features_copy['valence'].values,
        ])

        #Storing the transformed column vectors into our dataframe
        track_features_copy[['acousticness','danceability','duration_ms','energy','instrumentalness','liveness','loudness','speechiness','tempo','valence']] = scaled_features.T

        # #discarding the categorical and unnecessary features 
        track_features_copy = track_features_copy.drop('key',axis = 1)
        track_features_copy = track_features_copy.drop('mode', axis = 1)
        track_features_copy = track_features_copy.drop('time_signature', axis = 1)

        #Appending the OHE columns of the categorical features
        track_features_copy = track_features_copy.join(mode_OHE)
        track_features_copy = track_features_copy.join(key_OHE)
        track_features_copy = track_features_copy.join(time_signature_OHE)

        track_features_copy.head()

        return track_features_copy

    def generate_playlist_vector(self, track_features, playlist):
    
        features_playlist = track_features[track_features.index.isin(playlist.index.values)]
        spotify_features_nonplaylist = track_features[~track_features.index.isin(playlist.index.values)]
        
        return features_playlist.sum(axis = 0), spotify_features_nonplaylist

        
    def generate_recommendation(self, track_features, playlist, nonplaylist, track_infos):

        non_playlist = track_features[track_features.index.isin(nonplaylist.index.values)]
        non_playlist['sim'] = cosine_similarity(nonplaylist.values, playlist.values.reshape(1, -1))[:,0]

        recommendation = non_playlist.sort_values('sim',ascending = False).head(10)
        recommendation = recommendation.merge(track_infos, left_index=True, right_index=True)
        
        return recommendation

    def visualize_cover(self, playlist_df):
        temp = playlist_df['album_img'].values
        plt.figure(figsize=(15,int(0.625 * len(temp))) , facecolor='#8F7C7C')
        columns = 5
        
        for i, url in enumerate(temp):
            plt.subplot(int(len(temp) / columns + 1), int(columns), int(i + 1))

            image = io.imread(url)
            plt.imshow(image)
            plt.xticks([])
            plt.yticks([])
            s=' ' 
            plt.xlabel(s.join(playlist_df['name'].values[i].split(' ')[:4]), fontsize = 11, fontweight='bold')
            plt.tight_layout(h_pad=0.8, w_pad=0)
            plt.subplots_adjust(wspace=None, hspace=None)

        plt.show()
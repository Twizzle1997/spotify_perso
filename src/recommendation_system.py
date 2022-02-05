from sklearn.metrics.pairwise import cosine_similarity
# from sklearn.preprocessing import MinMaxScaler
# from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
from skimage import io
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import credentials as cr
import SQL_requests as rq
from db_connect import Db_connect

db = Db_connect()
data_path = cr.DATA_PATH

class Recommendation():

    def process_data(self, track_features):
        track_features_copy = track_features.copy()

        # Delete the unit digit of the year to get decades
        track_features_copy['decade'] = track_features_copy['year'].apply(lambda x: str(x)[:3])

        # Change duration into minutes
        track_features_copy['duration_min'] = track_features_copy['duration_ms'].apply(lambda x: x/60000)

        mode_dum = pd.get_dummies(track_features_copy['mode'], prefix="mode")
        key_dum = pd.get_dummies(track_features_copy['key'], prefix="key")
        time_signature_dum = pd.get_dummies(track_features_copy['time_signature'], prefix="time_signature")
        year_dum = pd.get_dummies(track_features_copy['decade'], prefix="decade")

        # scaled_features = MinMaxScaler(feature_range=(0, 10)).fit_transform([
        # track_features_copy['acousticness'].values,
        # track_features_copy['danceability'].values,
        # track_features_copy['duration_min'].values,
        # track_features_copy['energy'].values,
        # track_features_copy['instrumentalness'].values,
        # track_features_copy['liveness'].values,
        # track_features_copy['speechiness'].values,
        # track_features_copy['tempo'].values,
        # track_features_copy['valence'].values,
        # track_features_copy['loudness'].values
        # ])

        # track_features_copy[['acousticness','danceability','duration_min','energy','instrumentalness','liveness',
        # 'speechiness','tempo','valence', 'loudness']] = scaled_features.T

        # discarding the categorical and unnecessary features 
        track_features_copy = track_features_copy.drop('key',axis = 1)
        track_features_copy = track_features_copy.drop('mode', axis = 1)
        track_features_copy = track_features_copy.drop('time_signature', axis = 1)
        track_features_copy = track_features_copy.drop('year', axis = 1)
        track_features_copy = track_features_copy.drop('decade', axis = 1)
        track_features_copy = track_features_copy.drop('duration_ms', axis = 1)


        # Appending the dum columns of the categorical features
        track_features_copy = track_features_copy.join(mode_dum)
        track_features_copy = track_features_copy.join(key_dum)
        track_features_copy = track_features_copy.join(time_signature_dum)
        track_features_copy = track_features_copy.join(year_dum)

        track_features_copy.head()

        return track_features_copy

    def generate_playlist_nonplaylist(self, track_features, playlist):
    
        features_playlist = track_features[track_features.index.isin(playlist.index.values)]
        features_nonplaylist = track_features[~track_features.index.isin(playlist.index.values)]
        
        return features_playlist, features_nonplaylist

        
    def get_cosine_similarity(self, features_playlist, features_nonplaylist, track_infos):

        features_playlist_copy = features_playlist.copy()
        features_playlist_copy.sum(axis = 0)

        features_nonplaylist_copy = features_nonplaylist.copy()

        # tfidf_vectorizer = TfidfVectorizer()
        # features_nonplaylist_copy = tfidf_vectorizer.fit_transform(features_nonplaylist_copy)
        # features_playlist_copy = tfidf_vectorizer.transform(features_playlist_copy)
        
        features_nonplaylist_copy['sim'] = features_nonplaylist_copy.apply(lambda x: cosine_similarity(x.values.reshape((1, -1)), features_playlist_copy.values), axis=1)
        features_nonplaylist_copy['sim_mean'] = features_nonplaylist_copy.apply(lambda x: np.mean(x['sim'][0]), axis=1)
        output = features_nonplaylist_copy[['sim', 'sim_mean']].merge(track_infos, left_index=True, right_index=True)

        return output

    def get_recommendations(self, playlist, nonplaylist, track_features, track_titles):

        neighbors = NearestNeighbors(n_neighbors=5, algorithm='auto').fit(nonplaylist)

        distances, predictions = neighbors.kneighbors(playlist, 5, return_distance=True)

        keys = {'key':[], 'distance':[], 'weight':[]}

        for prediction_list, distance_list in zip(predictions, distances):
            for prediction, distance in zip(prediction_list, distance_list):
                index = track_features.iloc[prediction].name
                if index not in keys['key']:
                    keys['key'].append(index)
                    keys['distance'].append(distance)
                    keys['weight'].append(1)
                else : 
                    index_in_list = keys['key'].index(index)
                    keys['weight'][index_in_list] += 1
                    if distance < keys['distance'][index_in_list]: 
                        keys['distance'][index_in_list] = distance

                        # /!\ UTILISER POIDS

        keys_df = pd.DataFrame.from_dict(keys).reset_index(drop=True)
        keys_df = keys_df.sort_values(['weight', 'distance'], ascending=[False, True]).head(10)

        return keys_df.merge(track_titles, left_on='key', right_index=True).set_index('key'), track_features.loc[keys_df.key]


    def get_recommendations_processed(self, playlist, nonplaylist, track_features, track_titles):

        neighbors = NearestNeighbors(n_neighbors=5, algorithm='auto').fit(nonplaylist.values)

        distances, predictions = neighbors.kneighbors(playlist.values, 3, return_distance=True) # Reshape si on vectorise la playlist

        keys = {'key':[], 'distance':[], 'weight':[]}

        for prediction_list, distance_list in zip(predictions, distances):
            for prediction, distance in zip(prediction_list, distance_list):
                index = track_features.iloc[prediction].name
                if index not in keys['key']:
                    keys['key'].append(index)
                    keys['distance'].append(distance)
                    keys['weight'].append(1)
                else : 
                    index_in_list = keys['key'].index(index)
                    keys['weight'][index_in_list] += 1
                    if distance < keys['distance'][index_in_list]: 
                        keys['distance'][index_in_list] = distance

        keys_df = pd.DataFrame.from_dict(keys).reset_index(drop=True)
        keys_df = keys_df.sort_values(['weight', 'distance'], ascending=[False, True]).head(10)

        return keys_df.merge(track_titles, left_on='key', right_index=True).set_index('key'), track_features.loc[keys_df.key]

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

    def knnRecommandation(self, playlist_id):

        # get datas
        db.init_connection()
        playlist_titles = pd.read_sql_query(rq.SELECT_PLAYLIST_TITLES + playlist_id, db.connector).set_index('id')
        track_titles = pd.read_sql_query(rq.SELECT_TRACKS_TITLES, db.connector).set_index('id')
        track_features = pd.read_sql_query(rq.SELECT_TRACKS_FEATURES, db.connector).set_index('id')
        db.close_connection()

        # process datas and generate train / test sets
        track_features_processed = self.process_data(track_features)
        playlist, nonplaylist = self.generate_playlist_nonplaylist(track_features_processed, playlist_titles)

        train_test_dataset = track_features_processed.copy()
        train_test_dataset['playlist'] = train_test_dataset.apply(lambda x: int(x.name in playlist_titles.index), axis=1)

        classifier_data = train_test_dataset.copy()
        classifier_data = classifier_data.sort_values(['playlist'], ascending=False).head(100)

        classifier_target = classifier_data['playlist']

        classifier_data = classifier_data.drop('playlist',axis = 1)

        X_train, X_test, y_train, y_test = train_test_split(classifier_data, classifier_target, test_size=0.3, random_state=42)

        # generate model
        knn = KNeighborsClassifier(n_neighbors=5, algorithm='brute', weights='distance', metric='manhattan')
        knn.fit(X_train, y_train)

        y_pred = knn.predict(X_test)

        print("Accuracy:", metrics.accuracy_score(y_test, y_pred))

        # get recommandations
        recommendation = nonplaylist.copy()

        recommendation['predict'] = recommendation.apply(lambda x: knn.predict([x])[0], axis=1)
        recommendation['proba'] = recommendation.loc[:, recommendation.columns != 'predict'].apply(lambda x: knn.predict_proba([x])[0].max(), axis=1)

        recommendation = recommendation[recommendation['predict']==1]
        recommendation = recommendation.sort_values('proba', ascending=False).head(10)

        recommendation = recommendation.merge(track_titles, left_index=True, right_index=True)

        # vizualise recommandations
        self.visualize_cover(recommendation)
        recommendation = recommendation[['name', 'proba']]
        display(recommendation)

        # add results to the database
        recommendation['playlist'] = playlist_id
        recommendation[['proba', 'playlist']].to_csv(data_path + 'recommendations.csv', encoding='utf-8')
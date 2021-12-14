"""
"""
import numpy as np
import os
import pandas as pd
from sklearn import preprocessing, svm
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import sqlite3
"""
SQL queries
"""
from SQL_4_PREDICTION import SQL_GET_POPULARITY
from SQL_4_PREDICTION import SQL_GET_FEATURES
from SQL_4_PREDICTION import SQL_GET_TEST_CHARACTERISTICS

class PredictLR:

    def get_predictionLR(self, oneId, dbConnection):
        """
        Estimate the probability of being a hit song using the Logical Regression model.

        Args : 
            oneId(str): id of the selected music.
                
        Returns:
            int: y_track, probability estimated of the song.
        """
        # Create features and target tables.
        x = dbConnection.get_data(SQL_GET_FEATURES)
        y = dbConnection.get_data(SQL_GET_POPULARITY)

        # Split the dataset in training and test sets.
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=0)

        # Scale.
        sc = preprocessing.StandardScaler()
        x_train = sc.fit_transform(x_train)
        x_test = sc.transform(x_test)

        # Train the training set using the logistic regression model.
        classifier = LogisticRegression()
        classifier.fit(x_train, y_train)

        # Select the song features.
        x_track = dbConnection.get_data(SQL_GET_TEST_CHARACTERISTICS.format(oneId))
        x_track = sc.transform(x_track)
        y_track = classifier.predict(x_track)

        return int(y_track)

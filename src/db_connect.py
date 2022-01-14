import sqlite3
import csv
import credentials as cr
import pandas as pd

class Db_connect():
    
    def init_connection(self):
        self.connector = sqlite3.connect(cr.DATA_PATH + "spotify_database.db")
        self.cursor = self.connector.cursor()

    def close_connection(self):
        self.connector.close()

    def create_tables(self, requests):
        for request in requests:
            self.cursor.execute(request)

    def insert_data(self, request, csv_file):
        open_file = open(csv_file, encoding='utf-8')
        csv_rows = csv.reader(open_file)
        self.cursor.executemany(request, csv_rows)
        self.connector.commit()

    def get_data(self, request):
        self.cursor.execute(request)
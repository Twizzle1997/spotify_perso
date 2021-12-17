import sqlite3
import csv
import credentials as cr

class Db_connect():
    
    def init_connection(self):
        self.connector = sqlite3.connect(cr.DATA_PATH + "spotify_database.db")
        self.cursor = self.connector.cursor()

    def close_connection(self):
        self.connector.close()

    def create_tables(self, requests):
        for request in requests:
            self.cursor.execute(request)

    def insert_data(self, csv_file, table_name):
        open_file = open(csv_file)
        rows = csv.reader(open_file)
        self.cursor.executemany("INSERT INTO {table_name} VALUES (?, ?)", rows)
        self.connector.commit()

    def get_data(self):
        pass
    
 
    # cur.execute("SELECT * FROM data")
    # print(cur. fetchall())
    # 
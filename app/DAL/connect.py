import sqlite3


def db_connect(dbfile):
    conn = None
    conn = sqlite3.connect(dbfile)
    return conn


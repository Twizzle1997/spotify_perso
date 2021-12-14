import sqlite3
from DAL.connect import db_connect


conn = db_connect('DAL/DataBase_install/Prairie-Musique.db')
c = conn.cursor()
reqst = open('DAL/DataBase_install/Desinstllation_prairiemusic.sql', 'r', encoding='utf-8')
try: 
    c.executescript(reqst.read())
except Exception as erreur:
    print("Erreur dans uninstallPrairieMusic.py: ")
    print(erreur.args)
    pass
conn.commit()
c.close()
conn.close()
reqst.close()
print("base de données désinstallée")
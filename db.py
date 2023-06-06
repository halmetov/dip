from multiprocessing import connection
import sqlite3 as sq
from django import apps

from requests import ConnectTimeout 
conn = sq.connect('db.db')
with sq.connect("db.db") as con:
    cur = connection.cursor()
    cur.execute("SELECT * FROM cruise LEFT JOIN Gorod ON cruise.gorod = Gorod.gorodID")
    rows = cur.fetchall()
    connection.close()

if __name__ == '__main__':
    apps.run()

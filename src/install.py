import sqlite3

conn = sqlite3.connect('DataBase.db')
c = conn.cursor()

c.execute('.read main.sql')

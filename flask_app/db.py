import sqlite3

conn = sqlite3.connect('database.db')
print("Opened database successfully")

conn.execute('CREATE TABLE words (id INTEGER PRIMARY KEY, engg TEXT, russ TEXT)')
print("Table created successfully")


conn.close()

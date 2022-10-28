import sqlite3

def init_db():
    connection = sqlite3.connect('database.db')
    with open('model/schema.sql') as f:
        connection.executescript(f.read())
        connection.close()
    return

def init_test_db():
    connection = sqlite3.connect('database.db')
    with open('model/schema_test.sql') as f:
        connection.executescript(f.read())
        connection.close()
    return

def get_connection():
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    return connection

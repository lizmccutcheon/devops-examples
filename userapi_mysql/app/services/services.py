import mysql.connector
import json
from os import environ

### get environment variables
USER = environ.get('DB_CONFIG_USERNAME')
PASSWORD = environ.get('DB_CONFIG_PASSWORD')
DATABASE = environ.get('DB_CONFIG_DATABASE')
HOST = environ.get('DB_CONFIG_HOST')

### database connection
def get_connection():
    config = {
        'user': USER,
        'password': PASSWORD,
        'host': HOST,
        'port': '3306',
        'database': DATABASE
    }
    connection = mysql.connector.connect(**config)
    return connection

### Helper functions
def healthcheck():
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute('SELECT 1')
        rows = cursor.fetchall()
        cursor.close()
        conn.close()
        if len(rows) == 1:
            return 'OK'
        else:
            return None
    except:
        return None

def get_users():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM users')
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return json.dumps({"Users": results})


def get_user(username):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM users WHERE username = %s',(username,))
    results = cursor.fetchone()
    cursor.close()
    conn.close()
    if results is None:
        return None
    else:
        return json.dumps(results)

def add_user(username,firstname,lastname):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('INSERT INTO users (username, firstname,lastname) VALUES (%s, %s, %s)', ((username, firstname, lastname)))
    cursor.close()
    conn.commit()
    conn.close()
    return

def update_user(username, firstname, lastname):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('UPDATE `users` SET firstname = %s, lastname = %s WHERE username = %s',(firstname,lastname,username))
    cursor.close()
    conn.commit()
    conn.close()
    return

def delete_user(username):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('DELETE FROM `users` WHERE username = %s',(username,))
    cursor.close()
    conn.commit()
    conn.close()
    return

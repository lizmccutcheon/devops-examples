import sqlite3
import json
from model.api_models import *

def get_users():
    conn = get_connection()
    rows = conn.execute('SELECT * FROM users').fetchall()
    results = []
    for row in rows:
        d = dict(zip(row.keys(),row))
        results.append(d)
    conn.close()
    return json.dumps({"Users": results})


def healthcheck():
    try:
        conn = get_connection()
        rows = conn.execute('SELECT 1').fetchall()
        if len(rows) == 1:
            return 'OK'
        else:
            return None
    except:
        return None
        

def get_user(username):
    conn = get_connection()
    rows = conn.execute('SELECT * FROM users WHERE username = ?',(username,)).fetchall()
    results = []
    for row in rows:
        d = dict(zip(row.keys(),row))
        results.append(d)
    conn.close()
    if len(results) == 0:
        return None
    else:
        return json.dumps(results[0])


def add_user(username,firstname,lastname):
    if username != '' and firstname != '' and lastname != '':
        try:
            conn = get_connection()
            conn.execute('INSERT INTO users (username, firstname,lastname) VALUES (?, ?, ?)', ((username, firstname, lastname)))
            conn.commit()
            conn.close()
            return
        except Exception as e:
            return e
    else:
        return


def update_user(username, firstname, lastname):
    if username != '' and firstname != '' and lastname != '':
        try:
            conn = get_connection()
            conn.execute('UPDATE `users` SET firstname = ?, lastname = ? WHERE username = ?',(firstname,lastname,username))
            conn.commit()
            conn.close()
            return
        except Exception as e:
            return e
    else:
        return


def delete_user(username):
    if username != '':
        try:
            conn = get_connection()
            conn.execute('DELETE FROM `users` WHERE username = ?',(username,))
            conn.commit()
            conn.close()
            return
        except Exception as e:
            return e
    else:
        return

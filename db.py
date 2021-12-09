#import sqlite
import sqlite3

try:
    db = sqlite3.connect('app.db')
    print('connection to database is a success !')
    cursor = db.cursor()
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS users (user_id INTEGER , name Text)')
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS skills (name Text,progress TEXT,user_id INTEGER)')
except sqlite3.Error as er:
    print(f'Connection error {er}')

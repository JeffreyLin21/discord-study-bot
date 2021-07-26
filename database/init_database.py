import sqlite3
import sqlite3

def create_user_table(cursor):

  cursor.execute(""" CREATE TABLE IF NOT EXISTS discord_users (

      user_id INTEGER PRIMARY KEY,
      user_name TEXT NOT NULL,
      study_list TEXT

  )""")

def load_database():

    connection = sqlite3.connect("./database/discord_users.db")
    cursor = connection.cursor()
    create_user_table(cursor)

    print("Database loaded successfully")
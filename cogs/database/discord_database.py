import sqlite3

connection = sqlite3.connect("./cogs/database/discord_users.db")
cursor = connection.cursor()

def convert(category):
  if category == 'study_list':
    return 1
  return 0

def insert(uid, category, value):

  if (check_exists(uid)):
    replace(uid, category, value)
    pass

  if category == 'study_list':
    cursor.execute('INSERT INTO discord_users VALUES (?, ?)', (uid, value,))
    connection.commit()

def replace(uid, category, value):
  if category == 'study_list':
    cursor.execute("UPDATE discord_users SET study_list = ? WHERE user_id = ?", (value, uid,))
  connection.commit() 

def check_exists(uid):
  cursor.execute('SELECT EXISTS(SELECT 1 FROM discord_users WHERE user_id = ?)', (uid,))
  if cursor.fetchone():
    return True
  return False

def get(uid, category):
  cursor.execute("SELECT * FROM discord_users WHERE user_id = ?", (uid,))
  return cursor.fetchone()[convert(category,)]

def delete(uid):
  cursor.execute("DELETE FROM discord_users WHERE user_id = ?", (uid,))
  connection.commit()


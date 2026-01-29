import sqlite3

file="task_list.db"

def get_connect():
    return sqlite3.connect(file)

def create_table():

    conn= get_connect()
    cursor=conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS TASK(
                   ID INTEGER PRIMARY KEY AUTOINCREMENT,
                   TASK TEXT NOT NULL,
                   STATUS TEXT NOT NULL
                   )
""")

    conn.commit()
    conn.close()

create_table()    
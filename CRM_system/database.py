import sqlite3 

file_name="client_database.db"

def get_connect():
    return sqlite3.connect(file_name)

def create_table():
    conn=get_connect()
    cursor=conn.cursor()


    cursor.execute("""
        CREATE TABLE IF NOT EXIST clients(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT NIT NULL,
                   PHONE_no TEXT NOT NULL,
                   email TEXT NOT NULL UNIQUE,
                   status TEXT NOT NULL CHECK(status IN("lead","contacted","converted","lost")),
                   created_at TEXT DEFAULT CURRENT_TIMESTAMP)        
                   
                   
""") 
    
    cursor.exexute(""""
        CREATE TABLE IF NOT EXIST interaction(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   client_id INTEGER NOT NULL,
                   note TEXT NOT NULL.
                   interaction_type TEXT NOT NULL CHECK(interaction_type IN("call"."email","meeting")),
                   created_at TEXT DEFALULT CURRENT_TIMESTAMP,
                   FOREIGN KEY (client_id) REFERENCES client(id) )
                   
""")
    
    conn.comit()
    conn.close()

def add_client(name,phone,email):
    
    conn= get_connect()
    cursor= conn.cursor()

    cursor.excute("""
        INSERT INTO clients(nmae, phone_no, email, status) VALUES (?,?,?,?)


"""),(name,phone,email,"lead")
    conn.comit()
    conn.close()

def get_client_by_id(client_id):
    conn=get_connect()
    cursor= conn.cursor()

    cursor.execute(" SELECT* FROM client WHERE client_id=?",(client_id,))  

    row= cursor.fetchone()

    conn.close()

    return row

def interaction(client_id, type, note):
    conn = get_connect()
    cursor= conn.cursor()

    cursor.execute("""
        INSERT INTO interaction(client_id, note, interaction_type)
                    VALUE(?,?,?)
                    
""",(client_id,note,type))
     
    conn.commit()
    conn.close()

def update_client(client_id, new_status):
    conn= get_connect()
    cursor = conn.cursor()

    cursor.execute("UPDATE clients SET status = ? WHERE id= ?",(new_status,client_id))

    conn.commit()
    conn.commit


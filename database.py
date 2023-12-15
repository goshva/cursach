
import sqlite3
con = sqlite3.connect('main.db')
cur = con.cursor()


cur.execute(f'CREATE TABLE Users ( "id" INTEGER, "username" VARCHAR(20) UNIQUE, "password" VARCHAR(20) UNIQUE, "email" VARCHAR(30), "role" VARCHAR(20), PRIMARY KEY("id" AUTOINCREMENT) ) ')
cur.execute(f"INSERT INTO users (username, password, email, role) VALUES('admin', 'admin','admin@gmail.com', 'admin'), ('waiter', 'waiter','waiter@gmail.com', 'waiter')")
con.commit()

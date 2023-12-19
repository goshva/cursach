
import sqlite3
con = sqlite3.connect('main.db')
cur = con.cursor()

#таблица пользователей
#cur.execute(f'CREATE TABLE users ("id" INTEGER, "username" VARCHAR(30) UNIQUE, "password" VARCHAR(30),"email" VARCHAR(30), "role" VARCHAR(20), PRIMARY KEY("id" AUTOINCREMENT))')
#cur.execute(f"INSERT INTO users (username, password, email, role) VALUES('admin','admin', 'admin@gmail.com', 'admin'),('waiter','waiter', 'waiter@gmail.com', 'waiter')")

#таблица заказов
#cur.execute(f'CREATE TABLE orders ( "id" INTEGER, "dish_name" VARCHAR(30) UNIQUE, "table_num" integer(30), PRIMARY KEY("id" AUTOINCREMENT) )')
#cur.execute(f"INSERT INTO orders (dish_name, table_num) VALUES('Брускетта с томатами','2'),('Панна-котта с клубникой','6'), ('Филе миньон с красным вином','1'), ('Карпаччо осьминог','5')")

#таблица клиентов
#cur.execute(f'CREATE TABLE clients ( "id" INTEGER, "name" VARCHAR(30), "lastname" VARCHAR(30), "phone_number" VARCHAR(30), "discount" INTEGER(20), PRIMARY KEY("id" AUTOINCREMENT) )')
#cur.execute(f"INSERT INTO clients (name, lastname, phone_number, discount) VALUES('Алексей','Крюков', '+79781710765', '10%'),('Владимир','Яковлев', '+79969951898', '5%'), ('Иван','Андреев', '+79083755032', '5%'), ('Анна','Киселева', '+79023539639', '10%')")

#таблица меню
#cur.execute(f'CREATE TABLE menu ( "id" INTEGER, "name_dish" VARCHAR(30), "structure" VARCHAR(30), "price" INTEGER(30), PRIMARY KEY("id" AUTOINCREMENT) )')
#cur.execute(f"INSERT INTO menu (name_dish, structure, price) VALUES('Брускетта с томатами', 'с сыром страчателла', '570р'),('Карпаччо осьминог', 'с авокадо, руколой и креветками', '1670р'),('Салат Экзотика', 'с авокадо, руколой и креветками', '1200р'),('Тёплый салат Маре', 'с морепродуктами и фенхелем', '1450р'),('Салат корн с куриной печенью', 'и белыми грибами', '990р'),('Филе миньон с красным вином', 'и белыми грибами', '2850р'),('Филе миньон', 'с трюфельным кремом', '2900р'),('Равиоли с крабом и креветкой', 'под сливочным соусом', '1780р'),('Панна-котта с клубникой', '', '550р'),('Шоколадный фондан','','580р')")

#таблица сотрудников
#cur.execute(f'CREATE TABLE employees ("id" INTEGER, "name" VARCHAR(30) UNIQUE, "lastname" VARCHAR(30),"phone_number" VARCHAR(30), PRIMARY KEY("id" AUTOINCREMENT))')
#cur.execute(f"INSERT INTO employees (name, lastname, phone_number) VALUES('Валерий','Станиславов', '+79889607291'),('Дмитрий','Ничаев', '+79805553353')")

con.commit()

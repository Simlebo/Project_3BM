# Module généré par GenDB.py
#===========================
import sqlite3
from PySide6.QtSql import QSqlDatabase, QSqlTableModel

def createAllTables():
	conn = sqlite3.connect("dB_3BM_Project.db")
	cur = conn.cursor()
	# electricity_price
	cur.execute('''
			CREATE TABLE IF NOT EXISTS electricity_price
			(
				date DATETIME NOT NULL,
				price REAL NOT NULL,
				PRIMARY KEY (date)
			)
			''')

	# users
	cur.execute('''
			CREATE TABLE IF NOT EXISTS users
			(
				users_id INTEGER NOT NULL,
				name INTEGER NOT NULL,
				mail INTEGER,
				PRIMARY KEY (users_id)
			)
			''')

	# product
	cur.execute('''
			CREATE TABLE IF NOT EXISTS product
			(
				product_id INTEGER NOT NULL,
				price REAL NOT NULL,
				name TEXT,
				price_brut INTEGER NOT NULL,
				PRIMARY KEY (product_id)
			)
			''')

	# customer
	cur.execute('''
			CREATE TABLE IF NOT EXISTS customer
			(
				customer_id INTEGER NOT NULL,
				order_id INTEGER UNIQUE NOT NULL,
				name TEXT NOT NULL,
				account_number TEXT NOT NULL,
				PRIMARY KEY (customer_id)
			)
			''')

	# customer_order
	cur.execute('''
			CREATE TABLE IF NOT EXISTS customer_order
			(
				order_id INTEGER NOT NULL,
				customer_id INTEGER UNIQUE NOT NULL,
				date DATETIME NOT NULL,
				PRIMARY KEY (order_id),
				FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
			)
			''')

	# order_details
	cur.execute('''
			CREATE TABLE IF NOT EXISTS order_details
			(
				order_detail_id INTEGER NOT NULL,
				order_id INTEGER UNIQUE NOT NULL,
				product_id INTEGER UNIQUE NOT NULL,
				number INTEGER NOT NULL,
				PRIMARY KEY (order_detail_id),
				FOREIGN KEY (order_id) REFERENCES customer_order(order_id),
				FOREIGN KEY (product_id) REFERENCES product(product_id)
			)
			''')

	# machine
	cur.execute('''
			CREATE TABLE IF NOT EXISTS machine
			(
				machine_id INTEGER NOT NULL,
				user_id INTEGER UNIQUE NOT NULL,
				consumption REAL NOT NULL,
				PRIMARY KEY (machine_id),
				FOREIGN KEY (user_id) REFERENCES users(users_id)
			)
			''')

	# fabrication_step
	cur.execute('''
			CREATE TABLE IF NOT EXISTS fabrication_step
			(
				step_id INTEGER NOT NULL,
				product_id INTEGER UNIQUE NOT NULL,
				machine_id INTEGER UNIQUE NOT NULL,
				fabrication_step INTEGER NOT NULL,
				time REAL NOT NULL,
				step_name TEXT NOT NULL,
				PRIMARY KEY (step_id),
				FOREIGN KEY (product_id) REFERENCES product(product_id),
				FOREIGN KEY (machine_id) REFERENCES machine(machine_id)
			)
			''')
	conn.commit()
	conn.close()

def createTables_electricity_price():
	conn = sqlite3.connect("dB_3BM_Project.db")
	cur = conn.cursor()
	# electricity_price
	cur.execute('''
			CREATE TABLE IF NOT EXISTS electricity_price
			(
				date DATETIME NOT NULL,
				price REAL NOT NULL,
				PRIMARY KEY (date)
			)
			''')
	conn.commit()
	conn.close()

def createTables_users():
	conn = sqlite3.connect("dB_3BM_Project.db")
	cur = conn.cursor()
	# users
	cur.execute('''
			CREATE TABLE IF NOT EXISTS users
			(
				users_id INTEGER NOT NULL,
				name INTEGER NOT NULL,
				mail INTEGER,
				PRIMARY KEY (users_id)
			)
			''')
	conn.commit()
	conn.close()

def createTables_product():
	conn = sqlite3.connect("dB_3BM_Project.db")
	cur = conn.cursor()
	# product
	cur.execute('''
			CREATE TABLE IF NOT EXISTS product
			(
				product_id INTEGER NOT NULL,
				price REAL NOT NULL,
				name TEXT,
				price_brut INTEGER NOT NULL,
				PRIMARY KEY (product_id)
			)
			''')
	conn.commit()
	conn.close()

def createTables_customer():
	conn = sqlite3.connect("dB_3BM_Project.db")
	cur = conn.cursor()
	# customer
	cur.execute('''
			CREATE TABLE IF NOT EXISTS customer
			(
				customer_id INTEGER NOT NULL,
				order_id INTEGER UNIQUE NOT NULL,
				name TEXT NOT NULL,
				account_number TEXT NOT NULL,
				PRIMARY KEY (customer_id)
			)
			''')
	conn.commit()
	conn.close()

def createTables_customer_order():
	conn = sqlite3.connect("dB_3BM_Project.db")
	cur = conn.cursor()
	# customer_order
	cur.execute('''
			CREATE TABLE IF NOT EXISTS customer_order
			(
				order_id INTEGER NOT NULL,
				customer_id INTEGER UNIQUE NOT NULL,
				date DATETIME NOT NULL,
				PRIMARY KEY (order_id),
				FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
			)
			''')
	conn.commit()
	conn.close()

def createTables_order_details():
	conn = sqlite3.connect("dB_3BM_Project.db")
	cur = conn.cursor()
	# order_details
	cur.execute('''
			CREATE TABLE IF NOT EXISTS order_details
			(
				order_detail_id INTEGER NOT NULL,
				order_id INTEGER UNIQUE NOT NULL,
				product_id INTEGER UNIQUE NOT NULL,
				number INTEGER NOT NULL,
				PRIMARY KEY (order_detail_id),
				FOREIGN KEY (order_id) REFERENCES customer_order(order_id),
				FOREIGN KEY (product_id) REFERENCES product(product_id)
			)
			''')
	conn.commit()
	conn.close()

def createTables_machine():
	conn = sqlite3.connect("dB_3BM_Project.db")
	cur = conn.cursor()
	# machine
	cur.execute('''
			CREATE TABLE IF NOT EXISTS machine
			(
				machine_id INTEGER NOT NULL,
				user_id INTEGER UNIQUE NOT NULL,
				consumption REAL NOT NULL,
				PRIMARY KEY (machine_id),
				FOREIGN KEY (user_id) REFERENCES users(users_id)
			)
			''')
	conn.commit()
	conn.close()

def createTables_fabrication_step():
	conn = sqlite3.connect("dB_3BM_Project.db")
	cur = conn.cursor()
	# fabrication_step
	cur.execute('''
			CREATE TABLE IF NOT EXISTS fabrication_step
			(
				step_id INTEGER NOT NULL,
				product_id INTEGER UNIQUE NOT NULL,
				machine_id INTEGER UNIQUE NOT NULL,
				fabrication_step INTEGER NOT NULL,
				time REAL NOT NULL,
				step_name TEXT NOT NULL,
				PRIMARY KEY (step_id),
				FOREIGN KEY (product_id) REFERENCES product(product_id),
				FOREIGN KEY (machine_id) REFERENCES machine(machine_id)
			)
			''')
	conn.commit()
	conn.close()

# INSERT INTO electricity_price
def insert_electricity_price(date,price):
	conn = sqlite3.connect("dB_3BM_Project.db")
	cur = conn.cursor()
	sqlQuery="INSERT OR IGNORE INTO electricity_price (date,price) "
	sqlQuery+=f"VALUES ('{date}',{price})"
	cur.execute(sqlQuery)
	conn.commit()
	conn.close()

# INSERT INTO users
def insert_users(users_id,name,mail):
	conn = sqlite3.connect("dB_3BM_Project.db")
	cur = conn.cursor()
	sqlQuery="INSERT OR IGNORE INTO users (users_id,name,mail) "
	sqlQuery+=f"VALUES ({users_id},{name},{mail})"
	cur.execute(sqlQuery)
	conn.commit()
	conn.close()

# INSERT INTO product
def insert_product(product_id,price,name,price_brut):
	conn = sqlite3.connect("dB_3BM_Project.db")
	cur = conn.cursor()
	sqlQuery="INSERT OR IGNORE INTO product (product_id,price,name,price_brut) "
	sqlQuery+=f"VALUES ({product_id},{price},'{name}',{price_brut})"
	cur.execute(sqlQuery)
	conn.commit()
	conn.close()

# INSERT INTO customer
def insert_customer(customer_id,order_id,name,account_number):
	conn = sqlite3.connect("dB_3BM_Project.db")
	cur = conn.cursor()
	sqlQuery="INSERT OR IGNORE INTO customer (customer_id,order_id,name,account_number) "
	sqlQuery+=f"VALUES ({customer_id},{order_id},'{name}','{account_number}')"
	cur.execute(sqlQuery)
	conn.commit()
	conn.close()

# INSERT INTO customer_order
def insert_customer_order(order_id,customer_id,date):
	conn = sqlite3.connect("dB_3BM_Project.db")
	cur = conn.cursor()
	sqlQuery="INSERT OR IGNORE INTO customer_order (order_id,customer_id,date) "
	sqlQuery+=f"VALUES ({order_id},{customer_id},'{date}')"
	cur.execute(sqlQuery)
	conn.commit()
	conn.close()

# INSERT INTO order_details
def insert_order_details(order_detail_id,order_id,product_id,number):
	conn = sqlite3.connect("dB_3BM_Project.db")
	cur = conn.cursor()
	sqlQuery="INSERT OR IGNORE INTO order_details (order_detail_id,order_id,product_id,number) "
	sqlQuery+=f"VALUES ({order_detail_id},{order_id},{product_id},{number})"
	cur.execute(sqlQuery)
	conn.commit()
	conn.close()

# INSERT INTO machine
def insert_machine(machine_id,user_id,consumption):
	conn = sqlite3.connect("dB_3BM_Project.db")
	cur = conn.cursor()
	sqlQuery="INSERT OR IGNORE INTO machine (machine_id,user_id,consumption) "
	sqlQuery+=f"VALUES ({machine_id},{user_id},{consumption})"
	cur.execute(sqlQuery)
	conn.commit()
	conn.close()

# INSERT INTO fabrication_step
def insert_fabrication_step(step_id,product_id,machine_id,fabrication_step,time,step_name):
	conn = sqlite3.connect("dB_3BM_Project.db")
	cur = conn.cursor()
	sqlQuery="INSERT OR IGNORE INTO fabrication_step (step_id,product_id,machine_id,fabrication_step,time,step_name) "
	sqlQuery+=f"VALUES ({step_id},{product_id},{machine_id},{fabrication_step},{time},'{step_name}')"
	cur.execute(sqlQuery)
	conn.commit()
	conn.close()

# SELECT fields FROM electricity_price WHERE condition
def select_electricity_price(WHERE):
	conn = sqlite3.connect("dB_3BM_Project.db")
	cur = conn.cursor()
	sqlQuery="SELECT date,price FROM electricity_price"
	if WHERE.strip()!="":
		sqlQuery+=f" WHERE {WHERE}"
	cur.execute(sqlQuery)
	rows = cur.fetchall()
	conn.commit()
	conn.close()
	return rows

# SELECT fields FROM users WHERE condition
def select_users(WHERE):
	conn = sqlite3.connect("dB_3BM_Project.db")
	cur = conn.cursor()
	sqlQuery="SELECT users_id,name,mail FROM users"
	if WHERE.strip()!="":
		sqlQuery+=f" WHERE {WHERE}"
	cur.execute(sqlQuery)
	rows = cur.fetchall()
	conn.commit()
	conn.close()
	return rows

# SELECT fields FROM product WHERE condition
def select_product(WHERE):
	conn = sqlite3.connect("dB_3BM_Project.db")
	cur = conn.cursor()
	sqlQuery="SELECT product_id,price,name,price_brut FROM product"
	if WHERE.strip()!="":
		sqlQuery+=f" WHERE {WHERE}"
	cur.execute(sqlQuery)
	rows = cur.fetchall()
	conn.commit()
	conn.close()
	return rows

# SELECT fields FROM customer WHERE condition
def select_customer(WHERE):
	conn = sqlite3.connect("dB_3BM_Project.db")
	cur = conn.cursor()
	sqlQuery="SELECT customer_id,order_id,name,account_number FROM customer"
	if WHERE.strip()!="":
		sqlQuery+=f" WHERE {WHERE}"
	cur.execute(sqlQuery)
	rows = cur.fetchall()
	conn.commit()
	conn.close()
	return rows

# SELECT fields FROM customer_order WHERE condition
def select_customer_order(WHERE):
	conn = sqlite3.connect("dB_3BM_Project.db")
	cur = conn.cursor()
	sqlQuery="SELECT order_id,customer_id,date FROM customer_order"
	if WHERE.strip()!="":
		sqlQuery+=f" WHERE {WHERE}"
	cur.execute(sqlQuery)
	rows = cur.fetchall()
	conn.commit()
	conn.close()
	return rows

# SELECT fields FROM order_details WHERE condition
def select_order_details(WHERE):
	conn = sqlite3.connect("dB_3BM_Project.db")
	cur = conn.cursor()
	sqlQuery="SELECT order_detail_id,order_id,product_id,number FROM order_details"
	if WHERE.strip()!="":
		sqlQuery+=f" WHERE {WHERE}"
	cur.execute(sqlQuery)
	rows = cur.fetchall()
	conn.commit()
	conn.close()
	return rows

# SELECT fields FROM machine WHERE condition
def select_machine(WHERE):
	conn = sqlite3.connect("dB_3BM_Project.db")
	cur = conn.cursor()
	sqlQuery="SELECT machine_id,user_id,consumption FROM machine"
	if WHERE.strip()!="":
		sqlQuery+=f" WHERE {WHERE}"
	cur.execute(sqlQuery)
	rows = cur.fetchall()
	conn.commit()
	conn.close()
	return rows

# SELECT fields FROM fabrication_step WHERE condition
def select_fabrication_step(WHERE):
	conn = sqlite3.connect("dB_3BM_Project.db")
	cur = conn.cursor()
	sqlQuery="SELECT step_id,product_id,machine_id,fabrication_step,time,step_name FROM fabrication_step"
	if WHERE.strip()!="":
		sqlQuery+=f" WHERE {WHERE}"
	cur.execute(sqlQuery)
	rows = cur.fetchall()
	conn.commit()
	conn.close()
	return rows

# UPDATE electricity_price SET fields=value WHERE condition
def update_electricity_price(date,price,WHERE):
	conn = sqlite3.connect("dB_3BM_Project.db")
	cur = conn.cursor()
	sqlQuery=f"UPDATE electricity_price SET date='{date}',price = {price}"
	if WHERE.strip()!="":
		sqlQuery+=f" WHERE {WHERE}"
	cur.execute(sqlQuery)
	conn.commit()
	conn.close()

# UPDATE users SET fields=value WHERE condition
def update_users(users_id,name,mail,WHERE):
	conn = sqlite3.connect("dB_3BM_Project.db")
	cur = conn.cursor()
	sqlQuery=f"UPDATE users SET users_id = {users_id},name = {name},mail = {mail}"
	if WHERE.strip()!="":
		sqlQuery+=f" WHERE {WHERE}"
	cur.execute(sqlQuery)
	conn.commit()
	conn.close()

# UPDATE product SET fields=value WHERE condition
def update_product(product_id,price,name,price_brut,WHERE):
	conn = sqlite3.connect("dB_3BM_Project.db")
	cur = conn.cursor()
	sqlQuery=f"UPDATE product SET product_id = {product_id},price = {price},name='{name}',price_brut = {price_brut}"
	if WHERE.strip()!="":
		sqlQuery+=f" WHERE {WHERE}"
	cur.execute(sqlQuery)
	conn.commit()
	conn.close()

# UPDATE customer SET fields=value WHERE condition
def update_customer(customer_id,order_id,name,account_number,WHERE):
	conn = sqlite3.connect("dB_3BM_Project.db")
	cur = conn.cursor()
	sqlQuery=f"UPDATE customer SET customer_id = {customer_id},order_id = {order_id},name='{name}',account_number='{account_number}'"
	if WHERE.strip()!="":
		sqlQuery+=f" WHERE {WHERE}"
	cur.execute(sqlQuery)
	conn.commit()
	conn.close()

# UPDATE customer_order SET fields=value WHERE condition
def update_customer_order(order_id,customer_id,date,WHERE):
	conn = sqlite3.connect("dB_3BM_Project.db")
	cur = conn.cursor()
	sqlQuery=f"UPDATE customer_order SET order_id = {order_id},customer_id = {customer_id},date='{date}'"
	if WHERE.strip()!="":
		sqlQuery+=f" WHERE {WHERE}"
	cur.execute(sqlQuery)
	conn.commit()
	conn.close()

# UPDATE order_details SET fields=value WHERE condition
def update_order_details(order_detail_id,order_id,product_id,number,WHERE):
	conn = sqlite3.connect("dB_3BM_Project.db")
	cur = conn.cursor()
	sqlQuery=f"UPDATE order_details SET order_detail_id = {order_detail_id},order_id = {order_id},product_id = {product_id},number = {number}"
	if WHERE.strip()!="":
		sqlQuery+=f" WHERE {WHERE}"
	cur.execute(sqlQuery)
	conn.commit()
	conn.close()

# UPDATE machine SET fields=value WHERE condition
def update_machine(machine_id,user_id,consumption,WHERE):
	conn = sqlite3.connect("dB_3BM_Project.db")
	cur = conn.cursor()
	sqlQuery=f"UPDATE machine SET machine_id = {machine_id},user_id = {user_id},consumption = {consumption}"
	if WHERE.strip()!="":
		sqlQuery+=f" WHERE {WHERE}"
	cur.execute(sqlQuery)
	conn.commit()
	conn.close()

# UPDATE fabrication_step SET fields=value WHERE condition
def update_fabrication_step(step_id,product_id,machine_id,fabrication_step,time,step_name,WHERE):
	conn = sqlite3.connect("dB_3BM_Project.db")
	cur = conn.cursor()
	sqlQuery=f"UPDATE fabrication_step SET step_id = {step_id},product_id = {product_id},machine_id = {machine_id},fabrication_step = {fabrication_step},time = {time},step_name='{step_name}'"
	if WHERE.strip()!="":
		sqlQuery+=f" WHERE {WHERE}"
	cur.execute(sqlQuery)
	conn.commit()
	conn.close()

# DELETE FROM electricity_price WHERE condition 
# ATTENTION : Si pas de condition ("") efface toutes les données de la table !!!
def delete_electricity_price(WHERE):
	conn = sqlite3.connect("dB_3BM_Project.db")
	cur = conn.cursor()
	sqlQuery="DELETE FROM electricity_price"
	if WHERE.strip()!="":
		sqlQuery+=f" WHERE {WHERE}"
	cur.execute(sqlQuery)
	conn.commit()
	conn.close()

# DELETE FROM users WHERE condition 
# ATTENTION : Si pas de condition ("") efface toutes les données de la table !!!
def delete_users(WHERE):
	conn = sqlite3.connect("dB_3BM_Project.db")
	cur = conn.cursor()
	sqlQuery="DELETE FROM users"
	if WHERE.strip()!="":
		sqlQuery+=f" WHERE {WHERE}"
	cur.execute(sqlQuery)
	conn.commit()
	conn.close()

# DELETE FROM product WHERE condition 
# ATTENTION : Si pas de condition ("") efface toutes les données de la table !!!
def delete_product(WHERE):
	conn = sqlite3.connect("dB_3BM_Project.db")
	cur = conn.cursor()
	sqlQuery="DELETE FROM product"
	if WHERE.strip()!="":
		sqlQuery+=f" WHERE {WHERE}"
	cur.execute(sqlQuery)
	conn.commit()
	conn.close()

# DELETE FROM customer WHERE condition 
# ATTENTION : Si pas de condition ("") efface toutes les données de la table !!!
def delete_customer(WHERE):
	conn = sqlite3.connect("dB_3BM_Project.db")
	cur = conn.cursor()
	sqlQuery="DELETE FROM customer"
	if WHERE.strip()!="":
		sqlQuery+=f" WHERE {WHERE}"
	cur.execute(sqlQuery)
	conn.commit()
	conn.close()

# DELETE FROM customer_order WHERE condition 
# ATTENTION : Si pas de condition ("") efface toutes les données de la table !!!
def delete_customer_order(WHERE):
	conn = sqlite3.connect("dB_3BM_Project.db")
	cur = conn.cursor()
	sqlQuery="DELETE FROM customer_order"
	if WHERE.strip()!="":
		sqlQuery+=f" WHERE {WHERE}"
	cur.execute(sqlQuery)
	conn.commit()
	conn.close()

# DELETE FROM order_details WHERE condition 
# ATTENTION : Si pas de condition ("") efface toutes les données de la table !!!
def delete_order_details(WHERE):
	conn = sqlite3.connect("dB_3BM_Project.db")
	cur = conn.cursor()
	sqlQuery="DELETE FROM order_details"
	if WHERE.strip()!="":
		sqlQuery+=f" WHERE {WHERE}"
	cur.execute(sqlQuery)
	conn.commit()
	conn.close()

# DELETE FROM machine WHERE condition 
# ATTENTION : Si pas de condition ("") efface toutes les données de la table !!!
def delete_machine(WHERE):
	conn = sqlite3.connect("dB_3BM_Project.db")
	cur = conn.cursor()
	sqlQuery="DELETE FROM machine"
	if WHERE.strip()!="":
		sqlQuery+=f" WHERE {WHERE}"
	cur.execute(sqlQuery)
	conn.commit()
	conn.close()

# DELETE FROM fabrication_step WHERE condition 
# ATTENTION : Si pas de condition ("") efface toutes les données de la table !!!
def delete_fabrication_step(WHERE):
	conn = sqlite3.connect("dB_3BM_Project.db")
	cur = conn.cursor()
	sqlQuery="DELETE FROM fabrication_step"
	if WHERE.strip()!="":
		sqlQuery+=f" WHERE {WHERE}"
	cur.execute(sqlQuery)
	conn.commit()
	conn.close()

# DROP TABLE electricity_price
# ATTENTION : cette fonction détruit la table, elle devra (éventuellement) être recréée
def drop_electricity_price():
	conn = sqlite3.connect("dB_3BM_Project.db")
	cur = conn.cursor()
	sqlQuery="DROP TABLE electricity_price"
	cur.execute(sqlQuery)
	conn.commit()
	conn.close()

# DROP TABLE users
# ATTENTION : cette fonction détruit la table, elle devra (éventuellement) être recréée
def drop_users():
	conn = sqlite3.connect("dB_3BM_Project.db")
	cur = conn.cursor()
	sqlQuery="DROP TABLE users"
	cur.execute(sqlQuery)
	conn.commit()
	conn.close()

# DROP TABLE product
# ATTENTION : cette fonction détruit la table, elle devra (éventuellement) être recréée
def drop_product():
	conn = sqlite3.connect("dB_3BM_Project.db")
	cur = conn.cursor()
	sqlQuery="DROP TABLE product"
	cur.execute(sqlQuery)
	conn.commit()
	conn.close()

# DROP TABLE customer
# ATTENTION : cette fonction détruit la table, elle devra (éventuellement) être recréée
def drop_customer():
	conn = sqlite3.connect("dB_3BM_Project.db")
	cur = conn.cursor()
	sqlQuery="DROP TABLE customer"
	cur.execute(sqlQuery)
	conn.commit()
	conn.close()

# DROP TABLE customer_order
# ATTENTION : cette fonction détruit la table, elle devra (éventuellement) être recréée
def drop_customer_order():
	conn = sqlite3.connect("dB_3BM_Project.db")
	cur = conn.cursor()
	sqlQuery="DROP TABLE customer_order"
	cur.execute(sqlQuery)
	conn.commit()
	conn.close()

# DROP TABLE order_details
# ATTENTION : cette fonction détruit la table, elle devra (éventuellement) être recréée
def drop_order_details():
	conn = sqlite3.connect("dB_3BM_Project.db")
	cur = conn.cursor()
	sqlQuery="DROP TABLE order_details"
	cur.execute(sqlQuery)
	conn.commit()
	conn.close()

# DROP TABLE machine
# ATTENTION : cette fonction détruit la table, elle devra (éventuellement) être recréée
def drop_machine():
	conn = sqlite3.connect("dB_3BM_Project.db")
	cur = conn.cursor()
	sqlQuery="DROP TABLE machine"
	cur.execute(sqlQuery)
	conn.commit()
	conn.close()

# DROP TABLE fabrication_step
# ATTENTION : cette fonction détruit la table, elle devra (éventuellement) être recréée
def drop_fabrication_step():
	conn = sqlite3.connect("dB_3BM_Project.db")
	cur = conn.cursor()
	sqlQuery="DROP TABLE fabrication_step"
	cur.execute(sqlQuery)
	conn.commit()
	conn.close()


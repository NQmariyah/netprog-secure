import sqlite3

def connect_db():
	connection = sqlite3.connect('todolist.db')
	connection.row_factory = sqlite3.Row
	return connection

def create_table():
	connection = connect_db()
	cursor = connection.cursor()
	cursor.execute('''
		CREATE TABLE IF NOT EXISTS tasks (
			   id INTEGER PRIMARY KEY AUTOINCREMENT,
			   item TEXT NOT NULL,
			   completed BOOLEAN DEFAULT FALSE
			)
		''')
	connection.commit()
	connection.close()

def get_all_tasks():
	connection = connect_db()
	cursor = connection.cursor()
	cursor.execute('SELECT * FROM tasks')
	tasks = cursor.fetchall()
	connection.close()
	return tasks   

def get_task_by_id(task_id):
	connection = connect_db()
	cursor = connection.cursor()
	cursor.execute('SELECT * FROM tasks WHERE id = ?', (task_id,))
	task = cursor.fetchone()
	connection.close()
	return task

def create_task(item):
	connection = connect_db()
	cursor = connection.cursor()
	cursor.execute('INSERT INTO tasks (item) VALUES (?)', (item))
	tasks = cursor.fetchall()
	connection.close()
	return tasks

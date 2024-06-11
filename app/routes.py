from flask import Flask, jsonify, request, abort
from app import database

app = Flask(__name__)

@app.before_request
def create_db_if_not_exist():
	database.create_table()

@app.route('/tasks', methods=['GET'])
def get_tasks():
	tasks = database.get_all_tasks()
	return jsonify({'task': [{'id':task[0], 'item': task[1], 'completed':task[2]} for task in tasks]})

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
	tasks = database.get_task_by_id(task_id)
	if task is None:
		abort(404, "Task not found")
	return jsonify(task)

@app.route('/tasks', methods=['POST'])
def create_new_task():
	if not request.json or not 'item' in request.json:
		abort(400, "Bad request")

	item = request.json['item']
	database.create_task(item)

	return jsonify({'message' : "Task created"})

if __name__ == '__main__':
	app.run()

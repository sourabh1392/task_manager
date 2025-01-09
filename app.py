from flask import Flask, request, jsonify
from config import get_db

app = Flask(__name__)
db = get_db()
tasks_collection = db.tasks

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = list(tasks_collection.find({}, {'_id': 0}))
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    task = {"title": data['title'], "completed": False}
    tasks_collection.insert_one(task)
    return jsonify({"message": "Task created successfully"}), 201

@app.route('/tasks/<title>', methods=['PUT'])
def update_task(title):
    data = request.json
    tasks_collection.update_one({'title': title}, {'$set': {'completed': data['completed']}})
    return jsonify({"message": "Task updated successfully"})

@app.route('/tasks/<title>', methods=['DELETE'])
def delete_task(title):
    tasks_collection.delete_one({'title': title})
    return jsonify({"message": "Task deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)

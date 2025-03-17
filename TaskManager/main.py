from flask import Flask, render_template, request, redirect, url_for
from flask_restful import Resource, Api
import requests

app = Flask(__name__)
api = Api(app)

tasks = []

class Task(Resource):
    def get(self, task_id=None):
        if task_id:
            for task in tasks:
                if task['id'] == task_id:
                    return task, 200
            return {"message": "Task not found"}, 404
        return tasks, 200

    def post(self):
        data = request.get_json()
        task_id = len(tasks) + 1
        task = {
            'id': task_id,
            'title': data['title'],
            'description': data['description'],
            'deadline': data.get('deadline'),
            'assignment_type': data.get('assignment_type')
        }
        tasks.append(task)
        return task, 201

    def delete(self, task_id):
        global tasks
        tasks = [task for task in tasks if task['id'] != task_id]
        return {"message": f"Task {task_id} deleted"}, 200

api.add_resource(Task, '/api/task', '/api/task/<int:task_id>')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_task', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        new_task = {
            'title': request.form['title'],
            'description': request.form['description'],
            'deadline': request.form['deadline'],
            'assignment_type': request.form['assignment_type']
        }
        requests.post('http://127.0.0.1:5000/api/task', json=new_task)
        return redirect(url_for('show_tasks'))
    return render_template('add_task.html')

@app.route('/show_tasks')
def show_tasks():
    response = requests.get('http://127.0.0.1:5000/api/task')
    tasks_list = response.json()
    return render_template('show_tasks.html', tasks=tasks_list)

@app.route('/delete_tasks', methods=['POST'])
def delete_tasks():
    task_ids = request.form.getlist('task_ids')
    for task_id in task_ids:
        requests.delete(f'http://127.0.0.1:5000/api/task/{task_id}')
    return redirect(url_for('show_tasks'))

if __name__ == '__main__':
    app.run(debug=True)
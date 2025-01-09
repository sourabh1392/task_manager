# Task Manager

A simple task management app using Flask and MongoDB.

## Features
- Add tasks
- View all tasks
- Update task status
- Delete tasks

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Start MongoDB server.
3. Run the app: `python app.py`.
4. Access the app at `http://127.0.0.1:5000/`.

## API Endpoints
- `GET /tasks`: Fetch all tasks.
- `POST /tasks`: Add a new task.
- `PUT /tasks/<title>`: Update task status.
- `DELETE /tasks/<title>`: Delete a task.


# simplerestfulapi
Task Tracker which using a python script to integrate using flask for html front end.

MAKE SURE TO INSTALL pip flasgger & pip install flask for the API to work.

Simple Restful API For In-memory TaskTracker

📘 Flask Task API – Explanation
Project: Simple REST API using Flask
Purpose: In-memory Task Tracker
Author: 

🔧 What This API Does
This Flask API allows users to create and view a list of tasks. It simulates a simple backend system for a to-do list or task management app.

🧠 It supports two main actions:

GET – View all existing tasks

POST – Add a new task


🔁 How It Works
When you run the Flask app, it launches a local web server. That server listens for HTTP requests at certain "routes" (URLs), and performs actions based on the HTTP method (GET or POST).

🔌 API Endpoints
GET /tasks

📥 What it does: Returns all current tasks.

📤 Response format: JSON array.

🧠 Use case: A user wants to view the to-do list.

Example Request:


curl http://127.0.0.1:5000/tasks
Example Response:

json

[
  {"title": "Buy groceries"},
  {"title": "Call mom"}
]

POST /tasks
📥 What it does: Accepts a new task (in JSON format) and adds it to the list.

📤 Response format: Updated task list.

🚨 Note: The task must be sent in JSON, using Content-Type: application/json.

Example Request:

curl -X POST -H "Content-Type: application/json" -d '{"title": "Read a book"}' http://127.0.0.1:5000/tasks
Example Response:

json

[
  {"title": "Buy groceries"},
  {"title": "Call mom"},
  {"title": "Read a book"}
]

------------------------------------------------------------------

🛠️ Current Limitations
Tasks are not persistent (data resets on restart).

No task ID or update/delete functionality yet.

No database — purely in-memory.



💡 Future Ideas (for GitHub improvement):
Add a task_id to each task.

Add support for PUT and DELETE endpoints.

Add input validation and error handling.

Connect it to a real database (like SQLite or MongoDB).

Create a front-end (React or HTML) to interact with it.





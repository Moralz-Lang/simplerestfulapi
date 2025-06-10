# Import Flask framework tools
from flask import Flask, request, jsonify, render_template

# Import Swagger support for interactive API docs
from flasgger import Swagger

# Import built-in Python libraries to handle JSON and file system
import json
import os

# Create a Flask web app instance
app = Flask(__name__)

# Initialize Swagger so you can view API docs at http://127.0.0.1:5000/apidocs
swagger = Swagger(app)

# Define the filename where tasks will be stored (like a lightweight database)
DATA_FILE = 'tasks.json'

# Check if the file exists; if not, create it with an empty list inside
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump([], f)

# Function to load tasks from the file
def load_tasks():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

# Function to save updated tasks list back to the file
def save_tasks(tasks):
    with open(DATA_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

# Route for the homepage — shows the basic HTML interface
@app.route('/')
def home():
    return render_template('index.html')  # Loads HTML page from templates/index.html

# Route to GET all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    """
    Get the list of all tasks
    ---
    responses:
      200:
        description: List of all tasks stored
    """
    tasks = load_tasks()          # Load tasks from the file
    return jsonify(tasks)         # Return tasks as JSON to the browser/client

# Route to POST (add) a new task
@app.route('/tasks', methods=['POST'])
def add_task():
    """
    Add a new task
    ---
    parameters:
      - in: body
        name: task
        required: true
        schema:
          type: object
          properties:
            title:
              type: string
              example: Learn Flask
    responses:
      201:
        description: Task added successfully
    """
    task = request.get_json()     # Get task data from request body
    tasks = load_tasks()          # Load existing tasks
    tasks.append(task)            # Add the new task
    save_tasks(tasks)             # Save updated list to file
    return jsonify(tasks), 201    # Return updated task list with 201 Created

# Run the app only if this file is executed directly (not imported elsewhere)
if __name__ == '__main__':
    app.run(debug=True)           # Run Flask in debug mode so you see helpful errors

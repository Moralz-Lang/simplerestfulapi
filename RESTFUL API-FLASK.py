#Create Flask API
# if your using in a testing enviornment use this from doctest import debug


# Import the Flask class and required modules to build the API
from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# In-memory list to store task data (simulates a database)
# This means the data will be lost when the app restarts
tasks = []

# Define a route for HTTP GET requests at the URL "/tasks"
# This function will return the current list of tasks as JSON
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)  # Convert the Python list into JSON and return

# Define a route for HTTP POST requests at the URL "/tasks"
# This function allows a client to add a new task to the list
@app.route('/tasks', methods=['POST'])
def add_tasks():
    task = request.get_json()  # Extract JSON data from the request body
    tasks.append(task)         # Add the new task to the in-memory list
    return jsonify(tasks), 201 # Return the updated task list and status code 201 (Created)

# Start the Flask development server when this file is run directly
# 'debug=True' enables hot reloading and detailed error messages
if __name__ == '__main__':
    app.run(debug=True)

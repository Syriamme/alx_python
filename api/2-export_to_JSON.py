#!/usr/bin/python3

"""
Module: employee_todo_export.py

This module fetches and exports the tasks owned by an employee from an external API to a JSON file.

Usage:
    python employee_todo_export.py <employee_id>

Arguments:
    - <employee_id>: The ID of the employee whose tasks need to be exported.

Example Usage:
    python employee_todo_export.py 1

This script fetches the employee's details and their associated tasks from the JSONPlaceholder API
based on the provided employee_id. It then exports these tasks in a JSON file named USER_ID.json,
where USER_ID is the employee's ID.

Functions:
    - export_employee_todo_data(employee_id):
        Fetches employee details and their associated tasks, exports them to a JSON file,
        and prints a success message.

Dependencies:
    - json: For handling JSON data.
    - sys: For handling command-line arguments and exit codes.
    - urllib.request: For making HTTP requests to the external API.
"""


import json
import requests
import sys

dimport json
import sys
import urllib.request

def get_employee_todo_progress(employee_id):
  """Fetches the employee's TODO list and progress from the JSON Placeholder API.

  Args:
    employee_id: The ID of the employee.

  Returns:
    A list of tasks, where each task is a dictionary with the following keys:
      * task: The title of the task.
      * completed: Whether the task is completed.
      * username: The name of the employee who owns the task.
  """

  base_url = "https://jsonplaceholder.typicode.com"
  employee_url = f"{base_url}/users/{employee_id}"
  todo_url = f"{base_url}/users/{employee_id}/todos"

  try:
    with urllib.request.urlopen(employee_url) as response:
      if response.getcode() == 200:
        employee_data = json.loads(response.read().decode())
        employee_name = employee_data["name"]
      else:
        print(f"Error: Unable to fetch employee details. Status Code: {response.getcode()}")
        return

    with urllib.request.urlopen(todo_url) as response:
      if response.getcode() == 200:
        todo_data = json.loads(response.read().decode())
      else:
        print(f"Error: Unable to fetch TODO list. Status Code: {response.getcode()}")
        return

    # Create a list of tasks, with each task being a dictionary with the required keys.
    tasks = []
    for task in todo_data:
      tasks.append({
        "task": task["title"],
        "completed": task["completed"],
        "username": employee_name
      })

    return tasks

  except urllib.error.URLError as e:
    print(f"Error: {e}")
    return

def export_employee_todo_progress_to_json(employee_id, tasks):
  """Exports the employee's TODO list and progress to a JSON file.

  Args:
    employee_id: The ID of the employee.
    tasks: A list of tasks, where each task is a dictionary with the following keys:
      * task: The title of the task.
      * completed: Whether the task is completed.
      * username: The name of the employee who owns the task.
  """

  # Create a JSON object with the employee's ID and tasks.
  json_data = {
    "USER_ID": employee_id,
    "tasks": tasks
  }

  # Write the JSON data to a file.
  with open(f"{employee_id}.json", "w") as f:
    json.dump(json_data, f)


if __name__ == "__main__":
  if len(sys.argv) != 2:
    print("Usage: python script.py <employee_id>")
    sys.exit(1)

  try:
    employee_id = int(sys.argv[1])

    # Get the employee's TODO list and progress.
    tasks = get_employee_todo_progress(employee_id)

    # Export the employee's TODO list and progress to a JSON file.
    export_employee_todo_progress_to_json(employee_id, tasks)

  except ValueError:
    print("Please enter a valid integer for the employee ID.")

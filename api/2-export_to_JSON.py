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
    - requests: For making HTTP requests to the external API.
"""

import json
import requests
import sys

def export_employee_todo_data(employee_id):
    """Fetches the employee's TODO list and progress from the JSON Placeholder API,
    and exports the data to a JSON file.

    Args:
        employee_id: The ID of the employee.

    This function fetches the employee's tasks and details, and exports them to a JSON file
    named USER_ID.json, where USER_ID is the employee's ID.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/users/{employee_id}/todos"

    try:
        response = requests.get(employee_url)
        employee_data = json.loads(response.content.decode())
        employee_name = employee_data["username"]

        response = requests.get(todo_url)
        todo_data = json.loads(response.content.decode())

        tasks = []
        for task in todo_data:
            task_entry = {
                "task": task["title"],
                "completed": task["completed"],
                "username": employee_name
            }
            tasks.append(task_entry)

        json_data = {employee_id: tasks}

        filename = f"{employee_id}.json"

        with open(filename, "w") as f:
            json.dump(json_data, f)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = sys.argv[1]
        export_employee_todo_data(employee_id)
    except ValueError:
        print("Please enter a valid integer for the employee ID.")

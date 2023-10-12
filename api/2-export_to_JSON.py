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
import sys
import requests

def export_employee_todo_data(employee_id):
    """
    Fetches the employee's TODO list and progress from the JSON Placeholder API
    and exports them to a JSON file.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/users/{employee_id}/todos"

    try:
        # Fetch employee details
        response = requests.get(employee_url)
        response.raise_for_status()
        employee_data = response.json()
        employee_name = employee_data["username"]

        # Fetch TODO list
        response = requests.get(todo_url)
        response.raise_for_status()
        todo_data = response.json()

        # Create a list of tasks with the required keys
        tasks = []
        for task in todo_data:
            tasks.append({
                "task": task["title"],
                "completed": task["completed"],
                "username": employee_name
            })

        # Create a JSON object with the employee's ID and tasks
        json_data = {str(employee_id): tasks}

        # Write the JSON data to a file
        with open(f"{employee_id}.json", "w") as f:
            json.dump(json_data, f)

        print(f"Tasks for employee {employee_id} exported to {employee_id}.json")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])

        # Export the employee's TODO list and progress to a JSON file
        export_employee_todo_data(employee_id)

    except ValueError:
        print("Please enter a valid integer for the employee ID.")

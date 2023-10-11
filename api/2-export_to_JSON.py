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
    # Define the base URL and URLs for fetching employee and TODO data
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/users/{employee_id}/todos"

    try:
        # Fetch employee data using requests
        employee_response = requests.get(employee_url)
        if employee_response.status_code == 200:
            employee_data = employee_response.json()
            employee_name = employee_data.get("username")
        else:
            print(f"Error: Unable to fetch employee details. Status Code: {employee_response.status_code}")
            return

        # Fetch TODO list data using requests
        todo_response = requests.get(todo_url)
        if todo_response.status_code == 200:
            todo_data = todo_response.json()
        else:
            print(f"Error: Unable to fetch TODO list. Status Code: {todo_response.status_code}")
            return

        # Create a list to store tasks
        tasks = []

        for task in todo_data:
            task_info = {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": employee_name
            }
            tasks.append(task_info)

        # Create the final user data dictionary
        user_data = {str(employee_id): tasks}

        # Export data to JSON file
        with open(f"{employee_id}.json", "w") as json_file:
            json.dump(user_data, json_file)


    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Check for the correct number of command-line arguments
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        # Get the employee ID from the command-line argument
        employee_id = int(sys.argv[1])
        export_employee_todo_data(employee_id)
    except ValueError:
        print("Please enter a valid integer for the employee ID.")

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
import urllib.request

def export_employee_todo_data(employee_id):
    # Define the base URL and URLs for fetching employee and TODO data
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    try:
        # Fetch employee data
        with urllib.request.urlopen(employee_url) as response:
            if response.getcode() == 200:
                employee_data = json.loads(response.read().decode())
                employee_name = employee_data.get("username")
            else:
                print(f"Error: Unable to fetch employee details. Status Code: {response.getcode()}")
                return

        # Fetch TODO list data
        with urllib.request.urlopen(todo_url) as response:
            if response.getcode() == 200:
                todo_data = json.loads(response.read().decode())
            else:
                print(f"Error: Unable to fetch TODO list. Status Code: {response.getcode()}")
                return

        # Create a dictionary to store user data and tasks
        user_data = {
            str(employee_id): [
                {
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": employee_name
                }
                for task in todo_data
            ]
        }

        # Export user data to a JSON file with an indent of 4 spaces
        with open(f"{employee_id}.json", 'w') as outfile:
            json.dump(user_data, outfile, indent=4)

    except urllib.error.URLError as e:
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

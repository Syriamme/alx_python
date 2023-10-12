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

def export_employee_todo_data(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/users/{employee_id}/todos"

    #fetching employee details
    try:
        employee_response = requests.get(employee_url)
        if employee_response.status_code == 200:
            employee_data = employee_response.json()
            employee_name = employee_data.get("username")
        else:
            print(f"Error: Unable to fetch employee details. Status Code: {employee_response.status_code}")
            return
        
    #fetching to do list
        todo_response = requests.get(todo_url)
        if todo_response.status_code == 200:
            todo_data = todo_response.json()
        else:
            print(f"Error: Unable to fetch TODO list. Status Code: {todo_response.status_code}")
            return

        # a list to store tasks
        tasks = []

        for task in todo_data:
            task_info = {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": employee_name
            }
            tasks.append(task_info)

        with open(f"{employee_id}.json", "w") as json_file:
            json.dump({employee_id: tasks}, json_file)


    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        # Get the employee ID from the command-line argument
        employee_id = sys.argv[1]
        export_employee_todo_data(employee_id)
    except ValueError:
        print("Please enter a valid integer for the employee ID.")

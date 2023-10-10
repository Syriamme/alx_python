#!/usr/bin/python3

"""
Module: employee_todo_progress.py

This module fetches and records the tasks owned by an employee from an external API and stores them in a JSON file.

Usage:
    python employee_todo_progress.py <employee_id>

Arguments:
    - <employee_id>: The ID of the employee whose tasks need to be recorded.

Example Usage:
    python employee_todo_progress.py 1

This script fetches the employee's details and their associated tasks from the JSONPlaceholder API
based on the provided employee_id. It then records these tasks in a JSON file named USER_ID.json,
where USER_ID is the employee's ID.

Functions:
    - get_employee_todo_progress(employee_id):
        Fetches employee details and their associated tasks, records them in a JSON file,
        and prints the progress.

Dependencies:
    - json: For handling JSON data.
    - sys: For handling command-line arguments and exit codes.
    - urllib.request: For making HTTP requests to the external API.
"""

import json
import sys
import urllib.request

def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    try:
        with urllib.request.urlopen(employee_url) as response:
            if response.getcode() == 200:
                employee_data = json.loads(response.read().decode())
                employee_name = employee_data["username"]
            else:
                print(f"Error: Unable to fetch employee details. Status Code: {response.getcode()}")
                return

        with urllib.request.urlopen(todo_url) as response:
            if response.getcode() == 200:
                todo_data = json.loads(response.read().decode())
            else:
                print(f"Error: Unable to fetch TODO list. Status Code: {response.getcode()}")
                return

        # Create a list to store tasks
        tasks = []

        for task in todo_data:
            task_info = {
                "task": task['title'],
                "completed": task['completed'],
                "username": employee_name
            }
            tasks.append(task_info)

        # Export data to JSON file as a list
        with open(f"{employee_id}.json", "w") as json_file:
            json.dump(tasks, json_file, indent=4)

        print(f"Employee {employee_name} is done with tasks({len(tasks)}):")

        for task in tasks:
            if task["completed"]:
                print(f"\t {task['task']}")

    except urllib.error.URLError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Please enter a valid integer for the employee ID.")

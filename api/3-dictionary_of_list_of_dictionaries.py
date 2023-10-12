#!/usr/bin/python3

"""
Module: employee_todo_export.py

This module defines functions to retrieve and export tasks of employees from an external API to a JSON file.

Functions:
    - get_employee_todo_progress(employee_id):
        Fetches employee details and their associated tasks from an external API.
        
        Args:
            - employee_id (int): The unique ID of the employee whose tasks you want to retrieve.
        
        Returns:
            - list or None: A list containing dictionaries for each task of the employee. Returns None in case of errors.

    - export_all_employees_tasks():
        Iterates through available employee IDs, retrieves their tasks, and exports the data to a JSON file.
        The JSON file is named "todo_all_employees.json" and follows a specific format.

Dependencies:
    - json: Used for handling JSON data.
    - urllib.request: Utilized to make HTTP requests to an external API.

Example Usage:
    To export tasks for an employee with ID 1, run the script as follows:
    python employee_todo_export.py 1

Notes:
    - The base URL for the external API is "https://jsonplaceholder.typicode.com".
    - Completed tasks are identified based on the "completed" field in the task data.
    - The exported JSON file "todo_all_employees.json" contains tasks for multiple employees, organized by user IDs.
    - The script will stop fetching tasks once it encounters an error while fetching an employee's data.

"""

import json
import urllib.request

def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/users/{employee_id}/todos"

    try:
        with urllib.request.urlopen(employee_url) as response:
            if response.getcode() == 200:
                employee_data = json.loads(response.read().decode())
                employee_name = employee_data["username"]
            else:
                print(f"Error: Unable to fetch employee details. Status Code: {response.getcode()}")
                return None

        with urllib.request.urlopen(todo_url) as response:
            if response.getcode() == 200:
                todo_data = json.loads(response.read().decode())
            else:
                print(f"Error: Unable to fetch TODO list. Status Code: {response.getcode()}")
                return None

        return [{"username": employee_name, "task": task["title"], "completed": task["completed"]} for task in todo_data]

    except urllib.error.URLError as e:
        print(f"Error: {e}")
        return None

def export_all_employee_tasks_to_json():
    all_employees_tasks = {}

    for employee_id in range(1, 11):
        employee_tasks = get_employee_todo_progress(employee_id)

        if employee_tasks:
            user_id = f"{employee_id}"
            all_employees_tasks[user_id] = employee_tasks

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_employees_tasks, json_file)

if __name__ == "__main__":
    export_all_employee_tasks_to_json()

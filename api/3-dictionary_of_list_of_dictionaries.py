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
import requests
import sys
def get_employee_todo_progress(employee_id):
    """
    Fetches the employee's TODO list and progress from the JSON Placeholder API.

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
        response = requests.get(employee_url)
        if response.status_code == 200:
            employee_data = response.json()
            employee_name = employee_data["name"]
        else:
            print(f"Error: Unable to fetch employee details. Status Code: {response.status_code}")
            return

        response = requests.get(todo_url)
        if response.status_code == 200:
            todo_data = response.json()
        else:
            print(f"Error: Unable to fetch TODO list. Status Code: {response.status_code}")
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

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return

def export_employee_todo_progress_to_json(employee_id, tasks):
    """
    Exports the employee's TODO list and progress to a JSON file.

    Args:
        employee_id: The ID of the employee.
        tasks: A list of tasks, where each task is a dictionary with the following keys:
          * task: The title of the task.
          * completed: Whether the task is completed.
          * username: The name of the employee who owns the task.
    """
    # Create a JSON object with the employee's ID and tasks.
    json_data = {
        str(employee_id): tasks
    }

    # Write the JSON data to a file.
    with open(f"{employee_id}.json", "w") as f:
        json.dump(json_data, f)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1)

        # Get the employee's TODO list and progress.
        tasks = get_employee_todo_progress(employee_id)

        # Export the employee's TODO list and progress to a JSON file.
        export_employee_todo_progress_to_json(employee_id, tasks)

    except ValueError:
        print("Please enter a valid integer for the employee ID.")

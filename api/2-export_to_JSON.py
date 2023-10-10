#!/usr/bin/python3

import json
import sys
import urllib.request

def export_employee_todo_progress_to_json(employee_id, filename):
    """
    Exports employee TODO progress to a JSON file.

    Args:
        employee_id (int): The ID of the employee.
        filename (str): The filename of the JSON file.
    """
    employee_name = get_employee_name(employee_id)
    todo_data = get_employee_todo_data(employee_id)

    data_to_export = {
        "USER_ID": [
            {"task": task["title"], "completed": task["completed"], "username": employee_name}
            for task in todo_data
        ]
    }

    with open(filename, "w") as json_file:
        json.dump(data_to_export, json_file, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        filename = f"{employee_id}.json"
        export_employee_todo_progress_to_json(employee_id, filename)
    except ValueError:
        print("Please enter a valid integer for the employee ID.")

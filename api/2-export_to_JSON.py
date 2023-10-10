#!/usr/bin/python3

import json
import sys
import urllib.request

def export_employee_todo_progress_to_json(employee_id, filename):
    """Exports employee TODO progress to a JSON file.

    Args:
        employee_id: The ID of the employee.
        filename: The filename of the JSON file.
    """

    data = {"USER_ID": []}

    employee_name = get_employee_name(employee_id)
    todo_data = get_employee_todo_data(employee_id)

    for task in todo_data:
        task_entry = {
            "task": task["title"],
            "completed": task["completed"],
            "username": employee_name
        }
        data["USER_ID"].append(task_entry)

    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        export_employee_todo_progress_to_json(employee_id, f"{employee_id}.json")
    except ValueError:
        print("Please enter a valid integer for the employee ID.")

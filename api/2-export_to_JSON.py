#!/usr/bin/python3


import json
import sys
import urllib.request


def export_employee_todo_data(employee_id):
    """
    Export employee's TODO data to a JSON file.

    This function fetches employee information and their tasks from a remote API,
    constructs a JSON representation of the data, and saves it to a file named
    after the employee's ID.

    Args:
        employee_id (int): The ID of the employee for whom to export the TODO data.

    Returns:
        None

    Raises:
        urllib.error.URLError: If there is an issue with the URL request.
    """
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    try:
        with urllib.request.urlopen(employee_url) as response:
            if response.getcode() == 200:
                employee_data = json.loads(response.read().decode())
                employee_name = employee_data["name"]
            else:
                print(f"Error: Unable to fetch employee details. Status Code: {response.getcode()}")
                return

        with urllib.request.urlopen(todo_url) as response:
            if response.getcode() == 200:
                todo_data = json.loads response.read().decode())
            else:
                print(f"Error: Unable to fetch TODO list. Status Code: {response.getcode()}")
                return

        user_data = {
            str(employee_id): [
                {"task": task["title"], "completed": task["completed"], "username": employee_name}
                for task in todo_data
            ]
        }

        with open(f"{employee_id}.json", 'w') as outfile:
            json.dump(user_data, outfile, indent=4)

        print(f"Data exported to {employee_id}.json")

    except urllib.error.URLError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        export_employee_todo_data(employee_id)
    except ValueError:
        print("Please enter a valid integer for the employee ID.")

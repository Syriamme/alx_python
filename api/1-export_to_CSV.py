#!/usr/bin/python3

import csv
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
                employee_name = employee_data["username"]  # Use "username" instead of "name"
            else:
                print(f"Error: Unable to fetch employee details. Status Code: {response.getcode()}")
                return

        with urllib.request.urlopen(todo_url) as response:
            if response.getcode() == 200:
                todo_data = json.loads(response.read().decode())
            else:
                print(f"Error: Unable to fetch TODO list. Status Code: {response.getcode()}")
                return

        # Create a CSV file and write the data to it
        csv_filename = f"{employee_id}.csv"
        with open(csv_filename, mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

            for task in todo_data:
                csv_writer.writerow([employee_id, employee_name, task['completed'], task['title']])
        
        print(f"Data exported to {csv_filename}.")
        return len(todo_data)  # Return the number of tasks

    except urllib.error.URLError as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        num_tasks = get_employee_todo_progress(employee_id)
        if num_tasks is not None:
            print(f"Number of tasks in CSV: {num_tasks}")  # Print the number of tasks
    except ValueError:
        print("Please enter a valid integer for the employee ID.")

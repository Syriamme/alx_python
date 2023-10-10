#!/usr/bin/python3

import urllib.request
import json

def get_employee_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"

    employee_url = f"{base_url}/users/{employee_id}"
    todo_url = f"{base_url}/todos?userId={employee_id}"

    try:
        with urllib.request.urlopen(employee_url) as response:
            employee_data = json.loads(response.read().decode())
        
        with urllib.request.urlopen(todo_url) as response:
            todo_data = json.loads(response.read().decode())

        total_tasks = len(todo_data)
        
        completed_tasks = 0
        for task in todo_data:
            if task['completed']:
                completed_tasks += 1
                print(f"Employee {employee_data['name']} is done with tasks ({completed_tasks}/{total_tasks}):")
        
        for task in todo_data:
            if task['completed']:
                print(f"\t{task['title']}")

    except urllib.error.URLError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    try:
        employee_id = int(input("Enter the employee ID: "))
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Please enter a valid integer for the employee ID.")

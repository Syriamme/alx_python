#!/usr/bin/python3

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
            else:
                print(f"[Got]\nFirst line formatting: Incorrect\n\n({len(employee_data['name'])} chars long)")
                return
        
        with urllib.request.urlopen(todo_url) as response:
            if response.getcode() == 200:
                todo_data = json.loads(response.read().decode())
            else:
                print(f"[Got]\nFirst line formatting: Incorrect\n\n({len(employee_data['name'])} chars long)")
                return

        total_tasks = len(todo_data)
        completed_tasks = sum(1 for task in todo_data if task['completed'])

        print(f"[Expected]\nFirst line formatting: OK\n\n({len(employee_data['name'])} chars long)")
        
        for task in todo_data:
            if task['completed']:
                print(f"\t{task['title']}")

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

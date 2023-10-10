"""
This script retrieves and displays information on an employee's TODO list
using REST API. It accepts employee ID as a param and provides details
about the employee's completed tasks alongside their titles.

Usage: 0-gather_data_from_an_API.py <employee_id>
"""

import requests  # Responsible for making HTML requests
import sys       # Handles CL args


def get_employee_info(employee_id):
    """
    Retrieve & display an employee's TODO list progress

    Args:
        employee_id(int): The employee's ID

    Returns:
        None
    """

    # Define the base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Send a GET request to retrieve employee details
    employee_response = requests.get(f"{base_url}/users/{employee_id}")

    # Check if the request was successful
    if employee_response.status_code != 200:
        print("Missing Employee Details")
        return

    employee_data = employee_response.json()
    employee_name = employee_data["name"]

    # Send a GET request to retrieve the employee TODO list details
    todos_response = requests.get(f"{base_url}/users/{employee_id}/todos")

    # Check if the request is successful
    if todos_response.status_code != 200:
        print("Missing TODO List")
        return

    todos_data = todos_response.json()

    # Enumerate the number of completed and total tasks
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for todo in todos_data if todo["completed"])

    # Display employee details and task titles
    print(f"Employee {employee_name} is done with "
          f"{completed_tasks}/{total_tasks} tasks:")
    for todo in todos_data:
        if todo["completed"]:
            print(f"\t{todo['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_info(employee_id)
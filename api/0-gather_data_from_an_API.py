#!/usr/bin/python3

import json
import sys
import urllib.request

def export_employee_todo_progress_to_csv(employee_id, filename):
  """Exports employee TODO progress to a CSV file.

  Args:
    employee_id: The ID of the employee.
    filename: The filename of the CSV file.
  """

  with open(filename, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

    employee_name = get_employee_name(employee_id)
    todo_data = get_employee_todo_data(employee_id)

    for task in todo_data:
      writer.writerow([employee_id, employee_name, task["completed"], task["title"]])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Please enter a valid integer for the employee ID.")

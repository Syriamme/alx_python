import json
import urllib.request

def get_all_employee_tasks():
    base_url = "https://jsonplaceholder.typicode.com"
    users_url = f"{base_url}/users"

    try:
        with urllib.request.urlopen(users_url) as response:
            if response.getcode() == 200:
                users_data = json.loads(response.read().decode())
            else:
                print(f"Error: Unable to fetch employee details. Status Code: {response.getcode()}")
                return

        all_employee_tasks = {}

        for user in users_data:
            user_id = user["id"]
            username = user["username"]
            todo_url = f"{base_url}/todos?userId={user_id}"

            with urllib.request.urlopen(todo_url) as response:
                if response.getcode() == 200:
                    todo_data = json.loads(response.read().decode())
                else:
                    print(f"Error: Unable to fetch TODO list for user {username}. Status Code: {response.getcode()}")
                    continue

            tasks = [{"username": username, "task": task["title"], "completed": task["completed"]} for task in todo_data]
            all_employee_tasks[user_id] = tasks

        with open("todo_all_employees.json", "w") as outfile:
            json.dump(all_employee_tasks, outfile)

    except urllib.error.URLError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_all_employee_tasks()

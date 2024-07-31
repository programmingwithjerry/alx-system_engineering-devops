#!/usr/bin/python3
import requests
import sys


def fetch_employee_data(employee_id):
    """
    Fetches and displays TODO list progress for a given employee ID.

    Args:
        employee_id (int): The ID of the employee whose TODO list
      is to be fetched.

    Prints:
        - Employee's name and TODO list progress in the format:
          "Employee EMPLOYEE_NAME is done with tasks(
           NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):"
        - List of completed task titles, each preceded by a tab and space.
    """
    # Define the URLs for the API
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos"
    
    # Fetch user data
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print("Error: Unable to fetch user data")
        return

    # Fetch TODOs data
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print("Error: Unable to fetch TODOs data")
        return

    user_data = user_response.json()
    todos_data = todos_response.json()
    
    # Filter TODOs for the given employee ID
    employee_todos = [todo for todo in todos_data if \
      todo['userId'] == employee_id]

    # Get employee name
    employee_name = user_data.get('name')
    
    # Calculate number of completed and total tasks
    total_tasks = len(employee_todos)
    completed_tasks = sum(1 for todo in employee_todos if todo['completed'])
    
    # Print the progress
    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
    
    # Print completed task titles
    for todo in employee_todos:
        if todo['completed']:
            print(f"\t {todo['title']}")


if __name__ == "__main__":
    """
    Main function that handles command-line arguments and invokes the data fetching function.
    Expects one argument: the employee ID.
    """
    if len(sys.argv) != 2:
        print("Usage: ./script.py EMPLOYEE_ID")
        sys.exit(1)
    
    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Error: Employee ID must be an integer")
        sys.exit(1)
    
    fetch_employee_data(employee_id)

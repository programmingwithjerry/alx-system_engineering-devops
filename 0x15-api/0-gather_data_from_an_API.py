#!/usr/bin/python3
'''
Fetch and display TODO list progress for a specified employee ID.
'''

if __name__ == '__main__':
    import requests
    import sys

    # Initialize counters and storage for completed task titles
    completed_task_count = 0
    completed_tasks = []

    # Get the employee ID from command-line arguments
    employee_id = sys.argv[1]

    # Fetch user data to get the employee's username
    user_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    user_data = user_response.json()
    employee_username = user_data.get("username")

    # Fetch TODOs data for the specified employee ID
    todos_response = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
    todos_list = todos_response.json()

    # Process each TODO item
    for todo in todos_list:
        if todo.get('completed'):
            completed_tasks.append(todo.get('title'))
            completed_task_count += 1

    # Calculate total number of tasks
    total_task_count = len(todos_list)

    # Output the progress summary
    print(f'Employee {employee_username} is done with tasks({completed_task_count}/{total_task_count}):')

    # Print the titles of completed tasks
    for task in completed_tasks:
        print(f'\t {task}')

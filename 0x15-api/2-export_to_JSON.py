#!/usr/bin/python3
'''
Fetch and save a given employee's TODO list progress in JSON format.
'''

if __name__ == '__main__':
    import json
    import requests
    import sys

    # Retrieve the employee ID from command-line arguments
    employee_id = sys.argv[1]

    # Fetch employee information from the API
    user_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    user_data = user_response.json()
    username = user_data.get('username')

    # Fetch TODO list data for the specified employee ID
    todos_response = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
    todos_list = todos_response.json()

    # Prepare JSON structure for output
    tasks_info = []
    for todo in todos_list:
        task_info = {
            'task': todo.get('title'),
            'completed': todo.get('completed'),
            'username': username
        }
        tasks_info.append(task_info)

    # Organize the final JSON output
    output_data = {employee_id: tasks_info}

    # Write the JSON data to a file
    with open(f'{employee_id}.json', 'w') as json_file:
        json.dump(output_data, json_file)

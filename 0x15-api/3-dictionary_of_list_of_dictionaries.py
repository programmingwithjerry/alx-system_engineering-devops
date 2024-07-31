#!/usr/bin/python3
'''
Fetch and save TODO list progress for all employees in JSON format.
'''

if __name__ == '__main__':
    import json
    import requests

    # Fetch all users from the API and prepare dictionaries for storing user info
    users_response = requests.get('https://jsonplaceholder.typicode.com/users')
    users_data = users_response.json()
    todo_progress = {}
    username_map = {}

    # Initialize dictionaries with user IDs and usernames
    for user in users_data:
        user_id = user.get('id')
        todo_progress[user_id] = []
        username_map[user_id] = user.get('username')

    # Fetch all TODO items from the API
    todos_response = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos_data = todos_response.json()

    # Populate the TODO progress dictionary with task details
    for todo in todos_data:
        task_info = {}
        user_id = todo.get('userId')
        task_info['task'] = todo.get('title')
        task_info['username'] = username_map.get(user_id)
        task_info['completed'] = todo.get('completed')
        todo_progress[user_id].append(task_info)

    # Write the collected data to a JSON file
    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(todo_progress, json_file)

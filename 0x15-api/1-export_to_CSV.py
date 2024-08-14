#!/usr/bin/python3
'''
Generate a CSV file with TODO list details for a specified employee ID.
'''

if __name__ == '__main__':
    import csv
    import requests
    import sys

    # Initialize variables to store TODO list details
    completed_task_count = 0
    task_titles = []

    # Retrieve the employee ID from the command-line arguments
    employee_id = sys.argv[1]

    # Fetch employee information from the API
    user_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    user_data = user_response.json()

    # Fetch TODO list data for the given employee ID
    todos_response = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
    todos_list = todos_response.json()

    # Create and write to a CSV file with the employee's TODO list information
    with open(f'{employee_id}.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for todo in todos_list:
            csv_writer.writerow([user_data['id'], user_data['username'],
                                todo['completed'], todo['title']])

#!/usr/bin/python3
"""
Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys


def getData(id=None):
    """
    Function to get data progress of user

    Args
        URL: URL of the resource to get data
        name: name of the user selected
        total_task: total task of the user
        done_task: task completed by user
        user_data: info about user
    """
    URL = 'https://jsonplaceholder.typicode.com/users'
    user_data = requests.get(URL + '/{}'.format(id)).json()
    name = user_data.get('name')

    user_task = requests.get(URL + '/{}/todos'.format(id)).json()
    total_task = len(user_task)
    done_task = 0

    # Check for completed task of user
    for value in user_task:
        if value.get('completed'):
            done_task += 1

    print('Employee {} is done with tasks({}/{}):'
          .format(name, done_task, total_task))

    # Print completed task of user
    for task in user_task:
        if task.get('completed'):
            print('\t {}'.format(task.get('title')))


if __name__ == '__main__':
    """
    Call to getData function
    """
    getData(sys.argv[1])

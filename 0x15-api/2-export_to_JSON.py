#!/usr/bin/python3
"""
Python script to export data in the JSON format.
"""
import csv
import json
import requests
import sys


def exportJSON(id=None):
    """
    Function to export data of user to JSON file.

    Args
        URL: URL of the resource to get data
        user_data: info about selected user
        user_name: name of the user selected
        user_task: tasks of the user
        data: is the full data to convert in JSON file
        values: is the list that contains the dict of values
        path: is used to create the name of the JSON file.
    """
    URL = 'https://jsonplaceholder.typicode.com/users'
    user_data = requests.get(URL + '/{}'.format(id)).json()
    user_name = user_data.get('username')

    user_task = requests.get(URL + '/{}/todos'.format(id)).json()

    data = dict()
    values = []

    for value in user_task:
        items = dict()
        items['task'] = value.get('title')
        items['completed'] = value.get('completed')
        items['username'] = user_name
        values.append(items)

    data[id] = values
    # print(data)

    # Create data of the user to export a JSON file.
    path = id + '.json'
    with open(path, "w") as myfile:
        json.dump(data, myfile)


if __name__ == '__main__':
    """
    Call to exportData function
    """
    exportJSON(sys.argv[1])

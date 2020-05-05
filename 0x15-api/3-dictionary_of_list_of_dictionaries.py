#!/usr/bin/python3
"""
Python script to export full data in the JSON format.
"""
import csv
import json
import requests


def exportFullJSON():
    """
    Function to export full data users to JSON file.

    Args
        URL: URL of the resource to get data
        user_id: is the id of the user selected
        user_data: info about selected user
        user_name: name of the user selected
        user_task: tasks of the user
        data: is the full data to convert in JSON file
        values: is the list that contains the dict of values
        path: is used to create the name of the JSON file.
    """
    URL = 'https://jsonplaceholder.typicode.com/users'
    user_data = requests.get(URL).json()

    data = dict()

    if len(user_data) > 0:
        for user in user_data:
            user_id = user.get('id')
            user_name = user.get('username')
            user_task = requests.get(URL + '/{}/todos'.format(user_id)).json()
            values = []

            for value in user_task:
                items = dict()
                items['username'] = user_name
                items['task'] = value.get('title')
                items['completed'] = value.get('completed')
                values.append(items)

            data[user_id] = values
        # print(data)

        # Create collection data of all user to export a JSON file.
        with open("todo_all_employees.json", "w") as myfile:
            json.dump(data, myfile)


if __name__ == '__main__':
    """
    Call to exportFullJSON function
    """
    exportFullJSON()

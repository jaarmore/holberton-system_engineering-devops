#!/usr/bin/python3
"""
Python script to export data in the CSV format.
"""
import csv
import requests
import sys


def exportData(id=None):
    """
    Function to export data of user to CSV file.

    Args
        URL: URL of the resource to get data
        user_data: info about selected user
        user_id: id of the user selected
        user_name: name of the user selected
        user_task: task of the user
    """
    URL = 'https://jsonplaceholder.typicode.com/users'
    user_data = requests.get(URL + '/{}'.format(id)).json()
    user_name = user_data.get('username')

    user_task = requests.get(URL + '/{}/todos'.format(id)).json()

    # Create data of the user to export a CSV file.
    path = id + '.csv'
    with open(path, "w") as myfile:
        writer = csv.writer(myfile, delimiter=',', quoting=csv.QUOTE_ALL)
        full_data = []
        for value in user_task:
            data = []
            data.append(value.get('userId'))
            data.append(user_name)
            data.append(value.get('completed'))
            data.append(value.get('title'))
            writer.writerow(data)


if __name__ == '__main__':
    """
    Call to exportData function
    """
    exportData(sys.argv[1])

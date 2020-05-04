# 0x15. API


Old-school system administrators usually only know Bash and that is what they use to build their scripts. While Bash is perfectly fine for a lot of things, it can quickly get messy and not efficient compared to other programming languages. The new generation of system administrators, usually called SREs, are pretty much regular software engineers but instead of building products, they are managing systems. And one of the big differences with their predecessors is that they know more than just Bash scripting.

One popular way to expose an application and dataset is to use an API. Often, they are the public facing part of websites and micro-services so that allow outsiders to interact with them  access and modify their data. In this project, you will access employee data via an API to organize and export them to different data structures.


## General


+ What Bash scripting should not be used for
+ What is an API
+ What is a REST API
+ What are microservices
+ What is the CSV format
+ What is the JSON format
+ Pythonic Package and module name style
+ Pythonic Class name style
+ Significance of CapWords or CamelCase in Python


## Requirements


+ Allowed editors: `vi, vim, emacs`
+ All your files will be interpreted/compiled on `Ubuntu 14.04` LTS using `python3` (version 3.4.3)
+ All your files should end with a new line
+ The first line of all your files should be exactly `#!/usr/bin/python3`
+ Libraries imported in your Python files must be organized in alphabetical order
+ Your code should use the `PEP 8` style
+ All your files must be executable
+ The length of your files will be tested using `wc`


## Tasks


### [0. Gather data from an API](0-gather_data_from_an_API.py)
Python script that, using this REST API, for a given employee ID, returns information about his/her TODO list progress.


### [1. Export to CSV](1-export_to_CSV.py)
Python script to export data in the CSV format.


### [2. Export to JSON](2-export_to_JSON.py)
Python script to export data in the JSON format.


### [3. Dictionary of list of dictionaries](3-dictionary_of_list_of_dictionaries.py)
Python script to export data in the JSON format, file name must be: `todo_all_employees.json`.


## AUTHOR
**_Jackson Moreno_**

# 0x16. API advanced


Questions involving APIs are common for interviews. Sometimes theyre as simple as write a Python script that queries a given endpoint, sometimes they require you to use recursive functions and format/sort the results.

A great API to use for some practice is the `Reddit API.` Theres a lot of endpoints available, many that dont require any form of authentication, and theres tons of information to be parsed out and presented. Getting comfortable with API calls now can save you some face during technical interviews and even outside of the job market, you might find personal use cases to make your life a little bit easier.


## General


+ How to read API documentation to find the endpoints youre looking for
+ How to use an API with pagination
+ How to parse JSON results from an API
+ How to make a recursive API call
+ How to sort a dictionary by value


## Requirements


+ Allowed editors: `vi, vim, emacs`
+ All your files will be interpreted/compiled on `Ubuntu 14.04 LTS` using `python3` (version 3.4.3)
+ All your files should end with a new line
+ The first line of all your files should be exactly `#!/usr/bin/python3`
+ Libraries imported in your Python files must be organized in alphabetical order
+ Your code should use the `PEP 8` style
+ All your files must be executable
+ The length of your files will be tested using `wc`
+ All your modules should have a documentation `(python3 -c 'print(__import__("my_module").__doc__)')`
+ You must use the `Requests` module for sending `HTTP requests` to the `Reddit API`.


## Tasks


### [0. How many subs?](0-subs.py)
Function that queries the Reddit API and returns the number of subscribers (not active users, total subscribers) for a given subreddit. If an invalid subreddit is given, the function should return 0.


### [1. Top Ten](1-top_ten.py)
Function that queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.


### [2. Recurse it!](2-recurse.py)
Recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit, the function should return None.


## Author
**_Jackson Moreno_**

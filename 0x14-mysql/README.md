# 0x14. Mysql

In this project we learn about:

+ What is a primary-replica cluster
+ MySQL primary replica setup
+ Build a robust database backup strategy


## Requirements

+ Allowed editors: `vi, vim, emacs`
+ All your files will be interpreted on `Ubuntu 16.04 LTS`
+ All your files should end with a new line
+ All your Bash script files must be executable
+ Your Bash script must pass `Shellcheck` (version 0.3.7-5~ubuntu16.04.1 via apt-get) without any error
+ The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
+ The second line of all your Bash scripts should be a comment explaining what is the script doing


## Tasks

### 0. Install MySQL
Lets get MySQL installed on both your web-01 and web-02 servers.


### 1. Let us in!
Create a user and password for both MySQL databases which will allow the checker access to them.


### 2. If only you could see what I've seen with your eyes
Youll need to have a database with at least one table and one row in your primary MySQL server (web-01) to replicate from.


### 3. Quite an experience to live in fear, isn't it?
On your primary MySQL server (web-01), create a new user for the replica server.


### 4. Setup a Primary-Replica infrastructure using MySQL
Set up replica member on for your MySQL database.


### [5. MySQL backup](5-mysql_backup)
Write a Bash script that generates a MySQL dump and creates a compressed archive out of it.
[mysql_primary](4-mysql_configuration_primary), [mysql_replica](4-mysql_configuration_replica)


## AUTHOR
**_Jackson Moreno_**

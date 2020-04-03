# 0x0F. Load balancer
Lets improve our web stack so that there is redundancy for our web servers. This will allow us to be able to accept more traffic by doubling the number of web servers, and to make our infrastructure more reliable. If one web server fails, we will still have a second one to handle requests.

For this project, you will need to write Bash scripts to automate your work. All scripts must be designed to configure a brand new Ubuntu server to match the task requirements.

## Requirements

+ Allowed editors: `vi, vim, emacs`
+ All your files will be interpreted on `Ubuntu 16.04 LTS`
+ All your files should end with a new line
+ All your Bash script files must be executable
+ Your Bash script must pass `Shellcheck` (version 0.3.7) without any error
+ The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
+ The second line of all your Bash scripts should be a comment explaining what is the script doing

## Tasks

## [0. Double the number of webservers](0-custom_http_response-header)
Script that configure web-02 to be identical to web-01. Configure Nginx so that its HTTP response contains a custom header (on web-01 and web-02).

## [1. Install your load balancer](1-install_load_balancer)
Install and configure HAproxy on your lb-01 server.

## AUTHOR
**_Jackson Moreno_**

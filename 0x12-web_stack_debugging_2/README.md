# 0x12. Web stack debugging #2
The user `root` is, on Linux, the superuser. It can do anything it wants, thats a good and bad thing. A good practice is that one should never be logged in the `root` user, as if you fat finger a command and for example run `rm -rf /`, there is no comeback. Thats why it is preferable to run as a privileged user, meaning that the user also has the ability to perform tasks that the root user can do, just need to use a specific command that you need to discover.

## Requirements
+ All your files will be interpreted on `Ubuntu 14.04 LTS`
+ All your files should end with a new line
+ All your Bash script files must be executable
+ Your Bash scripts must pass `Shellcheck` without any error
+ Your Bash scripts must run without error
+ The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
+ The second line of all your Bash scripts should be a comment explaining what is the script doing.

## TASKS

### [0. Run software as another user](0-iamsomeonelese)
Script that accepts one argument run the `whoami` command under the user passed as an argument.

### [1. Run Nginx as Nginx](1-run_nginx_as_nginx)
Script that runs `nginx` server as `nginx` user.

## AUTHOR
**_Jackson Moreno_**

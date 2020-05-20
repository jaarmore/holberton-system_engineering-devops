# 0x18. Webstack monitoring
You cannot fix or improve what you cannot measure is a famous saying in the Tech industry. In the age of the data-ism, monitoring how our Software systems are doing is an important thing. In this project, we will implement one of many tools to measure what is going on our servers.

Web stack monitoring can be broken down into 2 categories:

+ Application monitoring: getting data about your running software and making sure it is behaving as expected
+ Server monitoring: getting data about your virtual or physical server and making sure they are not overloaded (could b.e CPU, memory, disk or network overload).


## Requirements

+ Allowed editors: `vi, vim, emacs`
+ All your files will be interpreted on `Ubuntu 16.04 LTS`
+ All your files should end with a new line
+ All your Bash script files must be executable
+ Your Bash script must pass `Shellcheck` (version 0.3.7) without any error
+ The first line of all your Bash scripts should be exactly `#!/usr/bin/env bash`
+ The second line of all your Bash scripts should be a comment explaining what is the script doing


## Tasks

### 0. Sign up for Datadog and install datadog-agent
Head to `https://www.datadoghq.com/` and sign up for a free Datadog account. When signing up, youll have the option of selecting statistics from your current stack that Datadog can monitor for you. 


### 1. Monitor some metrics
Set up some monitors within the Datadog dashboard to monitor and alert you of a few.

### [2. Create a dashboard](2-setup_datadog)
Create a dashboard with different metrics displayed in order to get a few different visualizations.


## Author
**_Jackson Moreno_**

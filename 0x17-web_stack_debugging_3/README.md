# 0x17. Web stack debugging #3


## Background Context
![alt text](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/293/d42WuBh.png "Stages of Debugging")

When debugging, sometimes logs are not enough. Either because the software is breaking in a way that was not expected and the error is not being logged, or because logs are not providing enough information. In this case, you will need to go down the stack, the good news is that this is something Holberton students can do :)

Wordpress is a very popular tool, it allows you to run blogs, portfolios, e-commerce and company websites It actually powers 26% of the web, so there is a fair chance that you will end up working with it at some point in your career.

Wordpress is usually run on LAMP (Linux, Apache, MySQL, and PHP), which is a very widely used set of tools.
The web stack you are debugging today is a Wordpress website running on a LAMP stack.


## Requirements

+ All your files will be interpreted on `Ubuntu 14.04 LTS`
+ All your files should end with a new line
+ Your Puppet manifests must pass `puppet-lint` version `2.1.1` without any errors
+ Your Puppet manifests must run without error
+ Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about
+ Your Puppet manifests files must end with the extension `.pp`
+ Files will be checked with `Puppet v3.4`


### Install puppet-lint

```
$ apt-get install -y ruby
$ gem install puppet-lint -v 2.1.1
```


## Tasks

### [0. Strace is your friend](0-strace_is_your_friend.pp)
Using `strace`, find out why Apache is returning a 500 error. Once you find the issue, fix it and then automate it using `Puppet`.


## Author
**_Jackson Moreno_**

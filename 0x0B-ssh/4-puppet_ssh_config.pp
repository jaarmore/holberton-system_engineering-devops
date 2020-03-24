# Set up your client SSH configuration file so that you can connect to a server without typing a password.

file_line { 'set_ssh_key':
    path => '/etc/ssh/ssh_config',
    line => 'IdentityFile ~/.ssh/holberton',
}

file_line { 'set_password_no':
    path => '/etc/ssh/ssh_config',
    line => 'PasswordAuthentication no',
}
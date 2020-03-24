# Using Puppet, create a manifest that kills a process named killmenow.

exec { 'killmenow':
    provider => 'shell',
    path     => '/usr/bin/',
    command  => '/usr/bin/pkill -f killmenow',
}
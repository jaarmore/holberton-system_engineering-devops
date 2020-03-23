# Using Puppet create a file in /tmp folder called holberton.

$file = 'holberton'
$str = 'I love Puppet'

file { "/tmp/${file}" :
    ensure  => 'present',
    owner   => 'www-data',
    group   => 'www-data',
    mode    => '0744',
    content => $str,
}
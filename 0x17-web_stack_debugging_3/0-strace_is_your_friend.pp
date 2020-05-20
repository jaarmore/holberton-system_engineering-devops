# Find out why Apache is returning a 500 error.
# Once you find the issue, fix it and then automate it using Puppet

# fix apache2
exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => ['/bin', '/usr/bin', '/usr/sbin']
}

# restart apache2
service { 'restart-apache2':
  name       => 'apache2',
  hasrestart => true
}

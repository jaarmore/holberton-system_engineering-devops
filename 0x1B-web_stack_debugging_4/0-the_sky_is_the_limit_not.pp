# Tunning NGINX configuration, to accept a huge amount of request

# Settings worker_rlimit_nofile
exec { 'fix--for-nginx':
  command => "sed -i 's/-n 15/n 10000/g' /etc/default/nginx",
  path    => ['/bin', '/usr/bin', '/usr/sbin']
}

# restart NGINX server
service { 'restart-nginx':
  name       => 'nginx',
  hasrestart => true
}

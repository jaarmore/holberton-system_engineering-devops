# Tunning NGINX configuration, to accept a huge amount of request

# Tunning NGINX
exec { 'fix--for-nginx':
  command => 'sed -i s/worker_processes 4;/worker_processes 7;/g /etc/nginx/nginx.conf',
  path    => ['/bin', '/usr/bin', '/usr/sbin']
}

# restart NGINX server
service { 'restart-nginx':
  name       => 'nginx',
  hasrestart => true
}
# Boosts the Nginx server's capacity to manage more traffic

# Raise the file descriptor limit in the Nginx default configuration
exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin'
}

# Restart the Nginx service

exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}

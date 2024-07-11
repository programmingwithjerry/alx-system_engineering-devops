# Use Puppet to automate the creation of a custom HTTP response header

# Ensure the package list is up-to-date
exec { 'update':
  command => '/usr/bin/apt-get update',  # Run the apt-get update command
  path    => ['/usr/bin', '/usr/sbin'],  # Ensure correct PATH is used
  unless  => '/usr/bin/test -f /var/lib/apt/periodic/update-success-stamp',  # Skip if already updated
}

# Ensure Nginx is installed
package { 'nginx':
  ensure => 'present',  # Install Nginx if it is not already installed
}

# Add a custom HTTP header to the Nginx configuration
file_line { 'http_header':
  path  => '/etc/nginx/nginx.conf',  # Specify the Nginx configuration file
  match => 'http {',  # Match the line containing 'http {'
  line  => "http {\n\tadd_header X-Served-By \"${::hostname}\";",  # Insert the custom header line
  notify => Exec['run'],  # Notify the exec resource to restart Nginx
}

# Restart Nginx to apply the new configuration
exec { 'run':
  command     => '/usr/sbin/service nginx restart',  # Restart the Nginx service
  refreshonly => true,  # Only run when notified
  path        => ['/usr/bin', '/usr/sbin'],  # Ensure correct PATH is used
}

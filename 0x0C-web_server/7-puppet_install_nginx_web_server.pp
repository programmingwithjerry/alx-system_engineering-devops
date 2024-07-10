# Puppet manifest to install and configure Nginx with specified requirements

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Ensure Nginx service is enabled and running
service { 'nginx':
  ensure => running,
  enable => true,
}

# Define default server configuration
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => "
    server {
        listen 80 default_server;
        listen [::]:80 default_server;

        root /var/www/html;
        index index.html index.htm index.nginx-debian.html;

        server_name _;

        location / {
            try_files \$uri \$uri/ =404;
        }

        location /redirect_me {
            return 301 https://www.youtube.com/@innocentsax;
        }

        error_page 404 /404.html;
        location = /404.html {
            internal;
            root /var/www/html;
            echo 'Ceci n\\'est pas une page';
        }
    }
  ",
  require => Package['nginx'],
}

# Ensure index.html with "Hello World!" content exists
file { '/var/www/html/index.html':
  ensure  => file,
  content => "Hello World!\n",
  require => Package['nginx'],
}

# Notify Nginx to reload configuration upon changes
exec { 'nginx-reload':
  command     => '/bin/systemctl reload nginx',
  refreshonly => true,
  subscribe   => File['/etc/nginx/sites-available/default', '/var/www/html/index.html'],
}

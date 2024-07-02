# Client configuration for SSH

# Disable password authentication
# This block executes a command to append "PasswordAuthentication no"
# to the SSH client configuration file.
exec { 'Turn off passwd auth':
  command => 'bash -c "echo PasswordAuthentication no >> /etc/ssh/ssh_config"',
  path    => '/usr/bin:/usr/sbin:/bin'
}

# Specify the identity file
# This block executes a command to append "IdentityFile '~/.ssh/school'"
# to the SSH client configuration file.
exec { 'Declare identity file':
  command => 'bash -c "echo IdentityFile \'~/.ssh/school\' >> /etc/ssh/ssh_config"',
  path    => '/usr/bin:/usr/sbin:/bin'
}

# Enable public key authentication
# This block executes a command to append "PubkeyAuthentication yes"
# to the SSH client configuration file.
exec { 'Turn on pubkey auth':
  command => 'bash -c "echo PubkeyAuthentication yes >> /etc/ssh/ssh_config"',
  path    => '/usr/bin:/usr/sbin:/bin'
}


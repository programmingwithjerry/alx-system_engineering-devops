# Using Puppet, create a manifest that kills a process named killmenow.


exec { 'kill_killmenow_process':
  command => '/usr/bin/pkill killmenow',
  path    => '/usr/bin:/bin:/usr/sbin:/sbin',
  onlyif  => '/usr/bin/pgrep killmenow',
}


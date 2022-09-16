# create file /tmp/school
# permission 0744
# owner and group is www-data
# file contains I love Puppet
file { '/tmp/holberton':
    ensure  => file,
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data',
    content => 'I love Puppet'
}

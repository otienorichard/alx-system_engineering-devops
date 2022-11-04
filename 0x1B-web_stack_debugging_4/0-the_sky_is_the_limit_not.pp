# remove limit
exec {'remove limit':
    command => 'mv /etc/default/nginx /etc/default/nginx.bak; sudo service nginx restart',
    path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
    onlyif  => 'find /etc/default/nginx'
}

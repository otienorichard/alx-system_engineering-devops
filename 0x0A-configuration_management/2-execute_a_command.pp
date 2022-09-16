# kill a process named killmenow
exec {'kill process killmenow':
    command  => 'pkill killmenow',
    path     => '/usr/bin',
    onlyif   => 'pgrep killmenow',
    provider => shell
}

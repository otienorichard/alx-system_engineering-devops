# fix-wordpress
exec {'fix-wordpress':
    command => 'sed -i "s/class-wp-locale.phpp/class-wp-locale.php/" /var/www/html/wp-settings.php',
    path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
    onlyif  => 'cat /var/www/html/wp-settings.php | grep class-wp-locale.phpp'
}
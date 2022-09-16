# install puppet-lint (2.1.1)
package { 'puppet-lint-2.1.1':
    ensure   => '2.1.1',
    name     => 'puppet-lint',
    provider => 'gem'
}

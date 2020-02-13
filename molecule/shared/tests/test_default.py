import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def get_facts(host):
    return host.ansible("setup")["ansible_facts"]


# We could take an environment variable here from a build matrix?
def get_psql_version():
    return '9.6'


def get_config_path(host, type):
    facts = get_facts(host)

    psql = get_psql_version()

    if facts['ansible_os_family'] == 'Debian':
        if type == 'hba':
            return '/etc/postgresql/' + psql + '/main/pg_hba.conf'
        else:
            return '/etc/postgresql/' + psql + '/main/postgresql.conf'

    if type == 'hba':
        return '/var/lib/pgsql/' + psql + '/data/pg_hba.conf'

    return '/var/lib/pgsql/' + psql + '/data/postgresql.conf'


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


@pytest.mark.parametrize("config_type", [
    ("hba"),
    ("conf"),
])
def test_configuration_files(host, config_type):
    config_path = get_config_path(host, config_type)

    f = host.file(config_path)
    assert f.exists
    assert f.user == 'postgres'
    assert f.group == 'postgres'


def test_hba(host):
    config_path = get_config_path(host, 'hba')

    hba = host.file(config_path)
    assert hba.contains('0.0.0.0/0')
    assert hba.contains('::/0')

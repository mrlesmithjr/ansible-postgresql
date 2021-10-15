# ansible-postgresql

An [Ansible](https://www.ansible.com) role to install/configure [Postgresql](https://www.postgresql.org/)

## Build Status

### GitHub Actions

![Molecule Test](https://github.com/mrlesmithjr/ansible-postgresql/workflows/Molecule%20Test/badge.svg)

### Travis CI

[![Build Status](https://travis-ci.org/mrlesmithjr/ansible-postgresql.svg?branch=master)](https://travis-ci.org/mrlesmithjr/ansible-postgresql)

## Requirements

For any required Ansible roles, review:
[requirements.yml](requirements.yml)

If setting up replication:

`defaults/main.yml`

```yaml
postgresql_config: true
postgresql_enable_replication: true
postgresql_listen_addresses:
  - "*"
postgresql_replication:
  interface: enp0s8
  master: "{{ groups[postgresql_replication_group][0] }}"
  user: repluser
postgresql_replication_group: postgres_replication
```

## Role Variables

[defaults/main.yml](defaults/main.yml)

## Dependencies

## Example Playbook

[playbook.yml](playbook.yml)

## License

MIT

## Author Information

Larry Smith Jr.

- [@mrlesmithjr](https://twitter.com/mrlesmithjr)
- [mrlesmithjr@gmail.com](mailto:mrlesmithjr@gmail.com)
- [http://everythingshouldbevirtual.com](http://everythingshouldbevirtual.com)

> NOTE: Repo has been created/updated using [https://github.com/mrlesmithjr/cookiecutter-ansible-role](https://github.com/mrlesmithjr/cookiecutter-ansible-role) as a template.

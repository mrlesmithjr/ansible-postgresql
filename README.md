# ansible-postgresql

An [Ansible](https://www.ansible.com) role to install/configure [Postgresql](https://www.postgresql.org/)

## Requirements

Install [required](./requirements.yml) [Ansible] roles:

```bash
sudo ansible-galaxy install -r requirements.yml
```

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

[Role Defaults](defaults/main.yml)

## Dependencies

None

## Example Playbook

[Example Playbook](./playbook.yml)

## License

MIT

## Author Information

Larry Smith Jr.

- [@mrlesmithjr](https://www.twitter.com/mrlesmithjr)
- [EverythingShouldBeVirtual](http://everythingshouldbevirtual.com)
- [mrlesmithjr@gmail.com](mailto:mrlesmithjr@gmail.com)

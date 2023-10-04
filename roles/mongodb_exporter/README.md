
# Ansible Role:  `mongodb-exporter` 

Ansible role to install and configure [mongodb_exporter](https://github.com/prometheus/mongodb_exporter).


[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/bodsch/ansible-mongodb-exporter/main.yml?branch=main)][ci]
[![GitHub issues](https://img.shields.io/github/issues/bodsch/ansible-mongodb-exporter)][issues]
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/bodsch/ansible-mongodb-exporter)][releases]
[![Ansible Quality Score](https://img.shields.io/ansible/quality/50067?label=role%20quality)][quality]

[ci]: https://github.com/bodsch/ansible-mongodb-exporter/actions
[issues]: https://github.com/bodsch/ansible-mongodb-exporter/issues?q=is%3Aopen+is%3Aissue
[releases]: https://github.com/bodsch/ansible-mongodb-exporter/releases
[quality]: https://galaxy.ansible.com/bodsch/mongodb_exporter


If `latest` is set for `mongodb_exporter_version`, the role tries to install the latest release version.  
**Please use this with caution, as incompatibilities between releases may occur!**

The binaries are installed below `/usr/local/opt/mongodb_exporter/${mongodb_exporter_version}` and later linked to `/usr/bin`. 
This should make it possible to downgrade relatively safely.

The downloaded archive is stored on the Ansible controller, unpacked and then the binaries are copied to the target system.
The cache directory can be defined via the environment variable `CUSTOM_LOCAL_TMP_DIRECTORY`. 
By default it is `${HOME}/.cache/ansible/mongodb_exporter`.
If this type of installation is not desired, the download can take place directly on the target system. 
However, this must be explicitly activated by setting `mongodb_exporter_direct_download` to `true`.

## Requirements & Dependencies

Ansible Collections

- [bodsch.core](https://github.com/bodsch/ansible-collection-core)
- [bodsch.scm](https://github.com/bodsch/ansible-collection-scm)

```bash
ansible-galaxy collection install bodsch.core
ansible-galaxy collection install bodsch.scm
```
or
```bash
ansible-galaxy collection install --requirements-file collections.yml
```

## Operating systems

Tested on

* ArchLinux
* Debian based
    - Debian 10 / 11
    - Ubuntu 20.04

## Contribution

Please read [Contribution](CONTRIBUTING.md)

## Development,  Branches (Git Tags)

The `master` Branch is my *Working Horse* includes the "latest, hot shit" and can be complete broken!

If you want to use something stable, please use a [Tagged Version](https://github.com/bodsch/ansible-mongodb-exporter/tags)!

## Configuration

```yaml
mongodb_exporter_version: "0.14.0"

mongodb_exporter_release_download_url: https://github.com/prometheus/mongodb_exporter/releases

mongodb_exporter_system_user: mongodb_exporter
mongodb_exporter_system_group: mongodb_exporter

mongodb_exporter_direct_download: false

mongodb_exporter_service: {}

mongodb_exporter_credentials:
  client:
    hostname: ""
    port: ""
    socket: ""
    username: ""
    password: ""
```

### service configuration

```yaml
mongodb_exporter_service:
  log:
    level: info
    format: ""
  web:
    listen_address: "127.0.0.1:9104"
    telemetry_path: /metrics
  exporter:
    lock_wait_timeout: ""                  # 2
    log_slow_filter: ""                    # true | false
  timeout_offset: ""                       # 0.25
  raw_flags: {}
```

### data source credentials

Using UNIX domain sockets and authentication:


```yaml
mongodb_exporter_credentials:
  client:
    socket: "/run/mongodb/mongodb.sock"
    username: "prometheus"
    password: "nopassword"
```

or using a TCP connection and password authentication:

```yaml
mongodb_exporter_credentials:
  client:
    hostname: "hostname"
    port: "3306"
    socket: "dbname"
    username: "prometheus"
    password: "nopassword"
```

---

## Author

- Bodo Schulz

## License

This project is licensed under Apache License. See [LICENSE](/LICENSE) for more details.

**FREE SOFTWARE, HELL YEAH!**

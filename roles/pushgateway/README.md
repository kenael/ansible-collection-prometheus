
# Ansible Role:  `pushgateway`

Ansible role to setup [pushgateway](https://github.com/prometheus/pushgateway).


[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/bodsch/ansible-pushgateway/main.yml?branch=main)][ci]
[![GitHub issues](https://img.shields.io/github/issues/bodsch/ansible-pushgateway)][issues]
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/bodsch/ansible-pushgateway)][releases]
[![Ansible Quality Score](https://img.shields.io/ansible/quality/50067?label=role%20quality)][quality]

[ci]: https://github.com/bodsch/ansible-pushgateway/actions
[issues]: https://github.com/bodsch/ansible-pushgateway/issues?q=is%3Aopen+is%3Aissue
[releases]: https://github.com/bodsch/ansible-pushgateway/releases
[quality]: https://galaxy.ansible.com/bodsch/pushgateway

If `latest` is set for `pushgateway_version`, the role tries to install the latest release version.  
**Please use this with caution, as incompatibilities between releases may occur!**

The binaries are installed below `/usr/local/bin/pushgateway/${pushgateway_version}` and later linked to `/usr/bin`. 
This should make it possible to downgrade relatively safely.

The downloaded archive is stored on the Ansible controller, unpacked and then the binaries are copied to the target system.
The cache directory can be defined via the environment variable `CUSTOM_LOCAL_TMP_DIRECTORY`. 
By default it is `${HOME}/.cache/ansible/pushgateway`.
If this type of installation is not desired, the download can take place directly on the target system. 
However, this must be explicitly activated by setting `pushgateway_direct_download` to `true`.

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

### Operating systems

Tested on

* Arch Linux
* Debian based
    - Debian 10 / 11
    - Ubuntu 20.10
* RedHat based
    - Alma Linux 8
    - Rocky Linux 8
    - Oracle Linux 8

## usage

### default configuration

```yaml
pushgateway_version: "1.4.2"

pushgateway_release: {}

pushgateway_system_user: pushgateway
pushgateway_system_group: pushgateway

pushgateway_direct_download: false

pushgateway_service: {}
```

#### `pushgateway_service`

```yaml
pushgateway_service:
  log:
    level: info
    format: ""
  web:
    config:
      file: ""
    listen_address: "127.0.0.1:9091"
    telemetry_path: ""
    external_url: ""
    route_prefix: ""
    enable_lifecycle: false
    enable_admin_api: false
  persistence:
    file: ""
    interval: 5m
  push:
    disable_consistency_check: false
```

## Contribution

Please read [Contribution](CONTRIBUTING.md)

## Development,  Branches (Git Tags)

The `master` Branch is my *Working Horse* includes the "latest, hot shit" and can be complete broken!

If you want to use something stable, please use a [Tagged Version](https://github.com/bodsch/ansible-pushgateway/tags)!

---

## Author and License

- Bodo Schulz

## License

[Apache](LICENSE)

**FREE SOFTWARE, HELL YEAH!**

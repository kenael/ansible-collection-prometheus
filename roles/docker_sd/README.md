# Ansible Role:  `docker-sd`

Ansible role to install and configure [docker-sd](https://github.com/bodsch/docker-sd).

[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/bodsch/ansible-docker-sd/main.yml?branch=main)][ci]
[![GitHub issues](https://img.shields.io/github/issues/bodsch/ansible-docker-sd)][issues]
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/bodsch/ansible-docker-sd)][releases]
[![Ansible Quality Score](https://img.shields.io/ansible/quality/50067?label=role%20quality)][quality]

[ci]: https://github.com/bodsch/ansible-docker-sd/actions
[issues]: https://github.com/bodsch/ansible-docker-sd/issues?q=is%3Aopen+is%3Aissue
[releases]: https://github.com/bodsch/ansible-docker-sd/releases
[quality]: https://galaxy.ansible.com/bodsch/docker_sd


If `latest` is set for `docker_sd_version`, the role tries to install the latest release version.  
**Please use this with caution, as incompatibilities between releases may occur!**

The binaries are installed below `/opt/docker-sd/${docker-sd_version}` and later linked to `/usr/sbin`. 
This should make it possible to downgrade relatively safely.

The Source archive is stored on the Ansible controller, unpacked and then the binaries are copied to the target system.
The cache directory can be defined via the environment variable `CUSTOM_LOCAL_TMP_DIRECTORY`. 
By default it is `${HOME}/.cache/ansible/docker-sd`.
If this type of installation is not desired, the download can take place directly on the target system. 
However, this must be explicitly activated by setting `docker_sd_direct_download` to `true`.

## Dependencies

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

* Arch Linux
* Debian based
    - Debian 10 / 11
    - Ubuntu 20.10


## Contribution

Please read [Contribution](CONTRIBUTING.md)

## Development,  Branches (Git Tags)

The `master` Branch is my *Working Horse* includes the "latest, hot shit" and can be complete broken!

If you want to use something stable, please use a [Tagged Version](https://github.com/bodsch/ansible-docker-sd/tags)!


## Configuration

```yaml
docker_sd_version: "0.10.0"

docker_sd_system_user: docker-sd
docker_sd_system_group: docker-sd
docker_sd_config_dir: /etc/docker-sd

docker_sd_direct_download: false

docker_sd_release: {}

docker_sd_rest_api:
  port: 8088
  address: 127.0.0.1

docker_sd_hosts:
  - host: "unix:///run/docker.sock"
    metrics_ports:
      8199: "/metrics"
      8081: "/actuator/prometheus"

docker_sd_addition_labels: []
```

---

## Author and License

- Bodo Schulz

## License

[Apache](LICENSE)

**FREE SOFTWARE, HELL YEAH!**

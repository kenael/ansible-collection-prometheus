
# Ansible Role:  `ssl_exporter`

Ansible role to install and configure [SSL Exporter](https://github.com/ribbybibby/ssl_exporter).


If `latest` is set for `ssl_exporter_version`, the role tries to install the latest release version.  
**Please use this with caution, as incompatibilities between releases may occur!**

The binaries are installed below `/usr/local/opt/ssl_exporter/${ssl_exporter_version}` and later linked to `/usr/bin`. 
This should make it possible to downgrade relatively safely.

The ssl_exporter archive is stored on the Ansible controller, unpacked and then the binaries are copied to the target system.
The cache directory can be defined via the environment variable `CUSTOM_LOCAL_TMP_DIRECTORY`. 
By default it is `${HOME}/.cache/ansible/ssl_exporter`.
If this type of installation is not desired, the download can take place directly on the target system. 
However, this must be explicitly activated by setting `ssl_exporter_direct_download` to `true`.

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

* Arch Linux
* Debian based
    - Debian 10 / 11
    - Ubuntu 20.10


## Contribution

Please read [Contribution](CONTRIBUTING.md)

## Development,  Branches (Git Tags)

The `master` Branch is my *Working Horse* includes the "latest, hot shit" and can be complete broken!


## Configuration

```yaml
ssl_exporter_version: '2.4.2'
ssl_exporter_ssl_plus: false

ssl_exporter_system_group: ssl-exporter
ssl_exporter_system_user: "{{ ssl_exporter_system_group }}"
ssl_exporter_config_dir: /etc/ssl_exporter

ssl_exporter_direct_download: false

ssl_exporter_service: {}

ssl_exporter_release: {}

ssl_exporter_modules: {}

ssl_exporter_default_module: "https"
```

----

## Author and License

- Bodo Schulz

## License

[Apache](LICENSE)

**FREE SOFTWARE, HELL YEAH!**

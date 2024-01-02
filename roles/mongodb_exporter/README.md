
# Ansible Role:  `mongodb-exporter` 

Ansible role to install and configure [mongodb_exporter](https://github.com/prometheus/mongodb_exporter).


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
mongodb_exporter_version: "0.39.0"

mongodb_exporter_system_user: mongodb_exporter
mongodb_exporter_system_group: mongodb_exporter

mongodb_exporter_direct_download: false

mongodb_exporter_release: {}

mongodb_exporter_service: {}
```

### service configuration

```yaml
mongodb_exporter_service:
  log:
    level: info
    format: ""
  web:
    listen_address: "127.0.0.1:9216"
    telemetry_path: /metrics
    config: ""
  collector_all: ""                         # [true|false]
  collector:
    diagnosticdata: ""                      # [true|false]
    replicasetstatus: ""                    # [true|false]
    dbstats: ""                             # [true|false]
    topmetrics: ""                          # [true|false]
    indexstats: ""                          # [true|false]
    collstats: ""                           # [true|false]
    collstats_limit: ""                     # 0
  metrics:
    overridedescendingindex: ""             # [true|false]
  mongodb:
    collstats_colls: []                     #
    indexstats_colls: []                    #
    uri: "mongodb://user:pass@127.0.0.1:27017/admin?ssl=true"
    global_conn_pool: ""                    # [true|false]
    direct_connect: ""                      # [true|false]
  discovering_mode: ""                      # [true|false]
  compatible_mode: ""                       # [true|false]
  raw_flags: {}
```

---

## Author

- Bodo Schulz

## License

This project is licensed under Apache License. See [LICENSE](/LICENSE) for more details.

**FREE SOFTWARE, HELL YEAH!**

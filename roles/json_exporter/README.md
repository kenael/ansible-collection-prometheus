
# Ansible Role:  `json_exporter`

This ansible role installs and configure [json_exporter](https://github.com/prometheus-community/json_exporter)


If `latest` is set for `json_exporter_version`, the role tries to install the latest release version.  
**Please use this with caution, as incompatibilities between releases may occur!**

The binaries are installed below `/usr/local/opt/json_exporter/${json_exporter_version}` and later linked to `/usr/bin`. 
This should make it possible to downgrade relatively safely.

The json_exporter archive is stored on the Ansible controller, unpacked and then the binaries are copied to the target system.
The cache directory can be defined via the environment variable `CUSTOM_LOCAL_TMP_DIRECTORY`. 
By default it is `${HOME}/.cache/ansible/json_exporter`.
If this type of installation is not desired, the download can take place directly on the target system. 
However, this must be explicitly activated by setting `json_exporter_direct_download` to `true`.


## Requirements & Dependencies

Ansible Collections

- [bodsch.core](https://github.com/bodsch/ansible-collection-core)

```bash
ansible-galaxy collection install bodsch.core
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

## Usage

```
json_exporter_version: '0.5.0'

json_exporter_release: {}

json_exporter_system_group: json-exporter
json_exporter_system_user: json-exporter
json_exporter_config_dir: /etc/json_exporter

json_exporter_direct_download: false

json_exporter_service: {}

json_exporter_config: []
```

### `json_exporter_service`

#### defaults

```yaml
json_exporter_service:
  config:
    file: "{{ json_exporter_config_dir }}/config.yml"
  log:
    level: info
    format: ""
  web:
    listen_address: "0.0.0.0:7979"
```


### `json_exporter_config`

#### defaults

```yaml
json_exporter_config: []
```

#### example

```yaml
json_exporter_config:
  - name: example_global_value
    help: Example of a top-level global value scrape in the json
    path: "{ .counter }"
    labels:
      environment: beta                   # static label
      location: "planet-{.location}"      # dynamic label

  - name: mgob_backup
    help: MongoDB Backup
    type: object
    path: "{}"
    labels:
      environment: DEV                    # static label
      id: '{[].plan}'                     # dynamic label
    values:
      next_run: "{[].next_run}"
      last_run: "{[].last_run}"
      last_run_status: "{[].last_run_status}"
```


You can also look at the [molecule](molecule/default/group_vars/all) test.


## Contribution

Please read [Contribution](CONTRIBUTING.md)

## Development,  Branches (Git Tags)

The `master` Branch is my *Working Horse* includes the "latest, hot shit" and can be complete broken!

If you want to use something stable, please use a [Tagged Version](https://github.com/bodsch/ansible-json-exporter/tags)!

---

## Author and License

- Bodo Schulz

## License

[Apache](LICENSE)

**FREE SOFTWARE, HELL YEAH!**

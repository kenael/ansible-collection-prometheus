
# Ansible Role:  `node_exporter_textfile_collectors`

Ansible role to install [external collector scripts](https://github.com/prometheus-community/node-exporter-textfile-collector-scripts.git) 
for [node-exporter](https://github.com/prometheus/node_exporter).

## requirement

- `node_exporter` role

## usage

Look to the [defaults](defaults/main.yml) properties file to see the possible configuration properties.

You can also look at the [molecule](molecule/default/group_vars/all) test.

```yaml
node_exporter_system_user: node_exporter
node_exporter_system_group: node_exporter
node_exporter_config_dir: /etc/node_exporter
node_exporter_textfile_dir: /var/lib/node_exporter

node_exporter_collector_scripts: []

node_exporter_external_repository:
  enabled: true
  url: https://github.com/prometheus-community/node-exporter-textfile-collector-scripts.git
  version: master
```

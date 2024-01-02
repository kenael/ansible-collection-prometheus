# Ansible Collection - bodsch.prometheus

Documentation for the collection.

## Roles

| Role                                                                       | | Description |
|:---------------------------------------------------------------------------| :---- | :---- |
| [bodsch.prometheus.alertmanager](./roles/alertmanager/README.md)           |[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/bodsch/ansible-collection-prometheus/test_role_alertmanager.yml?branch=main)][workflow-alertmanager] |       |
| [bodsch.prometheus.am_silence](./roles/am_silence/README.md)               |[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/bodsch/ansible-collection-prometheus/test_role_am_silence.yml?branch=main)][workflow-am_silence]|       |
| [bodsch.prometheus.blackbox_exporter](./roles/blackbox_exporter/README.md) |[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/bodsch/ansible-collection-prometheus/test_role_blackbox_exporter.yml?branch=main)][workflow-blackbox_exporter]|       |
| [bodsch.prometheus.docker_sd](./roles/docker_sd/README.md)                 |[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/bodsch/ansible-collection-prometheus/test_role_docker_sd.yml?branch=main)][workflow-docker_sd]|       |
| [bodsch.prometheus.json_exporter](./roles/json_exporter/README.md)         |[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/bodsch/ansible-collection-prometheus/test_role_json_exporter.yml?branch=main)][workflow-json_exporter]|       |
| [bodsch.prometheus.mysql_exporter](./roles/mysql_exporter/README.md)       |[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/bodsch/ansible-collection-prometheus/test_role_mysql_exporter.yml?branch=main)][workflow-mysql_exporter]|       |
| [bodsch.prometheus.nginx_exporter](./roles/nginx_exporter/README.md)       |[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/bodsch/ansible-collection-prometheus/test_role_nginx_exporter.yml?branch=main)][workflow-nginx_exporter]|       |
| [bodsch.prometheus.node_exporter](./roles/node_exporter/README.md)         |[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/bodsch/ansible-collection-prometheus/test_role_node_exporter.yml?branch=main)][workflow-node_exporter]|       |
| [bodsch.prometheus.node_exporter_textfile_collectors](./roles/node_exporter/README.md) |[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/bodsch/ansible-collection-prometheus/test_role_node_exporter_collectors.yml?branch=main)][workflow-node_exporter_collectors]|       |
| [bodsch.prometheus.mongodb_exporter](./roles/mongodb_exporter/README.md)   |[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/bodsch/ansible-collection-prometheus/test_role_mongodb_exporter.yml?branch=main)][workflow-mongodb_exporter]|       |
| [bodsch.prometheus.promcheck](./roles/promcheck/README.md)                 |[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/bodsch/ansible-collection-prometheus/test_role_promcheck.yml?branch=main)][workflow-promcheck]|       |
| [bodsch.prometheus.prometheus](./roles/prometheus/README.md)               |[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/bodsch/ansible-collection-prometheus/test_role_prometheus.yml?branch=main)][workflow-prometheus]|       |
| [bodsch.prometheus.pushgateway](./roles/pushgateway/README.md)             |[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/bodsch/ansible-collection-prometheus/test_role_pushgateway.yml?branch=main)][workflow-pushgateway]|       |
| [bodsch.prometheus.trickster](./roles/trickster/README.md)                 |[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/bodsch/ansible-collection-prometheus/test_role_trickster.yml?branch=main)][workflow-trickster]|       |
| [bodsch.prometheus.redis_exporter](./roles/redis_exporter/README.md)       |[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/bodsch/ansible-collection-prometheus/test_role_redis_exporter.yml?branch=main)][workflow-redis_exporter]|       |
| [bodsch.prometheus.ssl_exporter](./roles/ssl_exporter/README.md)           |[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/bodsch/ansible-collection-prometheus/test_role_ssl_exporter.yml?branch=main)][workflow-ssl_exporter]|       |


[workflow-alertmanager]: https://github.com/bodsch/ansible-collection-prometheus/actions/workflows/test_role_alertmanager.yml
[workflow-am_silence]: https://github.com/bodsch/ansible-collection-prometheus/actions/workflows/test_role_am_silence.yml
[workflow-blackbox_exporter]: https://github.com/bodsch/ansible-collection-prometheus/actions/workflows/test_role_blackbox_exporter.yml
[workflow-docker_sd]: https://github.com/bodsch/ansible-collection-prometheus/actions/workflows/test_role_docker_sd.yml
[workflow-json_exporter]: https://github.com/bodsch/ansible-collection-prometheus/actions/workflows/test_role_json_exporter.yml
[workflow-mysql_exporter]: https://github.com/bodsch/ansible-collection-prometheus/actions/workflows/test_role_mysql_exporter.yml
[workflow-nginx_exporter]: https://github.com/bodsch/ansible-collection-prometheus/actions/workflows/test_role_nginx_exporter.yml
[workflow-node_exporter]: https://github.com/bodsch/ansible-collection-prometheus/actions/workflows/test_role_node_exporter.yml
[workflow-node_exporter_collectors]: https://github.com/bodsch/ansible-collection-prometheus/actions/workflows/test_role_node_exporter_collectors.yml
[workflow-mongodb_exporter]: https://github.com/bodsch/ansible-collection-prometheus/actions/workflows/test_role_mongodb_exporter.yml
[workflow-promcheck]: https://github.com/bodsch/ansible-collection-prometheus/actions/workflows/test_role_promcheck.yml
[workflow-prometheus]: https://github.com/bodsch/ansible-collection-prometheus/actions/workflows/test_role_prometheus.yml
[workflow-pushgateway]: https://github.com/bodsch/ansible-collection-prometheus/actions/workflows/test_role_pushgateway.yml
[workflow-trickster]: https://github.com/bodsch/ansible-collection-prometheus/actions/workflows/test_role_trickster.yml
[workflow-redis_exporter]: https://github.com/bodsch/ansible-collection-prometheus/actions/workflows/test_role_redis_exporter.yml
[workflow-ssl_exporter]: https://github.com/bodsch/ansible-collection-prometheus/actions/workflows/test_role_ssl_exporter.yml

## Modules

### `amtool`

| Name  | Description |
| :---- | :---- |
| `bodsch.prometheus.amtool` | |


### `promtool`

| Name  | Description |
| :---- | :---- |
| `bodsch.prometheus.promtool` | |

### `alertmanager_silence`

| Name  | Description |
| :---- | :---- |
| `bodsch.prometheus.alertmanager_silence` | |


### `alertmanager_templates`

| Name  | Description |
| :---- | :---- |
| `bodsch.prometheus.alertmanager_templates` | |


### `prometheus_alert_rule`

| Name  | Description |
| :---- | :---- |
| `bodsch.prometheus.prometheus_alert_rule` | |


### `prometheus_alert_rules`

| Name  | Description |
| :---- | :---- |
| `bodsch.prometheus.prometheus_alert_rules` | |

## Filters

### `mysql_exporter`

| Name  | Description |
| :---- | :---- |
| `bodsch.prometheus.valid_credentials` | |
| `bodsch.prometheus.has_credentials` | |

### `nginx_exporter`


| Name  | Description |
| :---- | :---- |
| `bodsch.prometheus.nginx_exporter_prometheus_labels` | |

### `parse_checksum`

| Name  | Description |
| :---- | :---- |
| `bodsch.prometheus.parse_checksum` | |

### `prometheus`

| Name  | Description |
| :---- | :---- |
| `bodsch.prometheus.validate_file_sd` | |
| `bodsch.prometheus.validate_alertmanager_endpoints` | |
| `bodsch.prometheus.remove_empty_elements` | |
| `bodsch.prometheus.jinja_encode` | |

### `silencer`

| Name  | Description |
| :---- | :---- |
| `bodsch.prometheus.expired` | |
| `bodsch.prometheus.current_datetime` | |

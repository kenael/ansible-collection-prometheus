
# Ansible Role:  `redis_exporter`

This ansible role installs and configure [redis_exporter](https://github.com/oliver006/redis_exporter)


If `latest` is set for `redis_exporter_version`, the role tries to install the latest release version.  
**Please use this with caution, as incompatibilities between releases may occur!**

The binaries are installed below `/usr/local/opt/redis_exporter/${redis_exporter_version}` and later linked to `/usr/bin`. 
This should make it possible to downgrade relatively safely.

The redis_exporter archive is stored on the Ansible controller, unpacked and then the binaries are copied to the target system.
The cache directory can be defined via the environment variable `CUSTOM_LOCAL_TMP_DIRECTORY`. 
By default it is `${HOME}/.cache/ansible/redis_exporter`.
If this type of installation is not desired, the download can take place directly on the target system. 
However, this must be explicitly activated by setting `redis_exporter_direct_download` to `true`.


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
redis_exporter_version: '1.56.0'

redis_exporter_release: {}

redis_exporter_system_group: redis-exporter
redis_exporter_system_user: redis-exporter
redis_exporter_config_dir: /etc/redis_exporter

redis_exporter_direct_download: false

redis_exporter_service: {}

...

```

### `redis_exporter_service`

#### defaults

```yaml
redis_exporter_service:
  redis:
    address: ""                                                   # Address of the Redis instance to scrape (default "redis://localhost:6379")
    password: ""                                                  # Password of the Redis instance to scrape
    password_file: ""                                             # Password file of the Redis instance to scrape
    user: ""                                                      # User name to use for authentication (Redis ACL for Redis 6.0 and newer)
    only_metrics: ""                                              #
  check:
    key_groups: []                                                # Comma separated list of lua regex for grouping keys
    keys: []                                                      # Comma separated list of key-patterns to export value and length/size, searched for with SCAN
    keys_batch_size: ""                                           # Approximate number of keys to process in each execution, larger value speeds up scanning.
                                                                  # WARNING: Still Redis is a single-threaded app, huge COUNT can affect production environment. (default 1000)
    single_keys: []                                               # Comma separated list of single keys to export value and length/size
    single_streams: []                                            # Comma separated list of single streams to export info about streams, groups and consumers
    streams: []                                                   # Comma separated list of stream-patterns to export info about streams, groups and consumers, searched for with SCAN
  config_command: ""                                              #
  connection_timeout: ""                                          #
  count_keys: []                                                  #
  debug: ""                                                       #
  disable_exporting_key_values: ""                                #
  export_client_list: ""                                          # Whether to scrape Client List specific metrics
  export_client_port: ""                                          # Whether to include the client's port when exporting the client list. Warning: including the port increases the number of metrics generated and will make your Prometheus server take up more memory
  include_config_metrics: ""                                      # Whether to include all config settings as metrics
  include_system_metrics: ""                                      # Whether to include system metrics like e.g. redis_total_system_memory_bytes
  is_cluster: ""                                                  # Whether this is a redis cluster (Enable this if you need to fetch key level data on a Redis Cluster).
  is_tile38: ""                                                   # Whether to scrape Tile38 specific metrics
  max_distinct_key_groups: ""                                     # The maximum number of distinct key groups with the most memory utilization to present as distinct metrics per database, the leftover key groups will be aggregated in the 'overflow' bucket (default 100)
  namespace: ""                                                   # Namespace for metrics (default "redis")
  ping_on_connect: ""                                             # Whether to ping the redis instance after connecting
  redact_config_metrics: ""                                       # Whether to redact config settings that include potentially sensitive information like passwords (default true)
  script: []                                                      # Comma separated list of path(s) to Redis Lua script(s) for gathering extra metrics
  set_client_name: ""                                             # [true | false]
  tls:                                                            #
    skip_tls_verification: ""                                     # Whether to to skip TLS verification
    ca_cert_file: ""                                              # Name of the CA certificate file (including full path) if the server requires TLS client authentication
    client:
      cert_file: ""                                               # Name of the client certificate file (including full path) if the server requires TLS client authentication
      key_file: ""                                                # Name of the client key file (including full path) if the server requires TLS client authentication
    server:
      ca_cert_file: ""                                            # Name of the CA certificate file (including full path) if the web interface and telemetry should require TLS client authentication
      cert_file: ""                                               # Name of the server certificate file (including full path) if the web interface and telemetry should use TLS
      key_file: ""                                                # Name of the server key file (including full path) if the web interface and telemetry should use TLS
      min_version: ""                                             # Minimum TLS version that is acceptable by the web interface and telemetry when using TLS (default "TLS1.2")
  log:
    level: info                                                   # NOT USED (but why!?)
    format: ""                                                    #
  web:                                                            #
    listen_address: "127.0.0.1:9121"                              #
    telemetry_path: "/metrics"                                    #
```

You can also look at the [molecule](molecule/default/group_vars/all) test.


## Contribution

Please read [Contribution](CONTRIBUTING.md)

## Development,  Branches (Git Tags)

The `master` Branch is my *Working Horse* includes the "latest, hot shit" and can be complete broken!

---

## Author and License

- Bodo Schulz

## License

[Apache](LICENSE)

**FREE SOFTWARE, HELL YEAH!**

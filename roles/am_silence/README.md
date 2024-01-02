
# Ansible Role:  `am_silence`

Ansible role to create an alertmanager silence.

## usage

```yaml
silence_downtime:
  minutes: 10

silence_alertmanager:
  url: "http://127.0.0.1:9093"

silence_comment: Silence for ansible-deployment

silence_matchers:
  - name: "environment"
    value: "dev"
    isRegex: false
```

## tests

```
ANSIBLE_RUN_TAGS=silence_add make test -e COLLECTION_ROLE=am_silence -e COLLECTION_SCENARIO=default

ANSIBLE_RUN_TAGS=silence_remove make test -e COLLECTION_ROLE=am_silence -e COLLECTION_SCENARIO=default
```

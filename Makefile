#
export TOX_SCENARIO         ?= default
export TOX_ANSIBLE          ?= ansible_6.7

export COLLECTION_NAMESPACE ?= bodsch
export COLLECTION_NAME      ?= prometheus
export COLLECTION_ROLE      ?= ""
export COLLECTION_SCENARIO  ?= default

.PHONY: install uninstall doc converge test destroy verify lint

default: install

install:
	@hooks/install

uninstall:
	@hooks/uninstall

doc:
	@hooks/doc

converge:
	@hooks/converge

test:
	@hooks/test

destroy:
	@hooks/destroy

verify:
	@hooks/verify

lint:
	@hooks/lint

#!/usr/bin/env bash

env_file="/etc/node_exporter/.env/solr_response.rc"

if [ -e "${env_file}" ]
then
  . "${env_file}"
  # solr_endpoints=(dvinci eventbrite)
  # solr_core="live"
  # solr_server="solr-master"
  # solr_url="https://admin.cmsqa.arri.com/admin/${solr_server}/${solr_core}/select?q=network%3Advinci&q=%3A&rows=0"

  for e in ${solr_endpoints[@]}
  do
    data=$(curl \
      --silent \
      "${solr_url}/select?q=network:${e}&rows=0")

    num_found=$(echo "${data}" | jq -r '.response.numFound')

    echo "solr_response{network=\"${e}\", solr_server=\"${solr_server}\", solr_core=\"${solr_core}\"} ${num_found}"

  done
  exit 0
fi

exit 1

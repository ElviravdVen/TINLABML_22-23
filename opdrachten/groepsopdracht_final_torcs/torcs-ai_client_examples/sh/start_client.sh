#!/usr/bin/env bash

echo "Clear previous log"

function startLogging {
    date +%F > logs/torcs_client.log; ../client >> logs/torcs_client.log
}

if [[ "$(dirname $0)" == "sh" ]]; then
    startLogging
else
    (cd ..; startLogging)
fi
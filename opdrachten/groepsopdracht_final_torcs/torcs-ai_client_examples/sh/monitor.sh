#!/usr/bin/env bash

function monitor {
    (cd ../logs; tail -f torcs_client.log)
}

cls

if [[ "$(dirname $0)" == "sh" ]]; then
    monitor
else
    (cd ..; monitor)
fi
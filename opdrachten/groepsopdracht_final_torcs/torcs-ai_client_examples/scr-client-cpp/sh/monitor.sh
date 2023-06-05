#!/usr/bin/env bash

function monitor {
    tail -f torcs_client.log

}

cls

if [[ "$(dirname $0)" == "sh" ]]; then
    (cd logs; monitor)
else
    (cd ../logs; monitor)
fi
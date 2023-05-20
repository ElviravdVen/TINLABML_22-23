#!/usr/bin/env bash

function drive {
    echo "Clear previous log"
    date > logs/torcs_client.log; ./client >> logs/torcs_client.log    

}

cls

if [[ "$(dirname $0)" == "sh" ]]; then
    drive
else
    (cd ..; drive)
fi
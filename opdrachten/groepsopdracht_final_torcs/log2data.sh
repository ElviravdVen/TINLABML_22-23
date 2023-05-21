#!/usr/bin/env bash

track="$1"

if [ -z "$track" ]; then
    echo "Error. $0 requires a trackname"
    exit 1;
fi

cat logs/torcs_client.log | grep ';' > "data/${track}_$(date +%F).csv"
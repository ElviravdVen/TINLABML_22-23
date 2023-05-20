#!/usr/bin/env bash

function makeClient {
    echo "Make Client"
    make clean && make
}

cls

if [[ "$(dirname $0)" == "sh" ]]; then
    makeClient
else
    (cd ..; makeClient)
fi
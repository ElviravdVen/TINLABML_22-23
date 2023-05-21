#!/usr/bin/env bash

function makeClient {
    echo "Make Client"
    (cd scr-client-cpp; make clean && make)
}

cls

if [[ "$(dirname $0)" == "sh" ]]; then
    makeClient
else
    (cd ..; makeClient)
fi
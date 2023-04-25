#!/usr/bin/env bash

# export WORKSPACE=$PWD

echo "Create VM"
vagrant up --provider=virtualbox --no-provision --parallel && vagrant status

echo "Provision VM"
vagrant provision
#!/usr/bin/env bash

# export WORKSPACE=$PWD

cowsay "Create VM"
vagrant up torcs-ubuntu --provider=virtualbox --no-provision --parallel && vagrant status

cowsay "Provision VM"
vagrant provision
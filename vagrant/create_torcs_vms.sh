#!/usr/bin/env bash

machines=("torcs-server" "torcs-client")

printf "Create VMs %s and %s" "${machines[0]}" "${machines[0]}"
vagrant up --provider=virtualbox --no-provision "${machines[0]}" \
    && vagrant status "${machines[0]}"
vagrant up --provider=virtualbox --no-provision "${machines[1]}" \
     && vagrant status "${machines[1]}"

printf "Provision VM" "${machines[0]}"
vagrant provision "${machines[0]}"

printf "Provision VM" "${machines[1]}"
vagrant provision ${machines[1]}
#!/usr/bin/env bash

machines=("torcs-server" "torcs-client")

for machine in "${machines[@]}"
do
    printf "Create VM %s" "${machines[i]}\n"
    vagrant up --provider=virtualbox --no-provision "${machines[i]}" \
        && vagrant status "${machines[i]}"

    printf "Provision VM" "${machines[i]}\n"
    vagrant provision "${machines[i]}"

done

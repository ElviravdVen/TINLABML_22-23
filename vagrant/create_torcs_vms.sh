#!/usr/bin/env bash

machines=("torcs-server" "torcs-client")

for machine in ${machines[@]}
do
    printf "Create VM %s\n" ${machines[i]}
    vagrant up --provider=virtualbox --no-provision ${machines[i]} \
        && vagrant status ${machines[i]}

    printf "Provision VM %s\n" ${machines[i]}
    vagrant provision ${machines[i]}

done
#!/usr/bin/env bash

machines=("torcs-server" "torcs-client")

for machine in "${machines[@]}"
do
    boxname="${machine}.box"
    printf "Export VM %s\n" "${boxname}"

    vagrant package ${boxname} --output ${boxname}
    md5sum ${boxname}

done
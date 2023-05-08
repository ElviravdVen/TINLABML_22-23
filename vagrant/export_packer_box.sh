#!/usr/bin/env bash

# VBoxManage list vms
# vagrant package --base a3f59eed-b9c5-4a5f-9977-187f8eb8c4d4 --output boxname.box

boxname="tinlab-torcs"
boxbase="$(VBoxManage list vms | grep packer | cut -d ' ' -f 2 | sed -e 's/{//' | sed -e 's/}//')"
printf "Export VM %s with base %s\n" ${boxname} ${boxbase}

vagrant package --base ${boxbase} ${boxname} --output ${boxname}
# md5sum ${boxname}
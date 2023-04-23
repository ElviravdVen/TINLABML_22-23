#!/usr/bin/env bash

boxname="torcs-server"

vagrant package ${boxname} --output ${boxname}
md5sum "${boxname}.box"
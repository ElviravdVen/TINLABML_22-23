#!/usr/bin/env bash

argVals=("$@")
nrOfArgs=${#argVals[@]}

if ((nrOfArgs < 1))
then
    printf "USAGE: %s imagename\n" "$0"
    exit 1
fi

imageName=$1
registry="jaboo"

printf "Tag %s as %s\n" "${imageName}" "${registry}/${imageName}"
docker tag "${imageName}" "${registry}/${imageName}"

printf "Push %s\n" "${registry}/${imageName}"
docker push "${registry}/${imageName}"

docker images | grep "${imageName}"
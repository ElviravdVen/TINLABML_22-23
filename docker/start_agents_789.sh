#!/usr/bin/env bash

docker-compose -f docker-compose-789.yml down

docker-compose -f docker-compose-789.yml up \
    --no-attach agent7 \
    --no-attach agent8 \
    --no-attach agent9    
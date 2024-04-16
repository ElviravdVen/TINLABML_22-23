#!/usr/bin/env bash

docker-compose -f docker-compose-456.yml down

docker-compose -f docker-compose-456.yml up \
    --no-attach agent4 \
    --no-attach agent5 \
    --no-attach agent6    
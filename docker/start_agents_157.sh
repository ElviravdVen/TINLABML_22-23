#!/usr/bin/env bash

docker-compose -f docker-compose-157.yml down

docker-compose -f docker-compose-157.yml up \
    --no-attach agent1 \
    --no-attach agent7 \
    --no-attach agent5
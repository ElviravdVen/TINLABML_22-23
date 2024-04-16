#!/usr/bin/env bash

docker-compose -f docker-compose-123.yml down

docker-compose -f docker-compose-123.yml up \
    --no-attach agent1 \
    --no-attach agent2 \    
    --no-attach agent3
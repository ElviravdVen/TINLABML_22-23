#!/usr/bin/env bash

(cd ..; docker build . -t jaboo/agent:22230 -f docker/Dockerfile)
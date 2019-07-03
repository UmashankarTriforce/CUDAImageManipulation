#!/usr/bin/env bash

xhost +local:`docker inspect --format='{{ .Config.Hostname }}' cvmms`
docker start cvmms
docker exec -ti cvmms bash
docker stop cvmms
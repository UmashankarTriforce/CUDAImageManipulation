#!/usr/bin/env bash

docker build --tag 'cuda/cvmms:latest' .

set -x

echo "Searching for Docker image ..."
DOCKER_IMAGE_ID=$(docker images --format="{{.ID}}" cuda/cvmms:latest | head -n 1)
echo "Found and using ${DOCKER_IMAGE_ID}"

USER_UID=$(id -u)

QT_GRAPHICSSYSTEM="native" docker run -t -i -d \
  --runtime nvidia \
  --volume=/run/user/${USER_UID}/pulse:/run/user/1000/pulse \
  --name cvmms \
  --env="DISPLAY" \
  -p 54022:22 \
  --env="QT_X11_NO_MITSHM=1" \
  --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
  ${DOCKER_IMAGE_ID} \
  ${@}

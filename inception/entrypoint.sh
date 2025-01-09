#!/bin/sh

dockerd &

while ! docker info > /dev/null 2>&1; do
    sleep 1
done

chmod 777 /run/docker.sock
chmod 777 /var/run/docker.sock

docker-compose -f /internal/docker-compose.yaml up -d --build --force-recreate --remove-orphans

tail -f /dev/null

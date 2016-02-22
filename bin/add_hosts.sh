#! /bin/sh

PROJECT_NAME=storm

HOSTS_STR="\n"

for v in $(seq 1 $1)
do
    CONTAINER_NAME="${PROJECT_NAME}_supervisor_${v}"
    id_str=`docker ps -f name=${CONTAINER_NAME} --format "{{.ID}}"`
    address=`docker inspect --format "{{.NetworkSettings.IPAddress}}" ${CONTAINER_NAME}`
    HOSTS_STR="${HOSTS_STR}${address} ${id_str} ${CONTAINER_NAME}\n"
done

for v in $(seq 1 $1)
do
    CONTAINER_NAME="${PROJECT_NAME}_supervisor_${v}"
    echo $HOSTS_STR | docker exec -i ${CONTAINER_NAME} bash -c "cat >> /etc/hosts"
done

#!/bin/bash

# Extract the SERVER_IP
SERVER_IP="replace-with-server-ip"

# Function to stop and remove containers
stop_and_remove_containers() {
    docker stop $(docker ps -qa)
    docker rm $(docker ps -qa)
}

# Check if --noktls flag is provided
if [ "$1" == "--noktls" ]; then
    docker_image="container-nginx-noktls"
else
    docker_image="container-nginx-ktls"
fi

stop_and_remove_containers

echo "Starting $1 containers"

# Specify the number of containers to start (e.g., 5)
num_containers="$1"

for ((i = 1; i <= num_containers; i++)); do
    echo "Container $i"
    port=$((8000 + i))
    sed -i "/upstream\.*/a \        server $SERVER_IP:$port;" /etc/nginx/nginx.conf

    docker run -d -e HOST_N="$port" -p "$port:8383" "$docker_image"
done


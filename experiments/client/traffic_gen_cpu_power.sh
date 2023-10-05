#!/bin/bash

# Define the mode as the first argument passed to the script
mode="$1"

# Get the current date and time for log file naming
current_datetime=$(date +%F-%H-%M-%S)
log_file="$current_datetime-$mode"

# Log the start timestamp
date | tee -a "$log_file-start.log"
/opt/notify.sh "Starting $mode"

# Define the SSH server hostname or IP address
ssh_server="user@server"

# Define the server URL
server_url="http://xpto/1G"

# Define the number of iterations
num_iterations=10

# Loop for the specified number of iterations
for iteration in $(seq 1 $num_iterations); do
  # Log the start timestamp for each iteration
  start_timestamp=$(date +%s)
  echo "$start_timestamp" | tee -a "$log_file-start.log"

  # Send a request to the server and log the download speed
  download_speed=$(curl -H "Cache-Control: no-cache, no-store, must-revalidate" \
                        -H "Pragma: no-cache" \
                        -H "Expires: 0" \
                        -k -s -o /dev/null -w '%{speed_download}\n' "$server_url")
  
  # Log the download speed
  echo "$download_speed" | tee -a "$log_file.log"

  # Log the end timestamp for each iteration
  end_timestamp=$(date +%s)
  echo "$end_timestamp" | tee -a "$log_file-end.log"
done

# Log the end timestamp
date | tee -a "$log_file-end.log"
<path to send_experiment_status.sh> "Ending $mode"

# Trigger a remote shutdown (using the SSH server variable)
ssh -n -f "$ssh_server" -t sudo shutdown -ar now

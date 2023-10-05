#!/bin/bash

# User-defined variables
export mode="wrk_$1"
num_rounds=3
duration="5m"
connection_counts="1 8 16"
target_url="http://serverurl/1M"  # Replace with your target URL
ssh_server="user@server"  # Replace with your SSH server hostname or IP
wrk_binary="/opt/wrk/wrk"  # Path to the wrk binary
lua_script="/opt/chelsio-experiments/experiments/client/nginx_metrics.lua"  # Path to the Lua script

# Function to run the experiment
function run_experiment() {
    timestamp=$(date +%F-%H-%M-%S)
    log_file="$timestamp-$mode-$connections"
    csv_file="$timestamp-$mode-$connections.csv"

    echo "requests,duration,bytes_in_mb,requests_per_second,transfer_per_second,latency_min,latency_max,latency_mean,latency_stdev" > "$csv_file"

    <path to send_experiment_status.sh>  "Starting $mode with $connections connections"
    date | tee -a "$log_file-start.log"

    for round in $(seq 1 $num_rounds); do
        date +%s | tee -a "$log_file-start.log"
        "$wrk_binary" -s "$lua_script" -H "Cache-Control: no-cache, no-store, must-revalidate" -H "Pragma: no-cache" -H "Expires: 0" -d "$duration" -c "$connections" -t "$connections" "$target_url" | tee -a "$log_file"
        date +%s | tee -a "$log_file-end.log"
    done

    date | tee -a "$log_file-end.log"
    <path to send_experiment_status.sh>  "Ending $mode with $connections connections"
}

# Main script
for connections in $connection_counts; do
    run_experiment
    # Delay to reduce noise
    sleep 120
done

# Shutdown the SSH server (replace with your command if needed)
ssh -n -f "$ssh_server" -t sudo shutdown -ar now

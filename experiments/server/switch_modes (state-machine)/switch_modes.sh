#!/bin/bash

# Set the SSH server name or IP address
ssh_server="user@server"  # Replace with your SSH server

# Function to prepare the specified mode, including loading modules and configuring NGINX
prepare_mode() {
    case "$1" in
        "noktls")
            modprobe cxgb4
            rmmod tls

            sed -i 's/options\ =.*/options\ =/g' <path_to_openssl.cnf> # Update with the actual openssl.cnf file

            next_mode="swktls"
            config_file="/path/to/nooff.conf"  # Update with the actual config file path
            ;;
        "swktls")
            modprobe cxgb4
            modprobe tls
            
            sed -i 's/options\ =.*/options\ =\ ktls/g' <path_to_openssl.cnf> # Update with the actual openssl.cnf file

            next_mode="coprocessor"
            config_file="/path/to/swktls.conf"  # Update with the actual config file path
            ;;
        "coprocessor")
            modprobe cxgb4
            modprobe tls
            modprobe chcr
            
            sed -i 's/options\ =.*/options\ =\ ktls/g' <path_to_openssl.cnf> # Update with the actual openssl.cnf file

            next_mode="inline"
            config_file="/path/to/coprocessor.conf"  # Update with the actual config file path
            ;;
        "inline")
            rmmod csiostor cxgb4i cxgbit iw_cxgb4 chcr cxgb4vf cxgb4 libcxgbi libcxgb t4_tom
            modprobe t4_tom

            sed -i 's/options\ =.*/options\ =\ ktls/g' <path_to_openssl.cnf> # Update with the actual openssl.cnf file

            next_mode=""
            config_file="/path/to/inline.conf"  # Update with the actual config file path
            ;;
        *)
            echo "Invalid mode specified. Usage: $0 <mode>"
            exit 1
            ;;
    esac
}

# Main script starts here
if [ $# -ne 1 ]; then
    echo "Usage: $0 <mode>"
    exit 1
fi

mode="$1"
next_mode=""

prepare_mode "$mode"

#  Start NGINX with CPU afinity set to core 7 - adapt for your system or simply remove taskset
taskset -c 7 /usr/local/nginx/sbin/nginx -c "$config_file"

# Notification
if [ -n "$next_mode" ]; then
    /bin/bash /opt/chelsio-experiments/experiments/send_experiment_status/send_experiment_status.sh "$next_mode mode is on"
fi

# Disable other modes if needed
/bin/bash /opt/chelsio-experiments/disable.sh

# SSH and screen commands for running experiments
if [ -n "$next_mode" ]; then
    ssh -f -n -t "$ssh_server" "/usr/bin/screen -S wrk_$mode -dm /opt/chelsio-experiments/experiments/client/traffic_gen_throughput_latency.sh $mode"
fi

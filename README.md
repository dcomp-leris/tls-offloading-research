# Chelsio Experiments

## Introduction

This repository houses all the scripts, data, and resources related to our research paper focused on evaluating the performance and energy efficiency implications of using kTLS (Kernel TLS) in different operational modes for the Chelsio T6 (T62100-LP-CR). Our study encompasses both bare metal and containerized environments, aiming to understand how cryptographic offloading impacts system metrics, including CPU usage, latency, throughput, and power consumption.

## Using the code

Each code used has its own README file to explain to you how to use the code and what dependencies you need to install in order to reproduce the experiments.

## Repository Structure

The repository is organized as follows:

```bash

chelsio-experiments
├── experiments                  # Scripts and files for experimental setups.
│   ├── send_experiment_status  # Scripts for sending experiment status to Telegram and Discord.
│   │   ├── README.md          # Documentation explaining how to use these scripts.
│   │   └── send_experiment_status.sh  # Shell script for sending experiment status.
│   ├── server                 # Scripts for starting containers and managing server-side experiments.
│   │   ├── start_containers   # Scripts and resources for starting and orchestrating multiple containers.
│   │   │   ├── README.md      # Documentation explaining container initialization.
│   │   │   └── start_containers.sh  # Shell script for starting multiple containers.
│   │   ├── systemd_services  # SystemD service configuration.
│   │   │   └── chelsio-inline.service.example  # Example SystemD service file.
│   │   └── switch_modes (state-machine)  # Scripts for managing offloading mode, creating a state-machine.
│   │       ├── README.md      # Documentation for managing offloading modes.
│   │       ├── switch_modes.sh  # Shell script for switching modes.
│   │       └── disable.sh.example  # Example script for disabling SystemD services.
│   └── client                 # Scripts and documentation for client-side experiments.
│       ├── nginx_metrics.md  # Documentation for NGINX metrics wrk lua script.
│       ├── traffic_gen_throughput_latency.md  # Documentation for traffic generation to get throughput and latency.
│       ├── traffic_gen_throughput_latency.sh  # Shell script for traffic generation to get throughput and latency.
│       ├── nginx_metrics.lua  # Lua script for exporting NGINX metrics using the wrk tool.
│       ├── traffic_gen_cpu_power.sh  # Shell script for traffic generation for collecting CPU and power metrics.
│       └── traffic_gen_cpu_power.md  # Documentation of the shell script for traffic generation for collecting CPU and power metrics.
├── datasets                     # Datasets generated during experiments.
├── data_processing              # Data processing scripts.
│   ├── power                    # Power consumption analysis scripts.
│   │   ├── README.md            # Documentation for power consumption analysis.
│   │   └── power_analysis.py    # Python script for power analysis.
│   ├── cpu                      # CPU performance analysis scripts.
│   │   ├── cpu_analysis.py      # Python script for CPU performance analysis.
│   │   └── README.md            # Documentation for CPU performance analysis.
│   ├── throughput_latency       # Scripts for analyzing throughput and latency data.
│   │   ├── README.md            # Documentation for throughput and latency analysis.
│   │   └── throughput_latency.py  # Python script for throughput and latency analysis.
│   └── utils                    # Utility scripts for data processing.
│       ├── barplot.md           # Markdown documentation for creating barplots.
│       ├── prometheus_power_data_fetcher.md  # Markdown documentation for fetching data from Prometheus.
│       ├── prometheus_power_data_fetcher.py  # Python script for fetching data from Prometheus.
│       └──  experiments.json.example  # Example JSON file for experiments.
├── docker_container            # Docker container and related files for NGINX with kTLS enabled.
│   ├── nginx_noktls.conf       # NGINX configuration file without kTLS.
│   ├── Dockerfile              # Dockerfile for building the NGINX container.
│   ├── nginx_ktls.conf         # NGINX configuration file with kTLS enabled.
│   ├── README.md               # Documentation for using the Docker container.
│   ├── nginx-1.21.4.tar.gz     # NGINX source code archive.
│   └── entrypoint.sh           # Entry point script for the Docker container.
└── README.md                    # Root repository README.

```

## Additional Context

Our research involves conducting experiments using cURL and wrk for traffic generation, and for collecting data wrk (throughput and latency), Prometheus Scaphandre (power), and CollectD (CPU time). We've automated the experimental process using SystemD to seamlessly transition between different offloading modes. We have a particular interest in analyzing power consumption, CPU time, throughput, and latency. Our goal is to contribute insights into the trade-offs between performance optimization and energy efficiency in data center environments.

If you have any questions or need further information, please refer to the relevant directories and documentation in this repository.

## License

All the assets in this repo is released under the [BSD-3 License](https://opensource.org/license/bsd-3-clause/). You are free to use, modify, and distribute this software, provided that you include the original copyright notice and disclaimers. The BSD-3 License is a permissive open-source license that encourages collaboration and innovation. It grants you the freedom to adapt this software to your needs while respecting the original author's contributions. Feel free to contribute to the project or build upon it for your own projects. Please review the LICENSE file on the root of this repo for the full terms and conditions of this license.



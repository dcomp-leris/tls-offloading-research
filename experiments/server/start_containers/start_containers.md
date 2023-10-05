# Start Containers

This script allows you to start multiple Docker containers. During the experiments a round-robin NGINX server using load balancing configurations was put in front of these containers, rotating connections for each container evenly.

## Prerequisites

- Docker installed on your system.
- NGINX kTLS images build as per docker_container directory guide you.

## Usage

You can use the script as follows:

```bash
./start-containers.sh <num_containers> [--noktls]
```

- `<num_containers>`: The number of containers to start.
- `--noktls` (Optional): Use this flag if you want to start containers without kTLS configuration. If not provided, containers with kTLS configuration will be started.

## Example

Start 5 containers with kTLS configuration:

```bash
./start-containers.sh 5
```

Start 3 containers without kTLS configuration:

```bash
./start-containers.sh 3 --noktls
```

## Notes

- The script will update the NGINX load balancer configuration to include the appropriate server entries for each container.
- The containers are started in detached mode (`-d`) and expose port 8383.
- The script also includes a function to stop and remove all Docker containers, making it easy to clean up after testing.

## License

This software is released under the [BSD-3 License](https://opensource.org/license/bsd-3-clause/). You are free to use, modify, and distribute this software, provided that you include the original copyright notice and disclaimers. The BSD-3 License is a permissive open-source license that encourages collaboration and innovation. It grants you the freedom to adapt this software to your needs while respecting the original author's contributions. Feel free to contribute to the project or build upon it for your own projects. Please review the LICENSE file on the root of this repo for the full terms and conditions of this license.

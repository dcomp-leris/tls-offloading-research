
# Traffic Generation Script

This script is designed to generate network traffic to a target server using the `wrk` tool. It performs multiple rounds of HTTP requests with different connection counts.

## Prerequisites

Before running the script, ensure you have the following prerequisites:

- The `wrk` tool installed on your system.
- A Lua script (provided as `nginx_metrics.lua` in this repo) for `wrk` customization.
- A target URL (`target_url` variable) where you want to generate traffic.
- SSH access to a server for remote operations (optional). To do it passwordless, you must use private key-based SSH access.
- Notification Script: The script uses `send_experiment_status.sh` for sending notifications. Make sure this script is available and configured.


## Usage

1. Run the script:

   ```bash
   ./traffic_generation.sh <mode>
   ```

   Replace `<mode>` with a suitable offloading mode (noktls, swktls, coprocessor, inline) for your traffic generation.

2. The script will perform multiple rounds of HTTP requests with different connection counts as specified in the `range` variable.

## Example

Here's an example of how to run the script:

```bash
./traffic_generation.sh inline
```

## Configuration

At the top of the script, you have to configure the variables.

## Shutdown

The script includes a command to shut down an SSH server (specified in the `ssh_server` variable) at the end. If you don't need this functionality, you can remove or modify that part of the script.

## Notifications

The script sends notifications at the start and end of traffic generation using send_experiment_status.sh. Ensure this notification script is configured for your system.

## Note

For more information on using the `wrk` benchmarking tool, refer to the [official documentation](https://github.com/wg/wrk).

## License

This software is released under the [BSD-3 License](https://opensource.org/license/bsd-3-clause/). You are free to use, modify, and distribute this software, provided that you include the original copyright notice and disclaimers. The BSD-3 License is a permissive open-source license that encourages collaboration and innovation. It grants you the freedom to adapt this software to your needs while respecting the original author's contributions. Feel free to contribute to the project or build upon it for your own projects. Please review the LICENSE file on the root of this repo for the full terms and conditions of this license.

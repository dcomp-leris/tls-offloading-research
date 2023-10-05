# Traffic Generation Script

This script is designed to generate network traffic to a specified server URL for a defined number of iterations. It creates traffic and saves download speed and logs the results along with timestamps. The purpose is generating sufficient data so CollectD can gather metrics while these test is running.

## Prerequisites

Before using this script, make sure you have the following prerequisites:

- cURL: cCURL is used for sending HTTP requests. Install it if it's not already available on your system.
- SSH Access: You should have SSH access to a remote server for the remote shutdown functionality. Ensure SSH is properly configured, you need do it passwordless, you must use private key-based SSH access.
- Notification Script: The script uses `send_experiment_status.sh` for sending notifications. Make sure this script is available and configured.

## Usage

You can run the script with the following command:

```bash
./traffic_generator.sh [mode]
```

[mode]: The offloading mode of operation for the traffic generation. You can specify any mode as an argument, e.g., "noktls", "swktls", "inline", "coprocessor".

## Configuration

At the top of the script, you can configure the following variables:

    ssh_server: The hostname or IP address of the SSH server for remote shutdown.

    server_url: The URL of the server you want to generate traffic to.

    iterations: The number of iterations to run for traffic generation.

## Output

The script will generate log files for each run with timestamps. The log files include:

    start.log: Start timestamps for each iteration.

    end.log: End timestamps for each iteration.

    [mode].log: Log of download speeds for each iteration.


## Shutdown

The script includes a command to shut down an SSH server (specified in the `ssh_server` variable) at the end. If you don't need this functionality, you can remove or modify that part of the script.

## Notifications

The script sends notifications at the start and end of traffic generation using send_experiment_status.sh. Ensure this notification script is configured for your system.

## License

This software is released under the [BSD-3 License](https://opensource.org/license/bsd-3-clause/). You are free to use, modify, and distribute this software, provided that you include the original copyright notice and disclaimers. The BSD-3 License is a permissive open-source license that encourages collaboration and innovation. It grants you the freedom to adapt this software to your needs while respecting the original author's contributions. Feel free to contribute to the project or build upon it for your own projects. Please review the LICENSE file on the root of this repo for the full terms and conditions of this license.



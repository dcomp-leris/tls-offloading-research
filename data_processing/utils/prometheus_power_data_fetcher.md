# Prometheus Power Consumption Data Fetching Script

This script is designed to collect power consumption data from Prometheus for different experiments and save it as CSV files. It utilizes the Prometheus API to fetch power consumption metrics for specified experiment configurations.

## Prerequisites

Before using this script, ensure you have the following prerequisites:

- Python (3.6 or higher)
- Required Python libraries (`requests`, `pandas`)

You can install the required Python libraries using pip:

```bash
pip install requests pandas
```

## Usage

1. Create a JSON configuration file (`experiments.json`) that defines the experiment configurations. The JSON file should have the following structure:

```json
{
  "container_number1": {
    "mode1": {
      "connection_number1": { "start": "start_time1", "end": "end_time1" },
      "connection_number2": { "start": "start_time2", "end": "end_time2" }
    },
    "mode2": {
      "connection_number1": { "start": "start_time3", "end": "end_time3" }
    }
  },
  "container_number2": {
    ...
  }
}
```

Replace `"container_number1"`, `"mode1"`, `"connection_number1"`, `"start_time1"`, `"end_time1"`, etc., with your specific experiment names, modes, connections, and time ranges.

2. Run the script with the following command:

```bash
python script.py --config-file experiments.json --output-dir output_directory
```

Replace `experiments.json` with the path to your JSON configuration file and `output_directory` with the directory where you want to save the CSV files.

3. The script will fetch power consumption data for each experiment configuration and save it as CSV files in the specified output directory.

## Configuration

- `prometheus_host` and `prometheus_path`: Configure the Prometheus server's host and API path as needed in the script.
- `step`: Set the time step (in seconds) for querying Prometheus data.

## Output

The script will generate CSV files with the following naming convention:

    b-m-{ct}-{mode}-{conn}.csv

Where {ct} represents the container number, {mode} represents the offloading mode used, and {conn} represents the connection number.

## License

This software is released under the [BSD-3 License](https://opensource.org/license/bsd-3-clause/). You are free to use, modify, and distribute this software, provided that you include the original copyright notice and disclaimers. The BSD-3 License is a permissive open-source license that encourages collaboration and innovation. It grants you the freedom to adapt this software to your needs while respecting the original author's contributions. Feel free to contribute to the project or build upon it for your own projects. Please review the LICENSE file on the root of this repo for the full terms and conditions of this license.
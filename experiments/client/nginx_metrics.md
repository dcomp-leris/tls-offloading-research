
# nginx_metrics.lua

`nginx_metrics.lua` is a Lua script used with the wrk HTTP benchmarking tool to collect and format benchmarking results into a CSV file. This script calculates key performance metrics and appends them to a CSV file for analysis.

## Usage

1. Place `nginx_metrics.lua` in the same directory as your `wrk` benchmarking tool.

2. To run the benchmark with `nginx_metrics.lua`, use the following command:

   ```bash
   wrk -t <threads> -c <connections> -d <duration> -s nginx_metrics.lua <URL>
   ```

   Replace `<threads>`, `<connections>`, `<duration>`, and `<URL>` with your desired benchmarking parameters.

3. The script will create a CSV file with the results in the same directory as `nginx_metrics.lua`. The CSV file will contain the following columns:

   - `requests`: Total number of requests sent during the benchmark.
   - `duration`: Duration of the benchmark in seconds.
   - `bytes_in_mb`: Total number of bytes transferred during the benchmark, converted to megabytes.
   - `requests_per_second`: Average requests per second (RPS) during the benchmark.
   - `transfer_per_second`: Average transfer rate in megabytes per second (MB/s) during the benchmark.
   - `latency_min`: Minimum latency observed during the benchmark in microseconds (µs).
   - `latency_max`: Maximum latency observed during the benchmark in microseconds (µs).
   - `latency_mean`: Mean latency observed during the benchmark in microseconds (µs).
   - `latency_stdev`: Standard deviation of latency observed during the benchmark in microseconds (µs).

## Customization

You can customize the script as needed for your benchmarking requirements. For example, you can change the formatting of numerical values or add additional metrics.

## Note

For more information on using the `wrk` benchmarking tool, refer to the [official documentation](https://github.com/wg/wrk).

## License

This software is released under the [BSD-3 License](https://opensource.org/license/bsd-3-clause/). You are free to use, modify, and distribute this software, provided that you include the original copyright notice and disclaimers. The BSD-3 License is a permissive open-source license that encourages collaboration and innovation. It grants you the freedom to adapt this software to your needs while respecting the original author's contributions. Feel free to contribute to the project or build upon it for your own projects. Please review the LICENSE file on the root of this repo for the full terms and conditions of this license.

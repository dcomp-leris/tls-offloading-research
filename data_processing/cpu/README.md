# CPU Analysis Script

This script is designed to analyze CPU data from both bare metal and containerized environments. It calculates mean CPU times and generates bar plots for analysis.

## Configuration

Before running the script, you need to configure the data file paths. Replace the placeholders below with the actual file paths on your system:

### Bare Metal Data Paths

```python
baremetal_data_path = '/opt/chelsio-experiments/datasets/baremetal/cpu'
baremetal_output_path = '/opt/chelsio-experiments/datasets/baremetal/plots'
```

### Containerized Data Paths

```python
containerized_data_path = '/opt/chelsio-experiments/datasets/containerized/cpu'
containerized_output_path = '/opt/chelsio-experiments/datasets/containerized/plots'
```

Make sure to replace the paths within single quotes with the actual paths on your system.

## Usage

1. Configure the file paths as mentioned above.
2. Run the script in your preferred Python environment.

The script will process the data and generate PDF plots in the specified output directories.

## Dependencies

This script relies on the following Python libraries:

- matplotlib
- pandas
- numpy

You can install these libraries using pip:

```
pip install matplotlib pandas numpy
```

## Note

Please ensure that the required data files exist in the specified input directories before running the script.

## License

This software is released under the [BSD-3 License](https://opensource.org/license/bsd-3-clause/). You are free to use, modify, and distribute this software, provided that you include the original copyright notice and disclaimers. The BSD-3 License is a permissive open-source license that encourages collaboration and innovation. It grants you the freedom to adapt this software to your needs while respecting the original author's contributions. Feel free to contribute to the project or build upon it for your own projects. Please review the LICENSE file on the root of this repo for the full terms and conditions of this license.
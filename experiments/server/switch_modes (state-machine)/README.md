# switch_modes.sh

The switch_modes.sh script simplifies the process of switching between different offloading configurations on a Linux system. It is primarily designed to manage the kernel modules and service configurations required for different offloading modes, including:

- No kTLS (noktls): Disabling kernel TLS offloading.
- Software kTLS (swktls): Enabling software-based kernel TLS offloading.
- Hardware kTLS (inline and coprocessor): Enabling hardware-based kernel TLS offloading modes.

## Overview

This script automates the process of switching between different offloading configurations by:

- Loading and unloading kernel modules specific to each offloading mode.
- Enabling and disabling systemd services based on the selected mode.
- Providing a convenient way to perform mode-specific tasks, if needed.
- You can define different offloading modes and their corresponding configurations in separate configuration files, making it easy to switch between modes with minimal manual intervention.

## Usage

```bash
./switch_modes.sh [mode]


[mode]: The offloading mode you want to switch to. This should correspond to a configuration file located in the config/ directory.
```

## Examples

Assuming you have defined configurations for different offloading modes (e.g., noktls, swktls, inline, coprocessor) in the config/directory, you can enable a mode as follows:

```
./switch_modes.sh noktls
```

## License

This software is released under the [BSD-3 License](https://opensource.org/license/bsd-3-clause/). You are free to use, modify, and distribute this software, provided that you include the original copyright notice and disclaimers. The BSD-3 License is a permissive open-source license that encourages collaboration and innovation. It grants you the freedom to adapt this software to your needs while respecting the original author's contributions. Feel free to contribute to the project or build upon it for your own projects. Please review the LICENSE file on the root of this repo for the full terms and conditions of this license.

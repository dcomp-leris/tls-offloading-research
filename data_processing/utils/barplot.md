# barplot.py

`barplot.py` is a Python script for creating bar plots with customizable colors and styles. This script is intended for use in data visualization projects and provides a simple way to generate horizontal bar plots.

## Features

- Create horizontal bar plots.
- Customize bar colors, widths, and labels.
- Supports grouping bars with multiple datasets.
- Easy-to-use interface for creating visually appealing bar plots.

## Usage

1. Import `barplot.py` into your Python script:

   ```python
   from barplot import bar_plot
   ```

2. Prepare your data in a format that suits your plotting needs.

3. Create a bar plot using the `bar_plot` function:

   ```python
   import matplotlib.pyplot as plt

   # Sample data
   data = {
       "Category 1": [10, 20, 15],
       "Category 2": [25, 15, 30],
       "Category 3": [20, 10, 25],
   }

   # Create a horizontal bar plot
   fig, ax = plt.subplots()
   bar_plot(ax, data, total_width=0.8, single_width=0.9, colors=["#FF5733", "#33FF57", "#5733FF"])
   
   # Customize labels, titles, and other plot settings as needed
   ax.set_xlabel("X-axis Label")
   ax.set_ylabel("Y-axis Label")
   ax.set_title("Bar Plot Example")
   plt.legend(loc="upper right")

   # Show or save the plot
   plt.show()
   ```

## Function Parameters

- `ax`: Matplotlib Axes object to which the plot will be drawn.
- `data`: Dictionary containing the data for the bar plot.
- `total_width`: Total width of the bars for a single group (default: 0.8).
- `single_width`: Width of each individual bar within a group (default: 0.9).
- `colors`: List of colors for the bars (default is IBM color blind safe palette: ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]).

## License

This software is released under the [BSD-3 License](https://opensource.org/license/bsd-3-clause/). You are free to use, modify, and distribute this software, provided that you include the original copyright notice and disclaimers. The BSD-3 License is a permissive open-source license that encourages collaboration and innovation. It grants you the freedom to adapt this software to your needs while respecting the original author's contributions. Feel free to contribute to the project or build upon it for your own projects. Please review the LICENSE file on the root of this repo for the full terms and conditions of this license.


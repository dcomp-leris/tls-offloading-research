import matplotlib.pyplot as plt

def bar_plot(ax, data, colors=None, total_width=0.8, single_width=1, legend=True, label=True, fmt='%.2e'):
    """
    Generate a bar plot with customizable options.

    Parameters:
    - ax (matplotlib.axes.Axes): The axis to plot on.
    - data (dict): A dictionary where keys are group labels and values are lists of bar heights.
    - colors (list, optional): List of colors for bars. Default is None, which uses the default color cycle.
    - total_width (float, optional): Total width of each group of bars. Default is 0.8.
    - single_width (float, optional): Width of an individual bar within a group. Default is 1.
    - legend (bool, optional): Whether to show a legend. Default is True.
    - label (bool, optional): Whether to label the bars with values. Default is True.
    - fmt (str, optional): Format string for labeling bars. Default is '%.2e'.

    Returns:
    - None

    Example:
    data = {
        'Group A': [10, 15, 12],
        'Group B': [8, 14, 10]
    }
    fig, ax = plt.subplots()
    bar_plot(ax, data, colors=['#ff5733', '#3366ff'], total_width=0.9, single_width=0.4)
    plt.show()
    """
    ax.yaxis.grid(color='gray', linestyle='dashed')
    ax.set_axisbelow(True)

    if colors is None:
        # IBM's accessibility palette for visually impaired people
        colors = ["#ffb000", "#fe6100", "#dc267f", "#785ef0", "#648fff"]

    n_bars = len(data)
    bar_width = total_width / n_bars
    bars = []

    for i, (name, values) in enumerate(data.items()):
        x_offset = (i - n_bars / 2) * bar_width + bar_width / 2

        for x, y in enumerate(values):
            bar = ax.bar(x + x_offset, y, width=bar_width * single_width, color=colors[i % len(colors)], edgecolor='gray')
            if label:
                ax.bar_label(bar, label_type='center', fmt=fmt, color="White", fontweight="bold")

        bars.append(bar[0])

    if legend:
        ax.legend(bars, data.keys())

from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import sys
import os
sys.path.insert(1, '/opt/chelsio-experiments/data_processing/utils/')
from barplot import bar_plot

# Define the data directory path
baremetal_data_path = '/opt/chelsio-experiments/datasets/baremetal/power'
containerized_data_path = '/opt/chelsio-experiments/datasets/containerized/power'

baremetal_output_path = '/opt/chelsio-experiments/datasets/baremetal/plots'
containerized_output_path = '/opt/chelsio-experiments/datasets/containerized/plots'

# Function to process raw CSV from Scaphandre
def process(filename):
    df = pd.read_csv(filename, dtype={'Data': int})
    return df['Data'].sum() / 1e+6 # Microwatts to Watts


if __name__ == "__main__":
    

    # Bare Metal Power analysis
    swktls_bm = process(os.path.join(baremetal_data_path, 'swktls.csv'))
    noktls_bm = process(os.path.join(baremetal_data_path, 'noktls.csv'))
    coprocessor_bm = process(os.path.join(baremetal_data_path, 'coprocessor.csv'))
    inline_bm = process(os.path.join(baremetal_data_path, 'inline.csv'))
    print(swktls_bm)
    data_bm = {
        "No Offloading": [noktls_bm],
        "SW kTLS": [swktls_bm],
        "Coprocessor": [coprocessor_bm],
        "Inline": [inline_bm],
    }

    # Containerized Power analysis
    container_counts = ['5', '25', '50', '100']
    noktls_ct_data = {}
    swktls_ct_data = {}
    coprocessor_ct_data = {}

    for count in container_counts:
        noktls_ct_data[count] = process(os.path.join(containerized_data_path, f'noktls-{count}.csv'))
        swktls_ct_data[count] = process(os.path.join(containerized_data_path, f'swktls-{count}.csv'))
        coprocessor_ct_data[count] = process(os.path.join(containerized_data_path, f'coprocessor-{count}.csv'))

    data_ct = {
        "No Offloading": [noktls_ct_data.get(k) for k in container_counts],
        "SW kTLS": [swktls_ct_data.get(k) for k in container_counts],
        "Coprocessor Mode": [coprocessor_ct_data.get(k) for k in container_counts],
    }

    # Plotting and saving PDFs

    # Bare Metal
    X = []
    X_axis = []

    fig_bm, ax_bm = plt.subplots(figsize=(6, 4))
    ax_bm.set_xticks(X_axis, X)
    ax_bm.set_ylabel("Power Consumption (W)")
    bar_plot(ax_bm, data_bm, total_width=.8, single_width=.8, label=False)
    plt.savefig(os.path.join(baremetal_output_path, "bm_power_analysis.pdf"), format="pdf", bbox_inches="tight")

    # Containerized
    X = container_counts
    X_axis = np.arange(len(X))
    
    fig_ct, ax_ct = plt.subplots(figsize=(12,4))
    ax_ct.set_xticks(X_axis, X)
    ax_ct.set_xlabel("Containers")
    ax_ct.set_ylim(0,700)
    ax_ct.set_ylabel("Power Consumption (W)")
    bar_plot(ax_ct, data_ct, total_width=.8, single_width=.8, label=False)
    plt.savefig(os.path.join(containerized_output_path, "ct_power_analysis.pdf"), format="pdf", bbox_inches="tight")

    # Show the plots if needed
    plt.show()

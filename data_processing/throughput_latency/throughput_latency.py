from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import sys
import os
sys.path.insert(1, '/opt/chelsio-experiments/dev/experiments/utils/')
from barplot import bar_plot

def latency_mean(data):
    return data['latency_mean'].mean() / 1000  # Divides by 1000 to get ms from us

def throughput_mean(data):
    return data['transfer_per_second'].mean()

cts = ['1', '8', '16', '32']
conn_bm = ['1', '8', '16']
conn_ct = ['1', '8', '16', '32']
modes_bm = ['noktls', 'swktls', 'coprocessor', 'inline']
modes_ct = ['noktls', 'swktls', 'coprocessor']
exps_bm = {}
exps_ct = {}

# Initialize the exps dictionary for bare metal
exps_bm = {mode: {c: {} for c in conn_bm} for mode in modes_bm}
exps_ct = {ct: {mode: {c: {} for c in conn_ct} for mode in modes_ct} for ct in cts}

# Define the directory structure for bare-metal datasets
baremetal_data_path = '/opt/chelsio-experiments/datasets/baremetal/throughput_latency'
containerized_data_path = '/opt/chelsio-experiments/datasets/containerized/throughput_latency'
baremetal_output_path = '/opt/chelsio-experiments/datasets/baremetal/plots'
containerized_output_path = '/opt/chelsio-experiments/datasets/containerized/plots'

for mode in modes_bm:
    for c in conn_bm:
        # Define the full path to the CSV files
        file_path = f'{baremetal_data_path}/{mode}-{c}.csv'
        exps_bm[mode][c] = pd.read_csv(file_path)

for ct in cts:
    for mode in modes_ct:
        for c in conn_ct:
            # Define the full path to the CSV files
            file_path = f'{containerized_data_path}/{ct}-ct/{mode}-{c}.csv'
            exps_ct[ct][mode][c] = pd.read_csv(file_path)

# Plot latency
fig, ax = plt.subplots(figsize=(8,4))

data = {
    "No Offloading": [latency_mean(exps_bm['noktls'][c]) for c in conn_bm],
    "SW kTLS": [latency_mean(exps_bm['swktls'][c]) for c in conn_bm],
    "Coprocessor": [latency_mean(exps_bm['coprocessor'][c]) for c in conn_bm],
    "Inline": [latency_mean(exps_bm['inline'][c]) for c in conn_bm]
}
X = ["1", "8", "16"]
X_axis = np.arange(len(X))
ax.set_xticks(X_axis, X)
ax.set_xlabel("Connections")
ax.set_ylabel("Average Latency (ms)")
ax.set_ylim(0, 30)
bar_plot(ax, data, total_width=.8, single_width=.8, colors=["#ffb000", "#fe6100", "#dc267f", "#785ef0", "#648fff"], label=False)
ax.yaxis.grid(color='gray', linestyle='dashed')
ax.set_axisbelow(True)

plt.rcParams['figure.figsize'] = [18, 4]
plt.savefig(os.path.join(baremetal_output_path, "bm_latency_analysis.pdf"), format="pdf", bbox_inches="tight")

plt.show()

# Plot throughput
fig, ax = plt.subplots(figsize=(8,4))

data = {
    "No Offloading": [throughput_mean(exps_bm['noktls'][c]) for c in conn_bm],
    "SW kTLS": [throughput_mean(exps_bm['swktls'][c]) for c in conn_bm],
    "Coprocessor": [throughput_mean(exps_bm['coprocessor'][c]) for c in conn_bm],
    "Inline": [throughput_mean(exps_bm['inline'][c]) for c in conn_bm],
}

X = ["1", "8", "16"]
X_axis = np.arange(len(X))
ax.set_xticks(X_axis, X)
ax.set_xlabel("Connections")
ax.set_ylabel("Throughput (MB/s)")
ax.set_ylim(0, 1200)
bar_plot(ax, data, total_width=.8, single_width=.8, colors=["#ffb000", "#fe6100", "#dc267f", "#785ef0", "#648fff"], label=False)
ax.yaxis.grid(color='gray', linestyle='dashed')
ax.set_axisbelow(True)

plt.savefig(os.path.join(baremetal_output_path, "bm_throughput_analysis.pdf"), format="pdf", bbox_inches="tight")
plt.show()

# Plot containerized

fig, ax = plt.subplots(1, 4, figsize=(18,4))
for i, ct in enumerate(cts):
    data = {
        "No Offloading": [latency_mean(exps_ct[ct]['noktls'][c]) for c in conn_ct],
        "SW kTLS": [latency_mean(exps_ct[ct]['swktls'][c]) for c in conn_ct],
        "Coprocessor": [latency_mean(exps_ct[ct]['coprocessor'][c]) for c in conn_ct],
    }

    X = modes_ct
    X_axis = np.arange(len(X))
    ax[i].set_title(f'{ct} Container')
    if ct != '1':
        ax[i].set_title(f'{ct} Containers')
    ax[i].set_xticks(X_axis, X)
    ax[i].set_xlabel("Connections")
    ax[i].set_ylabel("Average Latency (ms)")
    ax[i].set_ylim(0, 300)
    bar_plot(ax[i], data, total_width=.8, single_width=.8, colors=["#ffb000", "#fe6100", "#dc267f", "#785ef0", "#648fff"], label=False)
    ax[i].yaxis.grid(color='gray', linestyle='dashed')
    ax[i].set_axisbelow(True)

plt.savefig(os.path.join(containerized_output_path, "ct_latency_analysis.pdf"), format="pdf", bbox_inches="tight")
plt.show()

# Plot throughput
fig, ax = plt.subplots(1, 4, figsize=(18,4))

for i, ct in enumerate(cts):
    data = {
        "No Offloading": [throughput_mean(exps_ct[ct]['noktls'][c]) for c in conn_ct],
        "SW kTLS": [throughput_mean(exps_ct[ct]['swktls'][c]) for c in conn_ct],
        "Coprocessor": [throughput_mean(exps_ct[ct]['coprocessor'][c]) for c in conn_ct],
    }

    X = modes_ct
    X_axis = np.arange(len(X))
    ax[i].set_title(f'{ct} Container')
    if ct != '1':
        ax[i].set_title(f'{ct} Containers')
    ax[i].set_xticks(X_axis, X)
    ax[i].set_xlabel("Connections")
    ax[i].set_ylabel("Throughput (MB/s)")
    ax[i].set_ylim(0, 250)
    bar_plot(ax[i], data, total_width=.8, single_width=.8, colors=["#ffb000", "#fe6100", "#dc267f", "#785ef0", "#648fff"], label=False)
    ax[i].yaxis.grid(color='gray', linestyle='dashed')
    ax[i].set_axisbelow(True)

plt.savefig(os.path.join(containerized_output_path, "ct_throughput_analysis.pdf"), format="pdf", bbox_inches="tight")
plt.show()
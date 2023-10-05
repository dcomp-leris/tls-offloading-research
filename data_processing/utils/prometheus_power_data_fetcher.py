import requests
import pandas as pd
import argparse
import os
from functools import reduce
import json


parser = argparse.ArgumentParser(description='Collect power consumption data from Prometheus for different experiments.')
parser.add_argument('--config-file', required=True, help='Path to the JSON configuration file (experiments.json)')
parser.add_argument('--output-dir', required=True, help='Directory where CSV files will be saved')
args = parser.parse_args()

# Prometheus server configuration
prometheus_host = "http://127.0.0.1:9090"
prometheus_path = "/api/v1/query_range"
step = 15

# Read experiment configurations from the specified JSON file
with open(args.config_file, 'r') as file:
    exps = json.load(file)

def get_power(query, start, end):
    r = requests.post(prometheus_host + prometheus_path, data={'start': start, 'end': end, 'step': step, 'query': query})
    return r.json()['data']['result']

def process_configuration(ct, ctdata):
    for mode, mdata in ctdata.items():
        for conn, cdata in mdata.items():
            query = f'scaph_process_power_consumption_microwatts{{cmdline=~"nginx.*"}}'
            results = get_power(query, cdata['start'], cdata['end'])

            # Get only worker data
            result = list(filter(lambda result: result['metric']['cmdline'] == 'nginx: worker process', results))
            result = result[0]
            
            save_to_csv(result, ct, mode, conn)

def save_to_csv(result, ct, mode, conn):
    frames = []
    frames.append(pd.DataFrame(result['values'], columns=['Time', 'Data']))

    df = pd.concat(frames)
    df = df.sort_values(by=['Time'])
    
    output_dir = args.output_dir
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f'b-m-{ct}-{mode}-{conn}.csv')
    df.to_csv(output_file, index=False)
    print(f'Data saved to {output_file}')

# Process each experiment configuration
for ct, ctdata in exps.items():
    process_configuration(ct, ctdata)

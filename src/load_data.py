# We will do below task
# Read data from data source
# Save in data/raw for further process

import os
from get_data import read_params, get_data
import argparse


def load_and_save(config_path):
    df = get_data(config_path)
    new_cols = [col for col in df.columns]  # To avoid the space in the column name which can create issue further
    print("New columns are", new_cols)


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config",default=os.path.join(os.path.split(os.getcwd())[0], "params.yaml"))
    parsed_args = args.parse_args()
    load_and_save(config_path=parsed_args.config)
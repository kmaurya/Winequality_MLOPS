# We will do below task:
# Read params
# Process data
# Return dataframe

import os
import yaml
import pandas as pd
import argparse


def read_params(config_path):
    with open(config_path) as f:
        response = yaml.safe_load(f)
    return response


def get_data(config_path):
    config = read_params(config_path)
    print(config)
    data_path = config["data_source"]["s3_resource"]

    # While running using main function  use this line
    # df = pd.read_csv(os.path.join(os.path.split(os.getcwd())[0],data_path))

    # While running through dvc repo command use this line
    df = pd.read_csv(data_path)
    print(df.head())
    return df


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default=os.path.join(os.path.split(os.getcwd())[0], "params.yaml"))
    parsed_args = args.parse_args()
    get_data(config_path=parsed_args.config)


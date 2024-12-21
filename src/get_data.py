## read params
## process
## return dataframe
import os
import yaml
import pandas as pd
import argparse

def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

def get_data(config_path):
    config = read_params(config_path)
    # print(config)
    data_path = config["data_source"]["s3_source"]
    df = pd.read_csv(data_path, sep=",", encoding='utf-8')
    # print(df.head())
    return df



if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    data = get_data(config_path=parsed_args.config)

# import os
# import yaml
# import pandas as pd
# import argparse

# def read_params(config_path):
#     try:
#         with open(config_path, "r") as yaml_file:
#             config = yaml.safe_load(yaml_file)
#             if config is None:
#                 raise ValueError(f"Config file {config_path} is empty.")
#             return config
#     except FileNotFoundError:
#         raise FileNotFoundError(f"Config file not found: {config_path}")
#     except yaml.YAMLError as e:
#         raise ValueError(f"Error parsing YAML file {config_path}: {e}")

# def get_data(config_path):
#     config = read_params(config_path)
#     print("Loaded config:", config)  # Debugging
#     data_path = config["data_source"]["s3_source"]
#     if not os.path.exists(data_path):
#         raise FileNotFoundError(f"Data file not found at: {data_path}")
#     df = pd.read_csv(data_path, sep=",", encoding='utf-8')
#     return df

# if __name__ == "__main__":
#     args = argparse.ArgumentParser()
#     args.add_argument("--config", default="params.yaml")
#     parsed_args = args.parse_args()
#     data = get_data(config_path=parsed_args.config)
#     print(data.head())  # Debugging to see the loaded DataFrame

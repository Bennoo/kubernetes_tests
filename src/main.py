import pandas as pd
import os

from modules import configuration, environment

if __name__ == "__main__":
    config_path = environment.get_config_path()
    config = configuration.get_config_parser(config_path)
    username, password = environment.get_dp_credentials()
    test_df = pd.DataFrame()
    print(username)
    print(password)
    print(f'Hello there first param: {config["SECTION"]["first"]}')
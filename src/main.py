import pandas as pd
import configparser
import os

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read('config/config.ini')
    test_df = pd.DataFrame()
    username = os.getenv('DP_USER')
    print(username)
    print(f'Hello there first param: {config["SECTION"]["first"]}')
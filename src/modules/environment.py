import os


def get_config_path():
    return os.getenv('CONFIG_PATH')

def get_dp_credentials():
    return os.getenv('DP_USER'), os.getenv('DP_PASSWORD')
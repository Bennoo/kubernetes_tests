import configparser


def get_config_parser(config_path):
    config = configparser.ConfigParser()
    config.read(config_path)
    return config
import configparser

config = configparser.ConfigParser()

config.read('config.ini')

class Config(object):
    def __init__(self):
        self.map = {
            "database": config['database']['database'],
            "host": config['database']['host'],
            "port": config['database']['port'],
        }

    def get_config(self):
        return self.map

config_map = Config()
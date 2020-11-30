import configparser

def config_dsn():
    config = configparser.ConfigParser()
    config.read('settings.ini')
    return config['dsn']['lib_dir'],config['dsn']['server'], config['dsn']['port'], config['dsn']['service_name']

def config_connect():
    config = configparser.ConfigParser()
    config.read('settings.ini')
    return config['connect']['login'],config['connect']['password']

def query():
    config = configparser.ConfigParser()
    config.read('settings.ini')
    return config['query']['test_query']
import configparser


class Config:
    def __init__(self):
        self.config = configparser.ConfigParser()

    def config_dsn(self):
        self.config.read('settings.ini')
        return self.config['dsn']['lib_dir'], self.config['dsn']['server'], self.config['dsn']['port'], self.config['dsn']['service_name']

    def config_connect(self):
        self.config.read('settings.ini')
        return self.config['connect']['login'], self.config['connect']['password']

    def query_graphic(self):
        self.config.read('settings.ini')
        return self.config['query_graphic']['test_query']

    def query_head_2gh(self):
        self.config.read('settings.ini')
        return self.config['query_2g_h']['col_query_2g_h']

    def query_head_2gd(self):
        self.config.read('settings.ini')
        return self.config['query_2g_d']['col_query_2g_d']

    def query_head_3gh(self):
        self.config.read('settings.ini')
        return self.config['query_3g_h']['col_query_3g_h']

    def query_head_3gd(self):
        self.config.read('settings.ini')
        return self.config['query_3g_d']['col_query_3g_d']

    def query_head_4gh(self):
        self.config.read('settings.ini')
        return self.config['query_4g_h']['col_query_4g_h']

    def query_head_4gd(self):
        self.config.read('settings.ini')
        return self.config['query_4g_d']['col_query_4g_d']

    def n1(self):
        self.config.read('settings.ini')
        return self.config['name1']['2gh']

    def n2(self):
        self.config.read('settings.ini')
        return self.config['name2']['2gd']

    def n3(self):
        self.config.read('settings.ini')
        return self.config['name3']['3gh']

    def n4(self):
        self.config.read('settings.ini')
        return self.config['name4']['3gd']

    def n5(self):
        self.config.read('settings.ini')
        return self.config['name5']['4gh']

    def n6(self):
        self.config.read('settings.ini')
        return self.config['name6']['4gd']
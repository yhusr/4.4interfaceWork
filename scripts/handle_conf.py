import yaml
import configparser
from scripts.handle_os import YAML_PATH, CONF_PATH


class HandleYaml:
    def __init__(self, filepath=None):
        if filepath:
            self.filepath = filepath
        else:
            self.filepath = YAML_PATH

    def read_yaml(self, section_name, option_name):
        with open(self.filepath, 'r', encoding='utf-8') as f:
            ry = yaml.full_load(f)
        result = ry[section_name][option_name]
        return result

    def write_yaml(self, datas, mode='a'):
        with open(self.filepath, mode, encoding='utf-8') as f:
            yaml.dump(datas, f, allow_unicode=True)


hy = HandleYaml()


class HandleConf:
    def __init__(self, filepath=None):
        if filepath:
            self.filepath = filepath
        else:
            self.filepath = CONF_PATH
        self.conf = configparser.ConfigParser()

    def read_conf(self, section_name, option_name):
        self.conf.read(self.filepath, encoding='utf-8')
        result1 = self.conf[section_name][option_name]
        try:
            result1 = eval(result1)
        except NameError as e:
            result1 = result1
        return result1

    def write_conf(self, datas):
        for data in datas:
            self.conf[data] = datas[data]
        with open(self.filepath, 'a', encoding='utf-8') as f:
            self.conf.write(f)


if __name__ == '__main__':
    # hy = HandleYaml()
    # result = hy.read_yaml('mysql', 'host')
    # print(result)
    # dict1 = {'mysql': {
    #     'db': 'course'
    # }}
    # hy.write_yaml(dict1)
    hc = HandleConf()
    result = hc.read_conf('mysql', 'name')
    print(result)
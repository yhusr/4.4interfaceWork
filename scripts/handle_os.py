import os


current_path = os.path.abspath(__file__)
SCRIPTS_PATH = os.path.dirname(current_path)
ROOT_PATH = os.path.dirname(SCRIPTS_PATH)

# data数据path路径
DATA_PATH = os.path.join(ROOT_PATH, 'data')
EXCEL_PATH = os.path.join(DATA_PATH, 'excelcases.xlsx')

# print(EXCEL_PATH)
# config配置文件的路径：
config_path = os.path.join(ROOT_PATH, 'config')
YAML_PATH = os.path.join(config_path, 'confYaml.yaml')
CONF_PATH = os.path.join(config_path, 'para_conf.ini')

# log日志文件的存放路径
LOG_PATH = os.path.join(ROOT_PATH, 'logs')

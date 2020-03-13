import os
from utils.YamlUtil import YamlRead

# 获取项目基本路径
base_url = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# config目录
config_url = os.path.join(base_url,'config')

# 获取conf.yml目录 os.sep 拼接路径
confyml_url = os.path.join(config_url,'conf.yml')

# 读取配置文件
class ConfYaml:
    def __init__(self):
        self.conf_yaml = YamlRead(confyml_url).data()

    #读取数据
    def get_yaml_data(self):
        return self.conf_yaml['BASE']['test']['url']

if __name__ == '__main__':
    c = ConfYaml()
    print(c.get_yaml_data())
    url = c.get_yaml_data()
    url_2 = url+os.sep+"authorizations/"
    url_1 = os.path.join(url,"authorizations/")
    print(url_1)
    print(url_2)

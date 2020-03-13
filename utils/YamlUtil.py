
import os
import yaml

class YamlRead:
    def __init__(self,yaml_file):
        if os.path.exists(yaml_file):
            self.file = yaml_file
        else:
            raise FileNotFoundError("未找到文件")

    def data(self):
        with open(self.file,"rb") as f:
            r = yaml.safe_load(f)
        return r

    def data_all(self):
        with open(self.file,"rb") as f:
            # r 是个对象
            # r = list(yaml.safe_load_all(f))
            r = list(yaml.safe_load_all(f))
        return r

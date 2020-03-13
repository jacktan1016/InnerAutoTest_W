
import yaml
# 创建yml对象
# with open("conf.yml","rb") as f:
#     r = yaml.safe_load_all(f)
#     # 读取文件,all是一个对象,循环取值
#     for i in r:
#         print(i)
from utils.YamlUtil import YamlRead

yaml_read = YamlRead("data.yml")
# data = yaml_read.data()
data = yaml_read.data_all()
print(data)
"""
  @Time    : 2020/4/12 18:50
  @Author  : Bug管理员-zeng
  @Site    : 
  @File    : read_yaml.py
  @Software: PyCharm
"""
import yaml

from config import BASE_OS


def build_data_func():
    with open(BASE_OS + 'data\login_data.yaml', encoding='utf-8')as f:
        data = yaml.safe_load(f)
        print(data)
        print(type(data))
    return data

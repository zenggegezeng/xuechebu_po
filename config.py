import os

# BASE_DIR在哪被调用就是获取当前调用BASE_DIR的执行py文件的上一级目录
BASE_DIR = os.getcwd() + os.sep
# print(BASE_DIR)

# BASE_OS就是获取当前py文件的根目录
BASE_OS = os.path.abspath(os.path.dirname(__file__)) + os.sep
# print(BASE_OS)

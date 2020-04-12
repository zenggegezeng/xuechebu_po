"""
  @Time    : 2020/4/10 15:38
  @Author  : Bug管理员-zeng
  @Site    : 
  @File    : utils.py
  @Software: PyCharm
"""
# 1. 导包
from appium import webdriver


def get_driver():
    """获取公共驱动对象方法"""
    # 2. 实例化驱动对象
    capabilities_android = dict()  # 等价于capabilities_android = {}
    # 系统类型
    capabilities_android['platformName'] = "Android"
    # 系统版本
    capabilities_android['platformVersion'] = "5"
    # 设备名称
    capabilities_android['deviceName'] = "模拟器"
    # 被测应用包名
    capabilities_android['appPackage'] = "com.bjcsxq.chat.carfriend"
    # 被测应用启动名
    capabilities_android['appActivity'] = ".MainActivity"

    # 解决无法输入中文问题
    # 启用Unicode输入，默认 false
    capabilities_android['unicodeKeyboard'] = True
    # 当 unicodeKeyboard为True时,将键盘重置为其原始状态,解决不能输入中文的原因
    capabilities_android['resetKeyboard'] = True

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',
                              desired_capabilities=capabilities_android)
    return driver


if __name__ == '__main__':
    driver = get_driver()
    print(driver)

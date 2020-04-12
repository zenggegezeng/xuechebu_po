"""
  @Time    : 2020/4/10 15:47
  @Author  : Bug管理员-zeng
  @Site    : 
  @File    : base_page.py
  @Software: PyCharm
"""
from selenium.webdriver.support.wait import WebDriverWait

"""

PO文件基类

"""


class BasePage(object):
    """po文件基类"""

    def __init__(self, driver):  # 封装代码过程中, 如果需要驱动对象, 直接编写此方法
        self.driver = driver

    def find_element_func(self, location, timeout=5, poll=.5):
        """
        :param location: 元素定位信息
        :param timeout:  显示等待超时时长
        :param poll:  显示等待执行间隔
        :return:  返回定位到的元素对象
        """
        # 添加显示等待
        element = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll) \
            .until(lambda x: x.find_element(*location))
        return element

    def input_func(self, element, text):
        """
        :param element: 元素对象
        :param text: 输入的内容
        :return: 无
        """
        element.clear()  # 清空
        element.send_keys(text)  # 输入

    def click_func(self, element):
        """
        :param element: 元素对象
        :return: 无
        """
        element.click()

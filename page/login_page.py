"""
  @Time    : 2020/4/10 16:14
  @Author  : Bug管理员-zeng
  @Site    :
  @File    : index_page.py
  @Software: PyCharm
"""

from base.base_page import BasePage
import page

"""

登录页面

"""


class LoginPage(BasePage):
    """登录页面"""

    def input_phone_box(self, text):
        """登录页面账号输入框输入方法"""
        # 调用基类的输入框输入方法
        self.input_func(self.find_element_func(page.phone_box), text)

    def input_pwd_box(self, text):
        """登录页面账号输入框输入方法"""
        # 调用基类的输入框输入方法
        self.input_func(self.find_element_func(page.pwd_box), text)

    # 根据目标元素的操作类型和元素名称得出封装方法名
    def click_login_btn(self):
        """
        登录页面登录按钮点击方法
        :return: 无
        """
        # 调用基类的点击方法(传入元素对象)
        self.click_func(self.find_element_func(page.login_btn))

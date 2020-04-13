"""
  @Time    : 2020/4/10 16:56
  @Author  : Bug管理员-zeng
  @Site    : 
  @File    : test_login.py
  @Software: PyCharm
"""
import allure
import pytest
import time

from read_data.read_yaml import build_data_func
from page.page_factory import PageFactory
from utils import get_driver

"""
登录测试用例
"""


class TestLogin(object):
    """搜索测试用例"""

    @pytest.fixture(autouse=True)
    def before_func(self):
        self.driver = get_driver()
        self.page_factory = PageFactory(self.driver)  # 实例化页面对象统一入口类
        yield
        time.sleep(3)
        self.driver.quit()  # 退出驱动对象

    @pytest.mark.parametrize('phone, pwd', build_data_func())
    @allure.MASTER_HELPER.step(title='登陆测试步骤001')  # 添加测试步骤 第二代语法
    @allure.MASTER_HELPER.severity(
        allure.MASTER_HELPER.severity_level.CRITICAL)  # 作⽤： 测试⽤例设置不同的严重级别， 可以帮助测试和开发⼈员更直观的关注重要Case
    def test_login_func(self, phone, pwd):
        """搜索测试方法"""
        # 点击我的按钮 跳转我的页面
        allure.MASTER_HELPER.attach("点击我的按钮", "跳转我的页面")
        self.page_factory.index_page().click_me_btn()
        time.sleep(2)
        # 点击登录注册按钮 跳转登录页面
        allure.MASTER_HELPER.attach("点击登录注册按钮", "跳转登录页面")
        self.page_factory.me_page().click_login_sign_btn()

        # 输入账号密码登录
        allure.MASTER_HELPER.attach("登录", "输入账号密码登录")
        self.page_factory.login_page().input_phone_box(phone)
        self.page_factory.login_page().input_pwd_box(pwd)
        # 点击登录按钮
        self.page_factory.login_page().click_login_btn()

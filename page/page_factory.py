"""
 统一入口类(集中封装页面对象的实例化操作)
"""
from page.index_page import IndexPage
from page.login_page import LoginPage
from page.me_page import MePage


class PageFactory(object):
    """页面对象统一入口类"""

    def __init__(self, driver):
        self.driver = driver

    def index_page(self):
        """首页"""
        return IndexPage(self.driver)  # 返回页面实例化对象

    def me_page(self):
        """我的页面"""
        return MePage(self.driver)  # 返回页面实例化对象

    def login_page(self):
        """我的页面"""
        return LoginPage(self.driver)  # 返回页面实例化对象

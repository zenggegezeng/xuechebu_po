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

我的首页

"""


class MePage(BasePage):
    """我的页面"""

    # 根据目标元素的操作类型和元素名称得出封装方法名
    def click_login_sign_btn(self):
        """
        我的页面登录注册按钮点击方法
        :return: 无
        """
        # 调用基类的点击方法(传入元素对象)
        self.click_func(self.find_element_func(page.login_sign_btn))

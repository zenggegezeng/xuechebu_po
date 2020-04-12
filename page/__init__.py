"""
 元素对立文件(元素定位信息进行统一管理)
"""
from selenium.webdriver.common.by import By

# 首页
me_btn = (By.ID, 'com.bjcsxq.chat.carfriend:id/tv_home_mine')  # 我的

# 我的页面
login_sign_btn = (By.ID, 'com.bjcsxq.chat.carfriend:id/mine_username_tv')  # 登录/注册

# 登录页面
phone_box = (By.ID, 'com.bjcsxq.chat.carfriend:id/login_phone_et')  # 账号输入框
pwd_box = (By.ID, 'com.bjcsxq.chat.carfriend:id/login_pwd_et')  # 密码输入框
login_btn = (By.ID, 'com.bjcsxq.chat.carfriend:id/login_btn')  # 登录按钮

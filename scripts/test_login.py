from appium import webdriver

from base.base_driver import init_driver
from page.home_page import HomePage
from page.login_page import LoginPage
from page.reg_page import RegPage


class TestLogin:

    def setup(self):
        self.driver = init_driver()

        self.home_page = HomePage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.reg_page = RegPage(self.driver)

    def test_login(self):
        # 首页 点击 我
        self.home_page.click_me()
        # 注册 点击 已有账号去登陆
        self.reg_page.click_go_to_login()
        # 登陆 输入 用户名
        self.login_page.input_username("itfeat")
        # 登陆 输入 密码
        self.login_page.input_password("itfeat123000")
        # 登陆 点击 登陆
        self.login_page.click_login()

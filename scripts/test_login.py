import pytest
from appium import webdriver

from base.base_analyze import analyze_data
from base.base_driver import init_driver
from page.home_page import HomePage
from page.login_page import LoginPage
from page.me_page import MePage
from page.page import Page
from page.reg_page import RegPage


class TestLogin:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)
        self.driver.implicitly_wait(10)

        # self.home_page = HomePage(self.driver)
        # self.login_page = LoginPage(self.driver)
        # self.reg_page = RegPage(self.driver)
        # self.me_page = MePage(self.driver)

    def find_toast(self, message):
        try:
            print("-----")
            print(self.driver.find_element_by_xpath("//*[contains(@text,'%s')]" % message).text)
            print("-----")
            return True
        except Exception:
            return False


    # def test_login_with_wrong_password(self):
    #     # 首页 点击 我
    #     self.page.home.click_me()
    #     # 注册 点击 已有账号去登陆
    #     self.page.reg.click_go_to_login()
    #     # 登陆 输入 用户名
    #     self.page.login.input_username("itfeat")
    #     # 登陆 输入 密码
    #     self.page.login.input_password("itfeat10")
    #     # 登陆 点击 登陆
    #     self.page.login.click_login()
    #
    #     assert self.find_toast("密码错误")



    @pytest.mark.parametrize("args", analyze_data("login_data.yaml", "test_login"))
    def test_login(self, args):
        username = args["username"]
        password = args["password"]
        expect = args["expect"]

        # 首页 点击 我
        self.page.home.click_me()
        # 注册 点击 已有账号去登陆
        self.page.reg.click_go_to_login()
        # 登陆 输入 用户名
        self.page.login.input_username(username)
        # 登陆 输入 密码
        self.page.login.input_password(password)
        # 登陆 点击 登陆
        self.page.login.click_login()

        if expect is None:
            # 断言
            assert self.page.me.get_username() == username
        else:
            assert self.find_toast(expect)



        # # 首页 点击 我
        # self.home_page.click_me()
        # # 注册 点击 已有账号去登陆
        # self.reg_page.click_go_to_login()
        # # 登陆 输入 用户名
        # self.login_page.input_username("itfeat")
        # # 登陆 输入 密码
        # self.login_page.input_password("itfeat123000")
        # # 登陆 点击 登陆
        # self.login_page.click_login()
        #
        # # 断言
        # assert self.me_page.get_username() == "itfeat"

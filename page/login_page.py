from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class LoginPage(BaseAction):

    # 登陆 - 用户名
    username_edit_text = By.ID, "com.yunmall.lc:id/logon_account_textview"
    # 登陆 - 密码
    password_edit_text = By.ID, "com.yunmall.lc:id/logon_password_textview"
    # 登陆 - 按钮
    login_button = By.ID, "com.yunmall.lc:id/logon_button"

    # 登陆 输入 用户名
    def input_username(self, text):
        self.input(self.username_edit_text, text)

    # 登陆 输入 密码
    def input_password(self, text):
        self.input(self.password_edit_text, text)

    # 登陆 点击 登陆
    def click_login(self):
        self.click(self.login_button)
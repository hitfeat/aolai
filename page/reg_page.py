from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class RegPage(BaseAction):

    # 注册 - 去登陆
    go_to_login_button = By.XPATH, "//*[@text='已有账号，去登录']"

    # 注册 点击 去登陆
    def click_go_to_login(self):
        self.click(self.go_to_login_button)

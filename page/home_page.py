from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class HomePage(BaseAction):

    # 主页 - 我
    me_button = By.ID, "com.yunmall.lc:id/tab_me"

    # 主页 点击 我
    def click_me(self):
        self.click(self.me_button)

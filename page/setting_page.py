from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class SettingPage(BaseAction):

    # 设置 - 关于百年奥莱
    about_aolai_button = By.XPATH, "//*[@text='关于百年奥莱']"

    # 设置 点击 关于百年奥莱
    def click_about_aolai(self):
        self.scroll_to_feature(self.about_aolai_button).click()
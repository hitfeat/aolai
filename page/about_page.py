from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class AboutPage(BaseAction):

    # 关于 - 版本更新
    update_button = By.ID, "com.yunmall.lc:id/about_version_update"

    # 关于 点击 版本更新
    def click_update(self):
        self.click(self.update_button)
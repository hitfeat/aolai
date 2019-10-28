from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MePage(BaseAction):

    # 我 - 用户名
    username_text_view = By.ID, "com.yunmall.lc:id/tv_user_nikename"

    # 我 获取 用户名
    def get_username(self):
        return self.get_text(self.username_text_view)
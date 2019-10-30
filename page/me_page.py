from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MePage(BaseAction):

    # 我 - 用户名
    username_text_view = By.ID, "com.yunmall.lc:id/tv_user_nikename"

    # 我 - 设置
    setting_button = By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image"

    # 我 - 加入超级vip
    vip_button = By.XPATH, "//*[@text='加入超级VIP']"

    # 我 获取 用户名
    def get_username(self):
        return self.get_text(self.username_text_view)

    # 我 点击 设置
    def click_setting(self):
        self.scroll_to_feature(self.setting_button).click()

    # 我 点击 加入超级vip
    def click_vip(self):
        self.scroll_to_feature(self.vip_button).click()
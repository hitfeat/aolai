from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MePage(BaseAction):

    # 主页 - 我
    me_button = By.ID, "com.yunmall.lc:id/tab_me"

    # 主页 - 分类
    category_button = By.ID, "com.yunmall.lc:id/tab_category"

    # 主页 点击 我
    def click_me(self):
        self.click(self.me_button)

    # 主页 点击 分类
    def click_category(self):
        self.click(self.category_button)

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
import time

from base.base_driver import init_driver
from page.page import Page


class TestCache:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    def test_clear_cache(self):
        # 如果没有登录则登录，此时会停留在"我"的页面
        self.page.home.login_if_not(self.page)
        # 我 点击 设置
        self.page.me.click_setting()
        # 设置 点击 关于百年奥莱
        self.page.setting.click_clear_cache()

        # 断言toast是否存在
        self.page.setting.is_toast_exist("清理成功")
import time

from base.base_driver import init_driver
from page.page import Page


class TestAddress:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    def test_add_address(self):
        # 如果没有登录则登录，此时会停留在"我"的页面
        self.page.home.login_if_not(self.page)
        # 我 点击 设置
        self.page.me.click_setting()
        self.page.setting.click_address()
        self.page.address_list.click_new_address()
        self.page.edit_address.input_name("zhangsan")
        self.page.edit_address.input_phone("18888888888")
        self.page.edit_address.input_detail("2单元 302")
        self.page.edit_address.input_postal_code("100000")
        self.page.edit_address.click_default()

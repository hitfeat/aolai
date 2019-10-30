import time

import pytest

from base.base_analyze import analyze_data
from base.base_driver import init_driver
from page.page import Page


class TestAddress:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    @pytest.mark.parametrize("args", analyze_data("address_data.yaml", "test_add_address"))
    def test_add_address(self, args):
        name = args["name"]
        phone = args["phone"]
        info = args["info"]
        post_code = args["post_code"]
        toast = args["toast"]

        # 如果没有登录则登录，此时会停留在"我"的页面
        self.page.home.login_if_not(self.page)
        # 我 点击 设置
        self.page.me.click_setting()
        self.page.setting.click_address()
        self.page.address_list.click_new_address()
        self.page.edit_address.input_name(name)
        self.page.edit_address.input_phone(phone)
        self.page.edit_address.input_detail(info)
        self.page.edit_address.input_postal_code(post_code)
        self.page.edit_address.click_default()
        self.page.edit_address.click_region()
        self.page.edit_address.click_save()

        if toast is None:
            assert self.page.address_list.get_default_receipt_name_text() == "%s  %s" % (name, phone)
        else:
            assert self.page.edit_address.is_toast_exist(toast)

    def test_edit_address(self):
               # 如果没有登录则登录，此时会停留在"我"的页面
        self.page.home.login_if_not(self.page)
        # 我 点击 设置
        self.page.me.click_setting()
        self.page.setting.click_address()
        if not self.page.address_list.is_default_exist():  # 如果不存在，添加地址
            self.page.address_list.click_new_address()
            self.page.edit_address.input_name("李四")
            self.page.edit_address.input_phone("17777777777")
            self.page.edit_address.input_detail("二单元 305")
            self.page.edit_address.input_postal_code("100000")
            self.page.edit_address.click_default()
            self.page.edit_address.click_region()
            self.page.edit_address.click_save()

        # 准备修改
        self.page.address_list.click_default()
        self.page.edit_address.input_name("李四123")
        self.page.edit_address.input_phone("18888888888")
        self.page.edit_address.input_detail("1单元 405")
        self.page.edit_address.input_postal_code("120000")
        self.page.edit_address.click_region()
        self.page.edit_address.click_save()

        assert self.page.address_list.is_toast_exist("保存成功")
        assert self.page.address_list.get_default_receipt_name_text() == "%s  %s" % ("李四123", "18888888888")

    def test_delete_address(self):
        # 如果没有登录则登录，此时会停留在"我"的页面
        self.page.home.login_if_not(self.page)
        # 我 点击 设置
        self.page.me.click_setting()
        self.page.setting.click_address()
        if not self.page.address_list.is_default_exist():  # 如果不存在，添加地址
            self.page.address_list.click_new_address()
            self.page.edit_address.input_name("李四")
            self.page.edit_address.input_phone("17777777777")
            self.page.edit_address.input_detail("二单元 305")
            self.page.edit_address.input_postal_code("100000")
            self.page.edit_address.click_default()
            self.page.edit_address.click_region()
            self.page.edit_address.click_save()

        self.page.address_list.delete_all_address()

        assert not self.page.address_list.is_default_exist()






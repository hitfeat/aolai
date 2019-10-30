import pytest
from appium import webdriver

from base.base_analyze import analyze_data
from base.base_driver import init_driver
from page.page import Page


class TestVip:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    @pytest.mark.parametrize("args", analyze_data("vip_data.yaml", "test_vip"))
    def test_vip(self, args):
        code = args["code"]
        expect = args["expect"]

        # 如果没有登录则登录，此时会停留在"我"的页面
        self.page.home.login_if_not(self.page)
        # 我 点击 vip
        self.page.me.click_vip()
        # vip 输入 邀请码
        self.page.vip.input_code(code)
        # vip 点击 成为会员
        self.page.vip.click_be_vip()

        assert self.page.vip.is_can_not_be_vip(expect)

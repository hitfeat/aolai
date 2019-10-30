import time

from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class VipPage(BaseAction):

    # vip - 邀请码
    code_edit_text = By.XPATH, "//*[@placeholder='邀请码必填']"

    # vip - 成为会员
    be_vip_button = By.XPATH, "//*[@value='立即成为会员']"

    # vip 输入 邀请码
    def input_code(self, text):
        time.sleep(3)
        print(self.driver.contexts)
        self.driver.switch_to.context("WEBVIEW_com.yunmall.lc")
        self.input(self.code_edit_text, text)
        self.driver.switch_to.context("NATIVE_APP")

    # vip 点击 成为会员
    def click_be_vip(self):
        self.driver.switch_to.context("WEBVIEW_com.yunmall.lc")
        self.click(self.be_vip_button)
        self.driver.switch_to.context("NATIVE_APP")

    # 是不是 不能成为 vip
    def is_can_not_be_vip(self, keyword):
        self.driver.switch_to.context("WEBVIEW_com.yunmall.lc")
        res = self.is_keyword_in_page_source(keyword)
        self.driver.switch_to.context("NATIVE_APP")
        return res




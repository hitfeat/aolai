from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class AddressListPage(BaseAction):

    # 地址管理 - 新增地址
    new_address_button = By.XPATH, "//*[@text='新增地址']"

    def click_new_address(self):
        self.scroll_to_feature(self.new_address_button).click()

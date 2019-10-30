from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class AddressListPage(BaseAction):

    # 地址管理 - 新增地址
    new_address_button = By.XPATH, "//*[@text='新增地址']"

    # 收件人的信息
    receipt_name_feature = By.ID, "com.yunmall.lc:id/receipt_name"

    def click_new_address(self):
        self.scroll_to_feature(self.new_address_button).click()

    def get_default_receipt_name_text(self):
        return self.get_text(self.receipt_name_feature)

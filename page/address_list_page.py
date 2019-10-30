import time

from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class AddressListPage(BaseAction):

    # 地址管理 - 新增地址
    new_address_button = By.XPATH, "//*[@text='新增地址']"

    # 收件人的信息
    receipt_name_feature = By.ID, "com.yunmall.lc:id/receipt_name"

    # 默认标记
    default_feature = By.ID, "com.yunmall.lc:id/address_is_default"

    # 编辑
    edit_button = By.XPATH, "//*[@text='编辑']"
    # 删除
    delete_button = By.XPATH, "//*[@text='删除']"
    # 确认
    confirm_button = By.XPATH, "//*[@text='确认']"

    def click_new_address(self):
        self.scroll_to_feature(self.new_address_button).click()

    def get_default_receipt_name_text(self):
        return self.get_text(self.receipt_name_feature)

    def is_default_exist(self):
        return self.is_feature_exist(self.default_feature)

    def click_default(self):
        self.click(self.default_feature)

    def click_edit(self):
        self.click(self.edit_button)

    def click_delete(self):
        self.click(self.delete_button)

    def click_confirm(self):
        self.click(self.confirm_button)

    def delete_all_address(self):
        for i in range(10):
            self.click_edit()
            time.sleep(1)
            if not self.is_feature_exist(self.delete_button):
                print("提前删除完毕")
                return

            self.click_delete()
            time.sleep(1)
            self.click_confirm()
            time.sleep(1)

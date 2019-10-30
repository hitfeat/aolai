from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class EditAddressPage(BaseAction):

    # 编辑地址 - 收件人
    name_edit_text = By.ID, "com.yunmall.lc:id/address_receipt_name"
    # 编辑地址 - 手机号
    phone_edit_text = By.ID, "com.yunmall.lc:id/address_add_phone"
    # 编辑地址 - 详细地址
    detail_edit_text = By.ID, "com.yunmall.lc:id/address_detail_addr_info"
    # 编辑地址 - 邮编
    postal_code_edit_text = By.ID, "com.yunmall.lc:id/address_post_code"
    # 编辑地址 - 默认地址
    default_button = By.ID, "com.yunmall.lc:id/address_default"

    def input_name(self, text):
        self.input(self.name_edit_text, text)

    def input_phone(self, text):
        self.input(self.phone_edit_text, text)

    def input_detail(self, text):
        self.input(self.detail_edit_text, text)

    def input_postal_code(self, text):
        self.input(self.postal_code_edit_text, text)

    def click_default(self):
        self.click(self.default_button)



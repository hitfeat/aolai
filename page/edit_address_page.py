import random
import time

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
    # 编辑地址 - 所在地区
    region_button = By.ID, "com.yunmall.lc:id/address_province"

    # 将要被选择的省市区的特征
    area_feature = By.ID, "com.yunmall.lc:id/area_title"

    save_button = By.XPATH, "//*[@text='保存']"


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

    def click_region(self):
        self.click(self.region_button)
        self.choose_region()

    def click_save(self):
        self.click(self.save_button)

    def choose_region(self):
        """执行这个方法之后，会选择省市区"""
        while True:
            time.sleep(1)
            if self.driver.current_activity != "com.yunmall.ymctoc.ui.activity.ProvinceActivity":
                return
            areas = self.find_elements(self.area_feature)
            areas_count = len(areas)
            index = random.randint(0, areas_count - 1)
            areas[index].click()
            time.sleep(1)








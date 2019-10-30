import random

from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class GoodsListPage(BaseAction):

    goods_detail_button = By.ID, "com.yunmall.lc:id/iv_element_1"

    def click_random_goods_detail(self):
        goods_details = self.find_elements(self.goods_detail_button)
        goods_details_count = len(goods_details)
        index = random.randint(0, goods_details_count - 1)
        goods_details[index].click()

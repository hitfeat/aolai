import random

from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class CategoryPage(BaseAction):

    goods_category_button = By.ID, "com.yunmall.lc:id/iv_img"

    def click_random_goods_category(self):
        goods_categories = self.find_elements(self.goods_category_button)
        goods_categories_count = len(goods_categories)
        index = random.randint(0, goods_categories_count - 1)
        goods_categories[index].click()

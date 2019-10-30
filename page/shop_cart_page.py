from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class ShopCartPage(BaseAction):

    def is_product_title_exist(self, product_title):
        return self.is_feature_exist((By.XPATH, "//*[@text='%s']" % product_title))


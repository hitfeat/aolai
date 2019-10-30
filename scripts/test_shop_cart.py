import time

from base.base_driver import init_driver
from page.page import Page


class TestShopCart:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(3)
        # self.driver.quit()

    def test_add_shop_cart(self):
        # 如果没有登录则登录，此时会停留在"我"的页面
        self.page.home.login_if_not(self.page)
        # 我 点击 分类
        self.page.me.click_category()
        self.page.category.click_random_goods_category()
        self.page.goods_list.click_random_goods_detail()

        # 获取 要加入的商品的名称
        product_title = self.page.goods_detail.get_product_title()

        self.page.goods_detail.click_add_shop_cart()

        # 选择所有规格，并且点击确定
        self.page.goods_detail.choose_spec()

        self.page.goods_detail.click_shop_cart()
        assert self.page.shop_cart.is_product_title_exist(product_title)




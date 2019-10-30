import random

from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class GoodsDetailPage(BaseAction):
    add_shop_cart_button = By.XPATH, "//*[@text='加入购物车']"

    # 确认按钮
    confirm_button = By.ID, "com.yunmall.lc:id/select_detail_sure_btn"

    # 商品详情的标题
    product_title_feature = By.ID, "com.yunmall.lc:id/tv_product_title"

    # 购物车
    shop_cart_button = By.ID, "com.yunmall.lc:id/btn_shopping_cart"

    def click_add_shop_cart(self):
        self.click(self.add_shop_cart_button)

    def click_confirm(self):
        self.click(self.confirm_button)

    def get_should_spec(self):
        """
        获取应该选择的规格的分类
        :return:
        """
        if self.is_toast_exist("请选择"):
            return self.get_toast_text("请选择").split(" ")[1]
        return None

    def choose_spec(self):
        """
        选择完所有的规格，并确定
        :return:
        """
        while True:
            self.click_confirm()
            should_spec = self.get_should_spec()
            if should_spec is None:
                # 如果为空，则意味着已经选择完毕，并且已经点击了确认
                return
            self.choose_first_spec(should_spec)

    def choose_first_spec(self, spec_name):
        """
        根据应该选择的规格的分类的名字，选择第一个规格
        :param spec_name:
        :return:
        """
        self.click((By.XPATH, "//*[@text='%s']/../*[2]/*[1]" % spec_name))

    def get_product_title(self):
        return self.get_text(self.product_title_feature)

    def click_shop_cart(self):
        self.click(self.shop_cart_button)



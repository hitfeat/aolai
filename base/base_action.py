from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, feature, timeout=10.0, poll_frequency=1.0):
        return WebDriverWait(self.driver, timeout, poll_frequency).until(lambda x: x.find_element(*feature))

    def click(self, feature, timeout=10.0, poll_frequency=1.0):
        self.find_element(feature, timeout, poll_frequency).click()

    def clear(self, feature, timeout=10.0, poll_frequency=1.0):
        self.find_element(feature, timeout, poll_frequency).clear()

    def input(self, feature, text, timeout=10.0, poll_frequency=1.0):
        self.clear(feature)
        self.find_element(feature, timeout, poll_frequency).send_keys(text)

    def get_text(self, feature, timeout=10.0, poll_frequency=1.0):
        return self.find_element(feature, timeout, poll_frequency).text

    def is_toast_exist(self, message):
        """
        根据部分toast的内容，判断该toast是否存在
        :param message: 部分内容
        :return: 是否存在
        """
        try:
            feature = By.XPATH, "//*[contains(@text,'%s')]" % message
            self.find_element(feature, 5, 0.1)
            return True
        except Exception:
            return False

    def get_toast_text(self, message):
        """
        根据部分toast的内容，获取全部的内容
        :param message: 部分内容
        :return: 全部内容（如果存在）
        """
        if self.is_toast_exist(message):
            feature = By.XPATH, "//*[contains(@text,'%s')]" % message
            return self.find_element(feature, 5, 0.1).text
        else:
            raise Exception("没有找到toast，无法获取toast上的内容")

    def scroll_page_one_time(self, direction="up"):
        """
        滑动屏幕一次
        :param direction:
            up: 从下往上
            down: 从上往下
            left: 从右往左
            right: 从左往右
        :return:
        """
        screen_width = self.driver.get_window_size()["width"]
        screen_height = self.driver.get_window_size()["height"]

        top_x = screen_width * 0.5
        top_y = screen_height * 0.25
        bottom_x = top_x
        bottom_y = screen_height * 0.75
        left_x = screen_width * 0.25
        left_y = screen_height * 0.5
        right_x = screen_width * 0.75
        right_y = left_y

        if direction == "up":
            self.driver.swipe(bottom_x, bottom_y, top_x, top_y)
        elif direction == "down":
            self.driver.swipe(top_x, top_y, bottom_x, bottom_y)
        elif direction == "left":
            self.driver.swipe(right_x, right_y, left_x, left_y)
        elif direction == "right":
            self.driver.swipe(left_x, left_y, right_x, right_y)

    def scroll_to_feature(self, feature, direction="up"):
        """
        滑动到执行的元素
        :param feature:
        :param direction:
        :return:
        """
        page_source = ""
        while True:
            try:
                return self.driver.find_element(*feature)

            except Exception:

                self.scroll_page_one_time(direction)

                if self.driver.page_source == page_source:
                    print("到底了")
                    break
                page_source = self.driver.page_source

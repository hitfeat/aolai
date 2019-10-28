from appium import webdriver


# 创建一个字典，包装相应的启动参数
from selenium.webdriver.common.by import By

desired_caps = dict()
# 需要连接的手机的平台(不限制大小写)
desired_caps['platformName'] = 'Android'
# 需要连接的手机的版本号(比如 5.2.1 的版本可以填写 5.2.1 或 5.2 或 5 ，以此类推)
desired_caps['platformVersion'] = '5.1'
# 需要连接的手机的设备号(andoird平台下，可以随便写，但是不能不写)
desired_caps['deviceName'] = 'huawei p30'
# 需要启动的程序的包名
desired_caps['appPackage'] = 'com.android.settings'
# 需要启动的程序的界面名
desired_caps['appActivity'] = '.Settings'

# 使用 查找toast
desired_caps['automationName'] = 'Uiautomator2'

# 连接appium服务器
driver = webdriver.Remote('http://192.168.1.64:4723/wd/hub', desired_caps)


def scroll_page_one_time(direction="up"):
    """
    滑动屏幕一次
    :param direction:
        up: 从下往上
        down: 从上往下
        left: 从右往左
        right: 从左往右
    :return:
    """
    screen_width = driver.get_window_size()["width"]
    screen_height = driver.get_window_size()["height"]

    top_x = screen_width * 0.5
    top_y = screen_height * 0.25
    bottom_x = top_x
    bottom_y = screen_height * 0.75
    left_x = screen_width * 0.25
    left_y = screen_height * 0.5
    right_x = screen_width * 0.75
    right_y = left_y

    if direction == "up":
        driver.swipe(bottom_x, bottom_y, top_x, top_y)
    elif direction == "down":
        driver.swipe(top_x, top_y, bottom_x, bottom_y)
    elif direction == "left":
        driver.swipe(right_x, right_y, left_x, left_y)
    elif direction == "right":
        driver.swipe(left_x, left_y, right_x, right_y)


def scroll_to_feature(feature, direction="up"):

    page_source = ""
    while True:
        try:
            return driver.find_element(*feature)

        except Exception:

            scroll_page_one_time(direction)

            if driver.page_source == page_source:
                print("到底了")
                break
            page_source = driver.page_source


scroll_to_feature((By.XPATH, "//*[@text='打印']")).click()
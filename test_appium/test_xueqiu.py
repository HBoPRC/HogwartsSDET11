from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestXueQiu:
    def setup(self):
        caps = {}
        caps['platformName'] = 'Android'
        caps['deviceName'] = 'emulator-5554'
        caps['appPackage'] = 'com.xueqiu.android'
        caps['appActivity'] = '.view.WelcomeActivityAlias'
        # 是否清理数据
        caps['noReset'] = True
        # 输入中文
        caps['unicodeKeyboard'] = True
        # 测试结束后恢复键盘，真机上跑的时候需要加上
        caps['resetKeyboard'] = True

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
        self.driver.implicitly_wait(30)

    def test_price(self):
        # 点击搜索框
        self.driver.find_element(MobileBy.ID, 'tv_search').click()
        # 点击文本框
        self.driver.find_element(MobileBy.ID, 'search_input_text').click()
        # 在文本框输入阿里巴巴
        self.driver.find_element(MobileBy.ID, 'search_input_text').send_keys('阿里巴巴')
        # xpath: https://www.w3schools.com/xml/xpath_syntax.asp
        # 点击搜索列表中的结果
        self.driver.find_element(MobileBy.XPATH, "//*[@text='阿里巴巴-SW' and contains(@resource-id, 'name')]").click()
        # 点击搜索到的结果
        self.driver.find_element(MobileBy.XPATH, "//*[@text='阿里巴巴-SW' and contains(@resource-id, 'stockName')]").click()
        # 断言股价大于200
        price = float(self.driver.find_element(MobileBy.XPATH, "//*[contains(@resource-id,'stock_current_price')]").get_attribute('text'))
        assert price > 200

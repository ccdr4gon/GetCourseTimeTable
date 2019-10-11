# encoding=utf-8
from selenium import webdriver
import unittest, time


class TestDemo(unittest.TestCase):


    def test_iPadChrome(self):
        options = webdriver.ChromeOptions()

        options.add_argument(
            '--user-agent=Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3')


        driver = webdriver.Chrome(executable_path="e:\\chromedriver", chrome_options=options)
        driver.get("http://www.baidu.com")
        # 暂停3秒，等待页面加载完成
        time.sleep(3)
        # 找到页面的搜索输入框，输入“iPad”
        driver.find_element_by_id("kw").send_keys("iPad")
        # 等待3秒，人工查看效果
        time.sleep(1)
        # 通过在Chrome浏览器地址栏中输入about:version，查看伪装效果
        driver.get("about:version")
        # 人工确认“用户代理”项配置信息是否跟设置一样
        time.sleep(10)
        driver.quit()


    def test_iPhoneChrome(self):
        options = webdriver.ChromeOptions()


        options.add_argument(
            '--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3')
        driver = webdriver.Chrome(executable_path="e:\\chromedriver", chrome_options=options)
        driver.get("http://www.baidu.com")
        time.sleep(3)
        # 找到搜索输入框，输入“iPhone”
        driver.find_element_by_id("index-kw").send_keys("iPhone")
        time.sleep(1)
        # 通过在Chrome浏览器地址栏中输入about:version，查看伪装效果
        driver.get("about:version")
        # 人工确认“用户代理”项配置信息是否跟设置一样
        time.sleep(10)
        driver.quit()


    def test_Android236Chrome(self):
        options = webdriver.ChromeOptions()


        options.add_argument(
            '--user-agent=Mozilla/5.0 (Linux; U; Android 2.3.6; en-us; Nexus S Build/GRK39F) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1')
        driver = webdriver.Chrome(executable_path="e:\\chromedriver", chrome_options=options)
        driver.get("http://www.baidu.com")
        time.sleep(3)
        # 找到搜索输入框，输入“Android 2.3.6”
        driver.find_element_by_id("index-kw").send_keys("Android 2.3.6")
        time.sleep(1)
        # 通过在Chrome浏览器地址栏中输入about:version，查看伪装效果
        driver.get("about:version")
        # 人工确认“用户代理”项配置信息是否跟设置一样
        time.sleep(10)
        driver.quit()


    def test_Android402Chrome(self):
        options = webdriver.ChromeOptions()


        options.add_argument(
            '--user-agent=Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30')
        driver = webdriver.Chrome(executable_path="e:\\chromedriver", chrome_options=options)
        driver.get("http://www.baidu.com")
        time.sleep(3)
        # 找到搜索输入框，输入“Android 4.0.2”
        driver.find_element_by_id("index-kw").send_keys("Android 4.0.2")
        time.sleep(1)
        # 通过在Chrome浏览器地址栏中输入about:version，查看伪装效果
        driver.get("about:version")
        # 人工确认“用户代理”项配置信息是否跟设置一样
        time.sleep(10)
        driver.quit()

if __name__ == '__main__':
    unittest.main()

#-*- coding=utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class Get_List:

    def __init__(self):
        self.first_day = "20190902" # 第一天是开学第一周的第一个星期一
        # 登录

        print("\n")
        print(
            """ 
             ██████╗ ██████╗██████╗ ██████╗  █████╗  ██████╗  ██████╗ ███╗   ██╗
            ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝ ██╔═══██╗████╗  ██║
            ██║     ██║     ██║  ██║██████╔╝███████║██║  ███╗██║   ██║██╔██╗ ██║
            ██║     ██║     ██║  ██║██╔══██╗██╔══██║██║   ██║██║   ██║██║╚██╗██║
            ╚██████╗╚██████╗██████╔╝██║  ██║██║  ██║╚██████╔╝╚██████╔╝██║ ╚████║
             ╚═════╝ ╚═════╝╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝
             """
        )  # ANSI shadow
    def get_page(self):
        fp = webdriver.FirefoxProfile()
        fp.set_preference("permissions.default.stylesheet", 2)
        driver = webdriver.Firefox()
        driver.get("http://portal.uestc.edu.cn")
        user_elem = driver.find_element_by_id("username")
        user=input("输入学号")
        user_elem.send_keys(user)
        passwd_elem = driver.find_element_by_id("password")
        passwd=input("输入密码")
        passwd_elem.send_keys(passwd)
        captcha_elem = driver.find_element_by_id("captchaResponse")
        captcha = input("输入看到的验证码:") # 看不清自己点一下换一个
        captcha_elem.send_keys(captcha)
        submit_elem = driver.find_element_by_class_name("auth_login_btn")
        submit_elem.click()
        driver.get("http://eams.uestc.edu.cn/eams/courseTableForStd.action")
        time.sleep(3)  # 等待重复登陆页面加载
        # 如果有重复登陆，踢掉
        print(driver.page_source)
        if "踢出" in driver.page_source:
            print(1111111111111)
            elem_rederict = driver.find_element_by_link_text("点击此处")
            elem_rederict.click()
            driver.implicitly_wait(2)
        # 获取课表
        # time.sleep(3)   #等待页面加载
        print(driver.page_source)
        a=driver.find_element_by_class_name("infoTitle")
        print(a)

if __name__ == '__main__':
    get=Get_List()
    get.get_page()



    ####### 垃圾Chrome会被检测，firefox不会，迷得很
    # option= webdriver.ChromeOptions()
    # option.add_experimental_option('excludeSwitches', ['enable-automation'])
    # option.add_argument('lang=zh_CN.UTF-8')
    # option.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"')
    # driver = webdriver.Chrome(options=option)


    #这个不行，垃圾教务系统写糊了，会500 driver.get("http://eams.uestc.edu.cn/eams/courseTableForStd!courseTable.action")
    # driver.get("http://eams.uestc.edu.cn/eams/home!submenus.action?menu.id=844")









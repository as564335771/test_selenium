import random
import time
# import sys
# sys.path.append('/Users/kely/PycharmProjects/test_selenium')

from selenium import webdriver

from base.find_element import FindElement


class RegisterFunction(object):
    def __init__(self,url,i):
        self.driver = self.get_driver(url,i)

    def get_driver(self,url,i):
        if i == 1:
            driver = webdriver.Chrome()
        elif i == 2:
            driver = webdriver.Firefox()
        else:
            driver = webdriver.Firefox()
        # driver = webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
        return driver

    #输入用户信息
    def send_user_info(self,key,data):
        self.get_user_element(key).send_keys(data)

    #定位用户信息，获取element
    def get_user_element(self,key):
        find_element = FindElement(self.driver)
        user_element = find_element.get_element(key)
        return user_element

    def get_range_user(self):
        user_info = ''.join(random.sample('123456qweasdzxc', 8))
        return user_info

    def main(self):
        user_name_info = self.get_range_user()
        user_email = user_name_info+'@126.com'
        self.send_user_info('user_name',user_email)
        self.send_user_info('password','123123')
        self.send_user_info('code','1234')
        self.get_user_element('register_button').click()
        code_error = self.get_user_element('register_error')
        print(code_error)
        if code_error == None:
            print('注册成功')
        else:
            self.driver.save_screenshot('/Users/kely/Documents/test_picture/code_error.png')
        time.sleep(5)
        self.driver.close()

if __name__ == '__main__':
    for i in range(3):
        register_function = RegisterFunction('https://cms.sumtoo.net/#/login',i)
        register_function.main()

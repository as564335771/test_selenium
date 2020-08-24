import random
import time

from selenium import webdriver

driver = webdriver.Chrome()

#浏览器初始化
def driver_init():
    driver.get("https://cms.sumtoo.net/#/login")
    driver.maximize_window()
    time.sleep(5)

#获取element信息
def get_element(xpath):
    element = driver.find_element_by_xpath(xpath)
    return element

#获取随机数
def get_range_user():
    user_info = ''.join(random.sample('123456qweasdzxc',8))
    return user_info

#运行主程序
def run_main():
    user_name_info =get_range_user()+'@163.com'
    driver_init()
    get_element('//*[@id="pane-first"]/form/div[1]/div/div/input').send_keys(user_name_info)
    get_element('//*[@id="pane-first"]/form/div[2]/div/div/input').send_keys(123456)
    get_element('//*[@id="pane-first"]/form/div[3]/div/div/input').send_keys(123456)
    get_element('//*[@id="pane-first"]/form/div[4]/button').click()
    time.sleep(6)
    driver.close()

run_main()


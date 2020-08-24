from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep

service = Service(r'/Users/kely/PycharmProjects/test_selenium/httprunnermanage/bin/msedgedriver')
service.start()
dr = webdriver.Remote(service.service_url)

dr.get('https://www.baidu.com/')

dr.find_element('id', 'kw').send_keys('博客园 韩志超')
dr.find_element('id', 'su').click()
sleep(3)

dr.quit()
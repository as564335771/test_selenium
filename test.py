import random
import time

from PIL import Image
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://cms.sumtoo.net/#/login")
time.sleep(5)

for i in range(5):
    user_name = ''.join(random.sample('1234567asdqwe',8)) + "@163.com"
    print(user_name)
driver.find_element_by_xpath('//*[@id="pane-first"]/form/div[1]/div/div/input').send_keys(user_name)
driver.find_element_by_xpath('//*[@id="pane-first"]/form/div[2]/div/div/input').send_keys("123456")
driver.find_element_by_xpath('//*[@id="pane-first"]/form/div[3]/div/div/input').send_keys("123456")
assert_picture = driver.find_element_by_class_name('getImgCode')
location = assert_picture.location  # 获取验证码x,y轴坐标
print(location)
driver.save_screenshot("/Users/kely/Documents/test_picture/imooc.png")
print(assert_picture.location)
# left = assert_picture.location['x']
# top = assert_picture.location['y']
# right = assert_picture.size['width']+left
# height = assert_picture.size['height']+top

size = assert_picture.size  # 获取验证码的长宽
rangle = (int(location['x']+110), int(location['y']+60), int(location['x'] + size['width']+165),
          int(location['y'] + size['height']+90))
print(rangle)
im = Image.open('/Users/kely/Documents/test_picture/imooc.png')
# print(right)
# print(height)
img = im.crop(rangle)
# img = im.crop((left,top,right,height))
# print(img)
img.save("/Users/kely/Documents/test_picture/imooc2.png")
driver.close()





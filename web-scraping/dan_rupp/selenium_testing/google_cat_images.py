import os
import time
import urllib
import urlparse
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

path_to_chromedriver = './chromedriver'
browser = webdriver.Chrome(executable_path=path_to_chromedriver)

browser.implicitly_wait(30)

time.sleep(2)

url = 'https://google.com/'
browser.get(url)

text_box = browser.find_element_by_id('lst-ib')

time.sleep(2)

for char in 'cats':
    text_box.send_keys(char)
    time.sleep(1)

text_box.send_keys(Keys.RETURN)

time.sleep(3)

images_link = browser.find_element_by_link_text('Images')
images_link.click()

time.sleep(3)

images = browser.find_elements_by_css_selector('#rg_s > div > a > img')

for i in range(0, 12):
    time.sleep(2)
    images[i].click()
    time.sleep(2)
    view_button = browser.find_element_by_link_text("View image")
    view_button.click()
    time.sleep(2)
    browser.switch_to_window(browser.window_handles[1])
    time.sleep(1)
    img_url = browser.current_url
    extension = os.path.splitext(urlparse.urlparse(img_url).path)[1]
    localpath = '{:02d}{}'.format(i, extension)
    urllib.urlretrieve(img_url, localpath)
    browser.close()
    browser.switch_to_window(browser.window_handles[0])


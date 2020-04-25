import sys
import io
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

#인프런 로그인 해보기

chrome_options = Options()


driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="d:/section3/webdriver/chrome/chromedriver")
driver.set_window_size(1920,1280)
driver.implicitly_wait(3)

driver.get('https://')
driver.save_screenshot("d:/section3/website1.png")

driver.implicitly_wait(5)

driver.get('https://www.daum.net')
driver.save_screenshot("d:/section3/website2.png")

driver.quit()

import sys
import io
from selenium import webdriver

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

driver = webdriver.Chrome(executable_path="d:/section3/webdriver/chrome/chromedriver")

driver.implicitly_wait(5)

driver.get('https://google.com')
driver.save_screenshot("d:/website1.png")

driver.implicitly_wait(5)

driver.get('https://www.daum.net')
driver.save_screenshot("d:/website2.png")

driver.quit()

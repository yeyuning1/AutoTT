import time
from appium import webdriver
from Appium_learning import app_settings

driver = webdriver.Remote('http://localhost:4723/wd/hub', app_settings.desired_caps)
time.sleep(5)
driver.quit()

import time
from appium import webdriver

from Appium_learning import app_settings

driver = webdriver.Remote('http://localhost:4723/wd/hub', app_settings.desired_caps)
print(driver.current_package)
print(driver.current_activity)
print(driver.context)
time.sleep(5)
# adb shell dumpsys window windows | findstr(grep) mFocusedApp
driver.start_activity('com.android.messaging', '.ui.conversationlist.ConversationListActivity')
print(driver.current_package)
print(driver.current_activity)
print(driver.context)
time.sleep(5)
# driver.quit() 销毁 driver 驱动对象  --> stop_client
driver.close_app()

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
# 打开指定url网页
driver.get('http://yeyuning.cn')
# 选择元素
# <input type="text" name="passwd" id="passwd-id" />
element = driver.find_element_by_id("passwd-id")
element = driver.find_element_by_name("passwd")
element = driver.find_element_by_xpath("//input[@id='passwd-id']")
# 输入内容
element.send_keys("some text")
# 输入方向键
element.send_keys(" and some", Keys.ARROW_DOWN)
# 清除文本框内容
element.clear()
# 填写表格
element = driver.find_element_by_xpath("//select[@name='name']")
all_options = element.find_elements_by_tag_name("option")
for option in all_options:
    print("Value is: %s" % option.get_attribute("value"))
    option.click()
# Select 类
from selenium.webdriver.support.ui import Select

index, value = None, None
select = Select(driver.find_element_by_name('name'))
select.select_by_index(index)
select.select_by_visible_text("text")
select.select_by_value(value)
# 取消选中
select = Select(driver.find_element_by_id('id'))
select.deselect_all()
# 列出所有选项
select = Select(driver.find_element_by_xpath("xpath"))
all_selected_options = select.all_selected_options  # type:list
options = select.options  # type:list
# 提交表单
driver.find_element_by_id("submit").click()
element.submit()
# 拖放
element = driver.find_element_by_name("source")
target = driver.find_element_by_name("target")

from selenium.webdriver import ActionChains
action_chains = ActionChains(driver)
action_chains.drag_and_drop(element, target).perform()
# 再不同窗口和框架之间移动
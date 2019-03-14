# coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(executable_path='D:\\WYJ\\QD\\chromedriver.exe')
driver.get("http://www.baidu.com")

# driver.find_element_by_class_name("s_ipt").send_keys("selenium")
above = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/a[8]")
right_click = driver.find_element_by_id("kw")
ActionChains(driver).context_click(right_click).perform()
time.sleep(2)
ActionChains(driver).move_to_element(above).perform()
time.sleep(3)
# driver.find_element_by_class_name("s_ipt").clear()
# driver.find_element_by_class_name("s_ipt").send_keys("WebDriver")
# driver.find_element_by_id("su").click()
# driver.find_element_by_partial_link_text("selenium用法详解").click()
# CSS定位使用id属性
# driver.find_element_by_css_selector("#su").click()
# 设置浏览器大小
driver.set_window_size(400, 600)
time.sleep(2)
# 设置浏览器全屏
driver.maximize_window()
time.sleep(3)
# 刷新页面
driver.refresh()
time.sleep(4)

driver.quit()

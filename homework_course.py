#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)
button = browser.find_element_by_id("book")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "10000"))
button.click()
x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = str(math.log(abs(12*math.sin(int(x)))))
browser.find_element_by_id("answer").send_keys(y)
browser.find_element_by_id("solve").click()


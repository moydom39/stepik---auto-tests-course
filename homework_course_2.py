#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math
from selenium import webdriver
link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)
browser.find_element_by_css_selector(".trollface.btn").click()
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)
x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = str(math.log(abs(12*math.sin(int(x)))))
browser.find_element_by_id("answer").send_keys(y)
browser.find_element_by_css_selector(".btn").click()


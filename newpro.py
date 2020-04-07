import os
from selenium import webdriver
import time

from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


binary = FirefoxBinary('path/to/binary')



os.system("echo hello manthila")
projectName = input("Enter project name : ")




driver = webdriver.Firefox()
driver.get("https://github.com/login")
driver.find_element_by_id("login_field").send_keys("manthila1997")
driver.find_element_by_id("password").send_keys("manthila@1A")
driver.find_element_by_name("commit").click()

driver.find_element_by_xpath("/html/body/div[4]/div/aside[1]/div[2]/div[1]/div/h2/a").click()
driver.find_element_by_id("repository_name").send_keys(projectName)

time.sleep(5)
driver.find_element_by_id("repository_auto_init").click()



driver.find_element_by_css_selector('button.first-in-line').click()
#driver.find_element_by_xpath("/html/body/div[4]/div/main/div[3]/div/div[3]/span/details/summary").click()




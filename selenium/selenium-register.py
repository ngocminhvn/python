# pip install selenium
# https://chromedriver.chromium.org/downloads

import string
import random
from logging import error
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

x = 1
while (x < 1000) :
	letters = string.ascii_lowercase
	rd = ''.join(random.choice(letters) for i in range(15))
	username = rd
	password = rd
	email = str(rd) + "@gmail.com"

	driver = webdriver.Chrome(r"chromedriver.exe")
	driver.get("https://trieusub.vn/register")
	driver.find_element_by_id("username").send_keys(username)
	driver.find_element_by_id("password").send_keys(password)
	driver.find_element_by_id("repassword").send_keys(password)
	driver.find_element_by_id("email").send_keys(email)
	driver.find_element_by_name("submit").click()
	x = x + 1;
#driver.close()
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from pprint import pprint


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

# driver.get("https://www.google.com/")
#
# my_cookies = driver.get_cookies()
# print(my_cookies)
# print("="*200)
# #adding cookies
# cookie = {"name": "cookiename", "value": "cookievalue"}
# driver.add_cookie(cookie)
# my_cookies = driver.get_cookies()
# print(my_cookies)
# print("="*200)
# #deleting cookies
# driver.delete_cookie("cookiename")
# my_cookies = driver.get_cookies()
# print(my_cookies)
# print("="*200)
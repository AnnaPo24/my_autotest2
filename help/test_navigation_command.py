import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
"""Хотел использовать яндекс, но там капча постоянно появляется"""
# driver.get("https://ya.ru/")
# driver.get("https://www.google.com/")
# time.sleep(1)
# print(driver.title)
# search_box = driver.find_element(By.CSS_SELECTOR, "input[class^='search3']")
# search_box = driver.find_element(By.CSS_SELECTOR, "textarea[name='q']")
# search_box.send_keys("Pytest")
# search_box.send_keys(Keys.ENTER)
# print(driver.title)
# time.sleep(1)
# driver.back()
# time.sleep(1)
# print(driver.title)
# driver.forward()
# time.sleep(1)
# print(driver.title)
# time.sleep(1)
# driver.refresh()
# time.sleep(2)
# driver.quit()
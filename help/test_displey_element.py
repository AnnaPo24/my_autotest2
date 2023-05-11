import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

# driver.get("https://demoqa.com/dynamic-properties")
# will_enable_button = driver.find_element(By.CSS_SELECTOR, "button[id='enableAfter']")
# print(will_enable_button.is_displayed())
# print(will_enable_button.is_enabled())
# print(will_enable_button.is_selected())
# time.sleep(5)
# print(will_enable_button.is_enabled())
# driver.quit()

# driver.get("https://the-internet.herokuapp.com/checkboxes")
# first_checkbox = driver.find_element(By.XPATH, "//form[@id='checkboxes']/input[1]")
# second_checkbox = driver.find_element(By.XPATH, "//form[@id='checkboxes']/input[2]")
# print(first_checkbox.is_selected())
# print(second_checkbox.is_selected())
# driver.quit()

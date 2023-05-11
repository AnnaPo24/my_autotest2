import time
from pprint import pprint
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

link = "https://demoqa.com"
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# driver.maximize_window()
# driver.fullscreen_window()
# driver.set_window_size(320, 1000)
# driver.set_window_rect(x=100, y=100, width=1000, height=400)

driver.get(link)
time.sleep(5)
# print(driver.title)
# print(driver.current_url)
# pprint(driver.page_source)
# driver.quit()
driver.close()

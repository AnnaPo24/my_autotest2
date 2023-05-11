import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

link = {"google": "https://www.google.com/",
        "demoqa_text-box": "https://demoqa.com/text-box",
        "demoqa_links": "https://demoqa.com/links",
        "demoqa_dynamic-properties": "https://demoqa.com/dynamic-properties",
        "demoqa_resizable": "https://demoqa.com/resizable"}


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
"""Поиск в google"""
# driver.get(link["google"])
# search_box_google = driver.find_element(By.CSS_SELECTOR, "textarea[name='q']")
# search_box_google = driver.find_element(By.XPATH, "//textarea[@name='q']")
# search_box_google.send_keys("Python")
# time.sleep(3)
# search_box_google.submit()
# search_box_google.send_keys(Keys.ENTER)
# time.sleep(3)
# driver.quit()
"""Заполнение формы в demoqa"""
# driver.get(link["demoqa_text-box"])

# time.sleep(3)
# input_full_name = driver.find_element(By.ID, "userName")
# input_full_name.send_keys("Denis Denisov")
# time.sleep(3)
# driver.quit()
"""Получение атрибута"""
# driver.get(link["demoqa_text-box"])
#
# time.sleep(1)
# input_full_name = driver.find_element(By.ID, "userName")
# attribute_full_name_field = input_full_name.get_attribute('placeholder')
#
# input_permanent_address_field = driver.find_element(By.CSS_SELECTOR, "textarea[id='permanentAddress']")
# input_permanent_address_field.get_attribute('placeholder')
#
# print(attribute_full_name_field, len(attribute_full_name_field))
# print(input_permanent_address_field, len(input_permanent_address_field))
# time.sleep(3)
# driver.quit()
"""Удаление атрибута"""
# driver.get(link["demoqa_links"])
# time.sleep(2)
# links = driver.find_element(By.CSS_SELECTOR, "a[id='simpleLink']")
# driver.execute_script("arguments[0].removeAttribute('target')", links)
# links.click()
# # получаем список всех открытых вкладок
# windows_pages = driver.window_handles
# print(windows_pages)
# # переходим на вторую вкладку (индекс 1)
# driver.switch_to.window(driver.window_handles[1])
# time.sleep(3)
# driver.quit()
"""Получение css-свойств элемента"""
# driver.get(link["demoqa_dynamic-properties"])
#
# time.sleep(1)
# button = driver.find_element(By.CSS_SELECTOR, "button[id='colorChange']")
# style_before = button.value_of_css_property('color')
# time.sleep(5)
# style_after = button.value_of_css_property('color')
# style_after_background_color = button.value_of_css_property('background-color')
# time.sleep(1)
# print(style_before)
# print(style_after)
# print(style_after_background_color)
# driver.quit()
"""Использование проперти"""
# driver.get(link["demoqa_resizable"])
#
# time.sleep(1)
# elem = driver.find_element(By.CSS_SELECTOR, "div[id='resizableBoxWithRestriction']")
# style = elem.value_of_css_property('background-color')
# width = elem.get_property('offsetWidth')
# height = elem.get_property('offsetHeight')
# print(f"Style: {style}")
# print(f"Ширина элемента: {width}")
# print(f"Высота элемента: {height}")
# time.sleep(1)
# driver.quit()

# driver.get(link["demoqa_links"])
#
# time.sleep(1)
# img = driver.find_element(By.XPATH, "//img[@src='/images/Toolsqa.jpg']")
# text_img = img.text
# value_img = img.get_property("src")
# print(text_img)
# print(value_img)
# print('='*50)
# elem_header = driver.find_element(By.CSS_SELECTOR, "div[id='linkWrapper'] h5")
# text = elem_header.text
# value = elem_header.get_property("textContent")
# print(text)
# print(value)
# print('='*50)
# url = driver.find_element(By.CSS_SELECTOR, "a[id='simpleLink']")
# attribute_url = url.get_attribute("href")
# text_url = url.text
# value_text = url.get_property("href")
# print(text_url)
# print(value_text)
# print(attribute_url)
# print('='*50)
# time.sleep(1)
# driver.quit()


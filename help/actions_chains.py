import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
"""List"""
# driver.get("https://demoqa.com/selectable")
# all_elem = driver.find_elements(By.XPATH, "//ul[@id='verticalListContainer']/li")
# for i in all_elem:
#     print(i.text)
#     time.sleep(1)
#     i.click()
# time.sleep(2)
# first = driver.find_element(By.XPATH, "//ul[@id='verticalListContainer']/li[1]")
# second = driver.find_element(By.XPATH, "//ul[@id='verticalListContainer']/li[2]")
# actions = ActionChains(driver)
# actions.click(first)
# actions.click(second)
# actions.perform()
# time.sleep(2)
# driver.quit()
"""Grid - показать на занятии"""
"""Some code"""

"""Right and double click"""
# driver.get("https://demoqa.com/buttons")
# double_click = driver.find_element(By.CSS_SELECTOR, "button[id='doubleClickBtn']")
# right_click = driver.find_element(By.CSS_SELECTOR, "button[id='rightClickBtn']")
# actions = ActionChains(driver)
# actions.double_click(double_click)
# actions.perform()
# time.sleep(1)
# text_double_click = driver.find_element(By.CSS_SELECTOR, "p[id='doubleClickMessage']")
# print(text_double_click.text)
# time.sleep(5)
# actions.context_click(right_click)
# actions.perform()
# time.sleep(1)
# text_right_click = driver.find_element(By.CSS_SELECTOR, "p[id='rightClickMessage']")
# print(text_right_click.text)
# time.sleep(5)
# driver.quit()

"""Key up and key down"""
# driver.get("https://the-internet.herokuapp.com/key_presses")
# actions = ActionChains(driver)
# elem = driver.find_element(By.XPATH, "//div[@class='example']/p[1]")
#
# time.sleep(1)
# actions.double_click(elem)
# # actions.key_down(Keys.SHIFT).click(text_elem).move_by_offset(100, 0).key_up(Keys.SHIFT).perform()
# time.sleep(1)
# actions.click(elem).key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
# input_field = driver.find_element(By.CSS_SELECTOR, "input[id='target']")
#
# time.sleep(5)
# print()
"""drag_and_drop_by_offset(self, source, xoffset, yoffset):
        Holds down the left mouse button on the source element, then moves
        to the target offset and releases the mouse button.

        :Args:
         - source: The element to mouse down.
         - xoffset: X offset to move to.
         - yoffset: Y offset to move to."""

# driver.get("https://demoqa.com/slider")
# value = driver.find_element(By.CSS_SELECTOR, "input[id='sliderValue']")
# slider = driver.find_element(By.CSS_SELECTOR, "input[class^='range-slider']")
# actions = ActionChains(driver)
# before = value.get_attribute('value')
# actions.drag_and_drop_by_offset(slider, 200, 0).perform()
# time.sleep(5)
# after = value.get_attribute('value')
# print(before)
# print(after)
# driver.get("https://demoqa.com/resizable")
# resizable_box = driver.find_element(By.CSS_SELECTOR, "div[id='resizableBoxWithRestriction']")
# resizable_box_handle = driver.find_element(By.CSS_SELECTOR, "div[id='resizableBoxWithRestriction'] span")
# before = resizable_box.get_attribute('style')
# actions = ActionChains(driver)
# actions.drag_and_drop_by_offset(resizable_box_handle, 100, 50).perform()
# after = resizable_box.get_attribute('style')
# time.sleep(3)
# print(before)
# print(after)
"""move_to_element(self, to_element):
        Moving the mouse to the middle of an element.
        :Args:
         - to_element: The WebElement to move to.
        """
# driver.get("https://demoqa.com/tool-tips")
# button = driver.find_element(By.CSS_SELECTOR, "button[id='toolTipButton']")
# actions = ActionChains(driver)
# actions.move_to_element(button).perform()
# time.sleep(2)
# after_hover = driver.find_element(By.CSS_SELECTOR, "div[class='tooltip-inner']")
# print(after_hover.text)

"""drag_and_drop(self, source, target):
        Holds down the left mouse button on the source element, then moves
        to the target element and releases the mouse button.
        :Args:
         - source: The element to mouse down.
         - target: The element to mouse up.
        """
# driver.get("https://demoqa.com/sortable")
# what = driver.find_element(By.CSS_SELECTOR, "div[class^='vertical'] > div:nth-child(2)")
# where = driver.find_element(By.CSS_SELECTOR, "div[class^='vertical'] > div:nth-child(5)")
# actions = ActionChains(driver)
# actions.drag_and_drop(what, where).perform()
# time.sleep(3)

"""click_and_hold(self, on_element=None):
        Holds down the left mouse button on an element.
        :Args:
         - on_element: The element to mouse down.
           If None, clicks on current mouse position.

release(self, on_element=None):
        Releasing a held mouse button on an element.
        :Args:
         - on_element: The element to mouse up.
           If None, releases on current mouse position."""

# driver.get("https://demoqa.com/sortable")
# what = driver.find_element(By.CSS_SELECTOR, "div[class^='vertical'] > div:nth-child(2)")
# where = driver.find_element(By.CSS_SELECTOR, "div[class^='vertical'] > div:nth-child(5)")
# actions = ActionChains(driver)
# actions.click_and_hold(what)
# actions.release(where)
# actions.perform()
# time.sleep(3)

"""scroll_to_element(self, element: WebElement):
        If the element is outside the viewport, scrolls the bottom of the
        element to the bottom of the viewport.
        :Args:
         - element: Which element to scroll into the viewport.
        """
# driver.get("https://the-internet.herokuapp.com/")
# elem = driver.find_element(By.CSS_SELECTOR, "div[id='content'] > ul > li:nth-child(40)")
# time.sleep(1)
# actions = ActionChains(driver)
# actions.scroll_to_element(elem).perform()
# text = elem.get_property('textContent')
# time.sleep(3)
# print(text)

driver.quit()
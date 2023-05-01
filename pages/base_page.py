from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver import ActionChains

@allure.suite("BasePage")
class BasePage:     #сновной класс от которого будут наследовать все остальные

    def __init__(self, driver, url): #основной конструктор откуда мы получаем драйвер,который у нас придёт из теста и url
        self.driver = driver
        self.url = url

    @allure.title("open")
    def open(self):
        self.driver.get(self.url)

    @allure.title("element is visible")
    def element_is_visible(self, locator, timeout=5):
        self.go_to_element(self.element_is_present(locator))
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.title("elements are visible")
    def elements_are_visible(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    @allure.title("element is present")
    def element_is_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    @allure.title("elements are visible")
    def elements_are_present(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    @allure.title("element is not visible")
    def element_is_not_visible(self, locator, timeout=5):                #редко используется
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    @allure.title("element is clicable")
    def element_is_clicable(self, locator, timeout=5):
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    @allure.title("go to element ")
    def go_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Remove footer')
    def remove_footer(self):
        self.driver.execute_script("document.querySelector('footer')[0].remove();")

    @allure.step("Double click")
    def action_double_click(self, elem):
        action = ActionChains(self.driver)  #из библиотеки загрузили класс,прописали сверху
        action.double_click(elem)        # получаем метод класса double_click
        action.perform()                    #без этой штуки не заведётся

    @allure.step("Right click")
    def action_right_click(self, elem):
        action = ActionChains(self.driver)  
        action.context_click(elem)          #из библиотеки инфа
        action.perform()



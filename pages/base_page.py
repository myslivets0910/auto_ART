# сюда прописываем функции которые будут использоваться на протяжении всех тестов и на все страницах (только меняться селекторы и условия)

from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=5): # чтобы был виден конкретный элемент
        return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5): # чтобы был видно несколько элементов
        return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def element_is_present(self, locator, timeout=5): # позволяет эелементы в DOM-дереве сайта (есть на сайте, но не в видимости экрана)
        return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def elements_are_presents(self, locator, timeout=5): # позволяет эелементы в DOM-дереве сайта (есть на сайте, но не в видимости экрана)
        return wait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))

    def elements_is_not_visible(self, locator, timeout=5): # позволяет использовать не видимые елементы
        return wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def elements_is_clickeble(self, locator, timeout=5): # чтобы элемент стал кликабельным
        return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def go_to_element(self, element): # помогает перемещать к нужному элементу
        self.driver.execute_script("argument[0].ScrollIntoView;", element)



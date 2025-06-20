# прописываем элементы, которые будем проверять

import time

from locators.elements_page_locators import TextBoxPageLocators
from pages.base_page import BasePage
from generator.generator import generated_person


class TextBoxPage(BasePage): # класс где буду работа с полями в https://demoqa.com/text-box
    locators = TextBoxPageLocators()

    def fill_all_fields(self): # заполните ве поля
        person_info = next(generated_person()) #указываем что только по одному разу берем такие данные
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address

        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        submit_element = self.element_is_visible(self.locators.SUBMIT) # назвали элемента до которого на до прокруть
        self.driver.execute_script("arguments[0].scrollIntoView();", submit_element) # указали до какого элемента надо прокрутить
        self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address


    def check_filled_form(self): # проверить результат заполненных полей
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address



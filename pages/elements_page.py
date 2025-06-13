# прописываем элементы, которые будем проверять
import random
import time

from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators
from pages.base_page import BasePage
from generator.generator import generated_person


class TextBoxPage(BasePage):  # класс где буду работа с полями в https://demoqa.com/text-box
    locators = TextBoxPageLocators()

    def fill_all_fields(self):  # заполните ве поля
        person_info = next(generated_person())  # указываем что только по одному разу берем такие данные
        full_name = person_info.full_name
        email = person_info.email
        current_address = person_info.current_address
        permanent_address = person_info.permanent_address

        self.element_is_visible(self.locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(self.locators.EMAIL).send_keys(email)
        self.element_is_visible(self.locators.CURRENT_ADDRESS).send_keys(current_address)
        self.element_is_visible(self.locators.PERMANENT_ADDRESS).send_keys(permanent_address)
        submit_element = self.element_is_visible(self.locators.SUBMIT)  # назвали элемента до которого на до прокруть
        self.driver.execute_script("arguments[0].scrollIntoView();",
                                   submit_element)  # указали до какого элемента надо прокрутить
        self.element_is_visible(self.locators.SUBMIT).click()
        return full_name, email, current_address, permanent_address

    def check_filled_form(self):  # проверить результат заполненных полей
        full_name = self.element_is_present(self.locators.CREATED_FULL_NAME).text.split(':')[1]
        email = self.element_is_present(self.locators.CREATED_EMAIL).text.split(':')[1]
        current_address = self.element_is_present(self.locators.CREATED_CURRENT_ADDRESS).text.split(':')[1]
        permanent_address = self.element_is_present(self.locators.CREATED_PERMANENT_ADDRESS).text.split(':')[1]
        return full_name, email, current_address, permanent_address


class CheckBoxPage(BasePage): # класс с функциями для проверки чекбоксов
    locators = CheckBoxPageLocators()

    def open_full_list(self):  # функция по раскрытию всего списка
        self.element_is_visible(self.locators.EXPAND_ALL_BUTTON).click()  # клик на + чтобы раскрыть список

    def click_random_checkbox(self):  # рандомные клики из списка (чтобы не песцитидеть)
        item_list = self.elements_are_visible(self.locators.ITEM_LIST)
        count = 21
        while count != 0:
            item = item_list[random.randint(2, 12)]
            if count > 0:
                self.driver.execute_script("arguments[0].scrollIntoView();", item)
                item.click()
                print(item)
                count = -1
            else:
                break

    def get_checked_checkboxes(self): #функция которая вытаскивае title чекбоксов
        checked_list = self.elements_are_presents(self.locators.CHECKED_ITEMS)
        data = []
        for box in checked_list:
            title_item = box.find_element(*self.locators.TITLE_ITEM)
            data.append(title_item.text)
        return str(data).replace(' ', '').replace('doc', '').replace('.', '').lower()
    # преобразовываем запись в понятный ви для сравнения(файл debug)

    def get_output_result(self): #функция которая показывает чекбоксы которые выделены в результате
        result_list = self.elements_are_presents(self.locators.OUTPUT_RESULT)
        data = []
        for item in result_list:
            data.append(item.text)
        return str(data).replace(' ', '').lower()
    # преобразовываем запись в понятный вид для сравнения(файл debug)

class RadioButtonPage(BasePage): # класс с функциями для проверки радиокнопок
    locators = RadioButtonPageLocators()

    def click_on_the_radio_button(self, choice): # функция со списком для клика по нашим чекбоксам
        choices = {'yes': self.locators.YES_RADIOBUTTON,
                'impressive':self.locators.IMPRESSIVE_RADIOBUTTON,
                'no':self.locators.NO_RADIBUTTON}
        self.element_is_visible(choices[choice]).click()

    def get_output_result_button(self): # функция с результатом после клика по нашим чекбоксам
        return self.element_is_present(self.locators.OUTPUT_RESULT_BUTTON).text






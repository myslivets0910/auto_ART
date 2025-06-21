# прописываем элементы, которые будем проверять
import base64
import os
import random
import time

import requests
from selenium.webdriver.common.by import By

from locators.elements_page_locators import TextBoxPageLocators, CheckBoxPageLocators, RadioButtonPageLocators, \
    WebTablePageLocators, ButtonsPageLocators, LinksPageLocators, UploadDownloadPageLocators, \
    DynamicPropertiesPageLocators
from pages.base_page import BasePage
from generator.generator import generated_person, generated_file


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

class WebTablePage(BasePage):
    #класс на создание / проверку / удаление данных из таблицы
    locators = WebTablePageLocators()

    def add_new_person(self): # функция на создание новой персоны. Используем рандомные данные.
        count = 1
        while count != 0:
            person_info = next(generated_person())
            firstname = person_info.firstname
            lastname = person_info.lastname
            email = person_info.email
            age = person_info.age
            salary = person_info.salary
            department = person_info.department
            self.element_is_visible(self.locators.ADD_BUTTON_PERSON_WEBTABLE).click()
            self.element_is_visible(self.locators.FIRST_NAME_INPUT_WEBTABLE).send_keys(firstname)
            self.element_is_visible(self.locators.LAST_NAME_INPUT_WEBTABLE).send_keys(lastname)
            self.element_is_visible(self.locators.EMAIL_INPUT_WEBTABLE).send_keys(email)
            self.element_is_visible(self.locators.AGE_INPUT_WEBTABLE).send_keys(age)
            self.element_is_visible(self.locators.SALARY_INPUT_WEBTABLE).send_keys(salary)
            self.element_is_visible(self.locators.DEPARTMENT_INPUT_WEBTABLE).send_keys(department)
            self.element_is_visible(self.locators.SUBMIT_ADD_FORM_PERSON_WEBTABLE).click()
            count -=1
            return [firstname, lastname, str(age), email, str(salary),department]

    def check_new_person_web_table(self): # функция на проверку созданной персоны в таблице. (преобразование данных)
        person_list = self.elements_are_presents(self.locators.FULL_PEOPLE_LIST)
        data = []
        for item in person_list:
            data.append(item.text.splitlines())
        return data

    def search_for_a_person_in_web_table(self,key_word): # поиск персоны в таблице
        self.element_is_visible(self.locators.SEARCH_TABLE).send_keys(key_word)

    def check_search_person_in_web_table(self): # проверка, на то что данная запись есть в таблице
        delete_button = self.element_is_present(self.locators.DELETE_BUTTON_PERSON)
        row = delete_button.find_element(self.locators.ROW_PARENT_SEARCH_TABLE)
        return row.text.splitlines()

    def update_person_info(self):
        # функция изменяет данные персоны (возраст) == надо откорректировать по всем полям
        person_info = next(generated_person())
        age = person_info.age
        self.element_is_visible(self.locators.UPDATE_BUTTON_PERSON).click()
        self.element_is_visible(self.locators.AGE_INPUT_WEBTABLE).clear()
        self.element_is_visible(self.locators.AGE_INPUT_WEBTABLE).send_keys(age)
        self.element_is_visible(self.locators.SUBMIT_ADD_FORM_PERSON_WEBTABLE).click()
        return str(age)

    def delete_person(self): # функция удаления персоны
        self.element_is_visible(self.locators.DELETE_BUTTON_PERSON).click()

    def check_deleted(self): # функция определения локатора который указывает на отсутствие данных в таблице
        return self.element_is_present(self.locators.NO_ROWS_FOUND).text

    def select_up_to_some_row(self):
        # функция по смене значение (селекта у строк)
        count = [5, 10, 20, 25, 50, 100]
        data = []
        for x in count:
            count_row_button = self.element_is_visible(self.locators.CHANGE_THE_LINES_PAGE)
            self.driver.execute_script("arguments[0].scrollIntoView();", count_row_button)
            count_row_button.click()
            self.element_is_visible((By.CSS_SELECTOR,f'option[value = "{x}"]')).click()
            data.append(self.check_count_rows())
        return data

    def check_count_rows(self):
        # функция возвращает кол-во строк в табблице
        list_table = self.elements_are_presents(self.locators.FULL_PEOPLE_LIST)
        return len(list_table)


class ButtonsPage(BasePage):
    locators = ButtonsPageLocators()

    def click_on_different_button(self, type_click): # функция в которой прожимаются все кнопка
        # данные методы можно рефачить на каждую кнопку по отдельности + тест на каждую кнопку
        if type_click == "double":
            self.action_double_click(self.element_is_visible(self.locators.DOUBLE_CLICK_ME_BUTTON))
            return self.check_clicked_button_result(self.locators.DOUBLE_CLICK_ME_RESULT)

        if type_click == "right":
            self.action_right_click(self.element_is_visible(self.locators.RIHGHT_CLICK_ME_BUTTON))
            return self.check_clicked_button_result(self.locators.RIHGHT_CLICK_ME_RESULT)

        if type_click == "click":
            self.element_is_visible(self.locators.CLICK_ME_BUTTON).click()
            return self.check_clicked_button_result(self.locators.CLICK_ME_RESULT)


    def check_clicked_button_result(self, element): # функция на определение результата при нажатии на кнопку на странице кнопок .
        return self.element_is_present(element).text


class LinksPage(BasePage):
    locators = LinksPageLocators()

    def check_new_tab_simple_link(self):
        # функция на проверку по перехлоду на активные ссылок
        simple_link = self.element_is_present(self.locators.SIMPLE_LINK_HOME)
        link_href = simple_link.get_attribute('href')
        request = requests.get(link_href)
        if request.status_code == 200:
            simple_link.click()
            self.driver.switch_to.window(self.driver.window_handles[1])
            url = self.driver.current_url
            return link_href, url
        else:
            return request.status_code, link_href

    def check_broken_link(self,url):
        # функция на проверку неактивных ссылок
        request = requests.get(url)
        if request.status_code == 200:
            self.element_is_present(self.locators.BAD_REQUEST_LINK).click()
        else:
            return request.status_code


class UploadDownloadPage(BasePage):
    locators = UploadDownloadPageLocators()


    def upload_file(self):
        # создаем и возращаем знначение загруженного файла (проверка что файл загрузился)
        file_name , path = generated_file()
        self.element_is_present(self.locators.INPUT_UPLOAD_FILE).send_keys(path)
        os.remove(path) # очистка созданного/скачаного файла
        text_uploaded = self.element_is_present(self.locators.UPLOADED_RESULT).text
        # print(file_name)
        # print(text_uploaded)
        return file_name.split('\\')[-1], text_uploaded.split('\\')[-1]

    def download_file(self):
        link_href = self.element_is_present(self.locators.BUTTON_DOWNLOAD).get_attribute('href')
        # print(link_href)
        link_b = base64.b64decode(link_href)
        path_name_file = rf'C:\Users\kabac\PycharmProjects\auto_ART\filetest{random.randint(0,999)}.jpg'
        with open(path_name_file, 'wb+') as f:
            offset = link_b.find(b'\xff\xd8')
            f.write(link_b[offset:])
            check_file = os.path.exists(path_name_file)
            f.close()
        os.remove(path_name_file) # очистка созданного/скачаного файла
        return check_file


class TimeoutExcepcion:
    pass


class DynamicPropertiesPage(BasePage):
    locators = DynamicPropertiesPageLocators()

    def check_enable_button(self):
        try:
            self.elements_is_clickeble(self.locators.WILL_ENABLE_5_SECONDS)
        except TimeoutExcepcion:
            return False
        return True

    def check_changed_of_color(self):
        color_button = self.element_is_present(self.locators.COLOR_CHANGE_BUTTON)
        color_button_defore = color_button.value_of_css_property('color')
        time.sleep(5)
        color_button_after = color_button.value_of_css_property('color')
        # print(color_button_defore , color_button_after)
        return color_button_defore , color_button_after

    def check_appear_of_button(self):
        try:
            self.element_is_visible(self.locators.VISIBLE_AFTER_5_SECONDS,)
        except TimeoutExcepcion:
            return False
        return True

















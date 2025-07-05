import base64
import os
import random
import time


import requests
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from generator.generator import generated_color, generated_date
from locators.widgets_locators import AccordianPageLocators, AutoCompletePageLocators, DatePickerPageLocators
from pages.base_page import BasePage


class AccordianPage(BasePage):
    locators = AccordianPageLocators()
    def check_accordian(self, accordian_num):
        # метод для поиска title и content
        # создаем словарь для поиска
        accordian = {'first':
                         {'title': self.locators.SECTION_1,
                          'content': self.locators.SECTION_1_TEXT},
                     'second':
                         {'title': self.locators.SECTION_2,
                          'content': self.locators.SECTION_2_TEXT},
                     'third':
                         {'title': self.locators.SECTION_3,
                          'content': self.locators.SECTION_3_TEXT},
                     }

        section_title = self.element_is_visible(accordian[accordian_num]['title'])
        self.driver.execute_script("arguments[0].scrollIntoView();", section_title) # скролим, чтобы каждый элемент title был в поле зрения
        section_title.click()

        try:
            section_content = self.element_is_visible(accordian[accordian_num]['content']).text
        except TimeoutException:
            section_title.click()
            section_content = self.element_is_visible(accordian[accordian_num]['content']).text

        #print(section_title.text)
        #print(section_content)
        return [section_title.text, len(section_content)] , 'сообщение об ошибке'

class AutoCompletePage(BasePage):

    locators = AutoCompletePageLocators()
    def fill_input_multi(self):
        # метод которые выбирает цвета в селект
        colors = random.sample(next(generated_color()).color_name, k=random.randint(2,5))
        for color in colors:
            input_multi = self.elements_is_clickeble(self.locators.MULTI_COMPLETE_INPUT)
            input_multi.send_keys(color)
            input_multi.send_keys(Keys.ENTER)
        return colors

    def remove_value_from_multi(self):
        # метод которые удаляет цвета и сравнивает значения после удаления
        count_value_before = len(self.elements_are_visible(self.locators.MULTI_COMPLETE_VALUE))
        remove_button_list = self.elements_are_visible(self.locators.MULTI_COMPLETE_REMOVE)
        for value in remove_button_list:
            value.click()
            break
        count_value_after = len(self.elements_are_presents(self.locators.MULTI_COMPLETE_VALUE))

        return count_value_before, count_value_after

    def check_color_in_multi(self):
        # метод который сравнивает введенные значения с результатом
        color_list = self.elements_are_presents(self.locators.MULTI_COMPLETE_VALUE)
        colors = []
        for color in color_list:
            colors.append(color.text)
        return colors

    def fill_input_single(self):
        # метод которые выбирает цвета в селект
        color = random.sample(next(generated_color()).color_name, k=1)
        input_single = self.elements_is_clickeble(self.locators.SINGLE_COMPLETE_INPUT)
        input_single.click()
        input_single.send_keys(color)
        input_single.send_keys(Keys.ENTER)
        return color[0]

    def check_color_in_single(self):
        # метод который показывает какой сделан выбор
        color = self.element_is_visible(self.locators.SINGLE_COMPLETE_VALUE)
        return color.text



class DatePickerPage(BasePage):
    locators = DatePickerPageLocators()
    def select_date(self):
        # метод на выбор и смену даты в датапикере (без времени)
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.set_date_by_text(self.locators.DATE_SELECT_MONTH, date.month)
        self.set_date_by_text(self.locators.DATE_SELECT_YEAR, date.year)
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        value_date_after = input_date.get_attribute('value')
        return value_date_before, value_date_after


    def select_date_and_time(self):
        # # метод на выбор и смену даты и времени в датапикере
        date = next(generated_date())
        input_date = self.element_is_visible(self.locators.DATE_TIME_INPUT)
        value_date_before = input_date.get_attribute('value')
        input_date.click()
        self.element_is_visible(self.locators.DATE_TIME_SELECT_MONTH).click()
        self.set_date_item_from_list(self.locators.DATE_TIME_SELECT_MONTH_LIST, date.month)
        self.element_is_visible(self.locators.DATE_TIME_SELECT_YEAR).click()
        self.set_date_item_from_list(self.locators.DATE_TIME_SELECT_YEAR_LIST, "2020")
        self.set_date_item_from_list(self.locators.DATE_SELECT_DAY_LIST, date.day)
        self.set_date_item_from_list(self.locators.DATE_TIME_SELECT_TIME_LIST, date.time)
        value_date_after = input_date.get_attribute('value')
        return value_date_before, value_date_after




    def  set_date_by_text(self, element, value):
        # нажатие селекта для раскрытия списков в датапикере
        select = Select(self.element_is_present(element))
        select.select_by_visible_text(value)

    def set_date_item_from_list(self, elements, value):
        # выбор значения в раскрывшемся датапикере со значениями
        item_list = self.elements_are_presents(elements)
        for item in item_list:
            if item.text == value:
                item.click()
                break




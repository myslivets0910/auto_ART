import base64
import os
import random
import time

import requests
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from generator.generator import generated_color
from locators.widgets_locators import AccordianPageLocators, AutoCompletePageLocators
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
        return [section_title.text, len(section_content)]

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





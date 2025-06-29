import base64
import os
import random
import time

import requests
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from locators.widgets_locators import AccordianPageLocators
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
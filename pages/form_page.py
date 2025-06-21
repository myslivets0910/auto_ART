import base64
import os
import random
import time

import requests
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from locators.form_page_locators import PracticeFormPageLocators
from pages.base_page import BasePage
from generator.generator import generated_person, generated_file, generated_subject, generated_state_selected, \
    generated_city_selected


class PracticeFormPage(BasePage):
    locators = PracticeFormPageLocators()

    def fill_form_fields(self):
        person = next(generated_person())
        file_name, path = generated_file()
        self.remove_footer()
        self.element_is_visible(self.locators.FIRST_NAME_INPUT).send_keys(person.firstname)
        self.element_is_visible(self.locators.LAST_NAME_INPUT).send_keys(person.lastname)
        self.element_is_visible(self.locators.EMAIL_INPUT).send_keys(person.email)
        self.element_is_visible(self.locators.GENDER_RADIO_BUTTON).click()
        self.element_is_visible(self.locators.MOBILE_INPUT).send_keys(person.mobile)
        self.element_is_visible(self.locators.SUBJECT_INPUT_SELECT).send_keys(generated_subject())
        self.element_is_visible(self.locators.SUBJECT_INPUT_SELECT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.HOBBIES_CHECKBOX).click()
        self.element_is_present(self.locators.PICTURE_UPLOAD).send_keys(path)
        os.remove(path)
        self.element_is_visible(self.locators.CURRENT_ADDRESS_INPUT).send_keys(person.current_address)
        self.element_is_visible(self.locators.STATE_SELECT).click()
        self.element_is_visible(self.locators.STATE_INPUT).send_keys(generated_state_selected())
        self.element_is_visible(self.locators.STATE_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.CITY_SELECT).click()
        self.element_is_visible(self.locators.CITY_INPUT).get_property(generated_city_selected(generated_state_selected()))
        self.element_is_visible(self.locators.CITY_INPUT).send_keys(Keys.RETURN)
        self.element_is_visible(self.locators.SUBMIT_BUTTON_FORM).click()
        return person


    def form_result(self):
        result_list = self.elements_are_presents(self.locators.TABLE_FORM_RESULT)
        data = []
        for item in result_list:
            self.go_to_element(item)
            data.append(item.text)
        return data








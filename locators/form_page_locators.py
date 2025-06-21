import random
from random import randint

from selenium.webdriver.common.by import By



class PracticeFormPageLocators:

    #form
    FIRST_NAME_INPUT = (By.CSS_SELECTOR,'#firstName')
    LAST_NAME_INPUT = (By.CSS_SELECTOR,'#lastName')
    EMAIL_INPUT = (By.CSS_SELECTOR,'#userEmail')
    GENDER_RADIO_BUTTON = (By.CSS_SELECTOR, f"label[for='gender-radio-{random.randint(1,3)}']")
    # проставляем рандомный значение на уровне селектора
    MOBILE_INPUT = (By.CSS_SELECTOR,'#userNumber')
    DATE_OF_BIRTH_DATAFORM = (By.CSS_SELECTOR,'#dateOfBirthInput')
    SUBJECT_INPUT_SELECT = (By.CSS_SELECTOR,'#subjectsInput')
    HOBBIES_CHECKBOX = (By.CSS_SELECTOR,f'label[for="hobbies-checkbox-{random.randint(1,3)}"]')
    # проставляем рандомный значение на уровне селектора
    PICTURE_UPLOAD = (By.CSS_SELECTOR,'#uploadPicture')
    CURRENT_ADDRESS_INPUT = (By.CSS_SELECTOR,'#currentAddress')
    STATE_SELECT = (By.CSS_SELECTOR,'#state')
    STATE_INPUT = (By.CSS_SELECTOR,'#react-select-3-input')
    CITY_SELECT = (By.CSS_SELECTOR,'#city')
    CITY_INPUT = (By.CSS_SELECTOR,'#react-select-4-input')

    # result
    SUBMIT_BUTTON_FORM = (By.CSS_SELECTOR,'#submit')
    TABLE_FORM_RESULT = (By.XPATH, '//div[@class="table-responsive"]//td[2]')
    # используем индекс 2 для таблицы, так как идет вторая колонка в таблице result
    CLOSE_BUTTON_TABLE_FORM_RESULT = (By.CSS_SELECTOR,'')
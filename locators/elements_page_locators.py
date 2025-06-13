# в данном файле называем все селекторы которые есть на странице / https://demoqa.com/text-box

from selenium.webdriver.common.by import By


class TextBoxPageLocators:  # класс назван как страница

    # form fields - поля формы
    FULL_NAME = (By.XPATH, "//*[@id='userName']")
    EMAIL = (By.XPATH, "//*[@id='userEmail']")
    CURRENT_ADDRESS = (By.XPATH, "//*[@id='currentAddress']")
    PERMANENT_ADDRESS = (By.XPATH, "//*[@id='permanentAddress']")
    SUBMIT = (By.XPATH, "//*[@id='submit']")

    # created form - заполненная форма
    CREATED_FULL_NAME = (By.XPATH, '//*[@id="name"]')
    CREATED_EMAIL = (By.XPATH, '//*[@id="email"]')
    CREATED_CURRENT_ADDRESS = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[6]/div/p[3]')
    CREATED_PERMANENT_ADDRESS = (By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[6]/div/p[4]')


class CheckBoxPageLocators:  # определили локаторы на странице чекбокса.

    EXPAND_ALL_BUTTON = (By.XPATH, '//*[@id="tree-node"]/div/button[1]')  # кнопка которая раскрывает весь список
    ITEM_LIST = (By.CSS_SELECTOR,
                 'span[class = "rct-title"]')  # определяет все элементы на странице с таким значение класса "class = 'rct-title'
    CHECKED_ITEMS = (By.CSS_SELECTOR, "svg[class = 'rct-icon rct-icon-check']")
    TITLE_ITEM = (By.XPATH, './/ancestor::span[@class="rct-text"]')
    OUTPUT_RESULT = (By.CSS_SELECTOR, "span[class = 'text-success']")

class RadioButtonPageLocators: # определили локаторы на странице радиокнопки.

    YES_RADIOBUTTON = (By.XPATH, "//label[contains(@class, 'custom-control-label') and text()='Yes']")
    IMPRESSIVE_RADIOBUTTON =(By.XPATH, "//label[contains(@class, 'custom-control-label') and text()='Impressive']")
    NO_RADIBUTTON = (By.XPATH,"//label[contains(@class, 'custom-control-label') and text()='No']")
    OUTPUT_RESULT_BUTTON = (By.CSS_SELECTOR, 'p span[class = "text-success"]')
    # c помощью chatgpt



# в данном файле называем все селекторы которые есть на странице / https://demoqa.com/text-box

from selenium.webdriver.common.by import By

class TextBoxPageLocators: # класс назван как страница

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
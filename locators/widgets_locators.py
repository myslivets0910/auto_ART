import random
from random import randint

from selenium.webdriver.common.by import By


class AccordianPageLocators:

    SECTION_1 = (By.CSS_SELECTOR,'div[id="section1Heading"]')
    SECTION_1_TEXT = (By.CSS_SELECTOR,'div[id="section1Content"] p')

    SECTION_2 = (By.CSS_SELECTOR,'div[id="section2Heading"]')
    SECTION_2_TEXT = (By.CSS_SELECTOR,'div[id="section2Content"] p')

    SECTION_3 = (By.CSS_SELECTOR,'div[id="section3Heading"]')
    SECTION_3_TEXT = (By.CSS_SELECTOR,'div[id="section3Content"] p')

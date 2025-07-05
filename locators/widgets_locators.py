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


class AutoCompletePageLocators:
    # селекторы
    MULTI_COMPLETE_INPUT = (By.CSS_SELECTOR,'input[id="autoCompleteMultipleInput"]')
    MULTI_COMPLETE_VALUE = (By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue auto-complete__multi-value"]')
    MULTI_COMPLETE_REMOVE = (By.CSS_SELECTOR, 'div[class="css-1rhbuit-multiValue auto-complete__multi-value"] svg path')


    SINGLE_COMPLETE_INPUT = (By.CSS_SELECTOR,'input[id="autoCompleteSingleInput"]')
    SINGLE_COMPLETE_VALUE = (By.CSS_SELECTOR, 'div[class="auto-complete__single-value css-1uccc91-singleValue"]')



class DatePickerPageLocators:
    #data
    DATE_INPUT = (By.CSS_SELECTOR,'input[id="datePickerMonthYearInput"]')
    DATE_SELECT_MONTH = (By.CSS_SELECTOR,'select[class="react-datepicker__month-select"]')
    DATE_SELECT_YEAR = (By.CSS_SELECTOR,'select[class="react-datepicker__year-select"]')
    DATE_SELECT_DAY_LIST = (By.CSS_SELECTOR,'div[class^="react-datepicker__day react-datepicker__day"]')

    #data_and_time
    DATE_TIME_INPUT = (By.CSS_SELECTOR,'input[id="dateAndTimePickerInput"]')

    DATE_TIME_SELECT_MONTH = (By.CSS_SELECTOR,'div[class="react-datepicker__month-read-view"]')
    DATE_TIME_SELECT_MONTH_LIST = (By.CSS_SELECTOR,'div[class="react-datepicker__month-option"]')

    DATE_TIME_SELECT_YEAR = (By.CSS_SELECTOR,'div[class="react-datepicker__year-read-view"]')
    DATE_TIME_SELECT_YEAR_LIST = (By.CSS_SELECTOR,'div[class="react-datepicker__year-option"]')

    DATE_TIME_SELECT_TIME_LIST = (By.CSS_SELECTOR,'li[class="react-datepicker__time-list-item "]')


class SliderPageLocators:
    INPUT_SLIDER = (By.CSS_SELECTOR,'input[class="range-slider range-slider--primary"]')
    VALUE_SLIDER = (By.CSS_SELECTOR,'input[id="sliderValue"]')
    pass

class ProgressBarPageLocators:

    PROGRESS_BAR_BUTTON = (By.CSS_SELECTOR,'button[id="startStopButton"]')
    PROGRESS_BAR_VALUE = (By.CSS_SELECTOR,'div[class="progress-bar bg-info"]')


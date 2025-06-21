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


class RadioButtonPageLocators:  # определили локаторы на странице радиокнопки.

    YES_RADIOBUTTON = (By.XPATH, "//label[contains(@class, 'custom-control-label') and text()='Yes']")
    IMPRESSIVE_RADIOBUTTON = (By.XPATH, "//label[contains(@class, 'custom-control-label') and text()='Impressive']")
    NO_RADIBUTTON = (By.XPATH, "//label[contains(@class, 'custom-control-label') and text()='No']")
    OUTPUT_RESULT_BUTTON = (By.CSS_SELECTOR, 'p span[class = "text-success"]')
    # c помощью chatgpt


class WebTablePageLocators:  # определили локаторы на странице c таблицей.

    ADD_BUTTON_PERSON_WEBTABLE = (By.CSS_SELECTOR, '#addNewRecordButton')

    # form
    FIRST_NAME_INPUT_WEBTABLE = (By.CSS_SELECTOR, '#firstName')
    LAST_NAME_INPUT_WEBTABLE = (By.CSS_SELECTOR, '#lastName')
    EMAIL_INPUT_WEBTABLE = (By.CSS_SELECTOR, '#userEmail')
    AGE_INPUT_WEBTABLE = (By.CSS_SELECTOR, '#age')
    SALARY_INPUT_WEBTABLE = (By.CSS_SELECTOR, '#salary')
    DEPARTMENT_INPUT_WEBTABLE = (By.CSS_SELECTOR, '#department')
    SUBMIT_ADD_FORM_PERSON_WEBTABLE = (By.CSS_SELECTOR, '#submit')

    # table
    FULL_PEOPLE_LIST = (By.XPATH, '//div[@class="rt-tr-group"]')
    SEARCH_TABLE = (By.XPATH, '//*[@id="searchBox"]')
    SEARCH_TABLE_BUTTON = (By.XPATH, '//*[@id="basic-addon2"]')
    ROW_PARENT_SEARCH_TABLE = (By.XPATH, './/ancestor::div[@class="rt-tr-group"]')
    NO_ROWS_FOUND = (By.XPATH, '//div[@class="rt-noData"]')

    # update_table
    UPDATE_BUTTON_PERSON = (By.CSS_SELECTOR, 'span[title = "Edit"]')
    DELETE_BUTTON_PERSON = (By.XPATH, '//span[@title="Delete"]')
    CHANGE_THE_LINES_PAGE = (By.XPATH, '//select[@aria-label="rows per page"]')


class ButtonsPageLocators:  # определили локаторы на странице c кнопками.

    # buttons
    DOUBLE_CLICK_ME_BUTTON = (By.XPATH, '//button[@id="doubleClickBtn"]')
    RIHGHT_CLICK_ME_BUTTON = (By.XPATH, '//button[@id="rightClickBtn"]')
    CLICK_ME_BUTTON = (
    By.XPATH, '//button[text()="Click Me"]')  # здесь динамический айдишник, и нашил вариант с текстом кнопки

    # result_buttons
    DOUBLE_CLICK_ME_RESULT = (By.XPATH, '//p[@id="doubleClickMessage"]')
    RIHGHT_CLICK_ME_RESULT = (By.XPATH, '//p[@id="rightClickMessage"]')
    CLICK_ME_RESULT = (By.XPATH, '//p[@id="dynamicClickMessage"]')


class LinksPageLocators:
    SIMPLE_LINK_HOME = (By.XPATH, '//*[@id="simpleLink"]')
    BAD_REQUEST_LINK = (By.CSS_SELECTOR, 'a[id = "bad-request"]')


class UploadDownloadPageLocators:

    INPUT_UPLOAD_FILE = (By.XPATH,'//*[@id="uploadFile"]')
    UPLOADED_RESULT = (By.XPATH, '//*[@id = "uploadedFilePath"]')

    BUTTON_DOWNLOAD = (By.XPATH, '//*[@id="downloadButton"]')

class DynamicPropertiesPageLocators:
    COLOR_CHANGE_BUTTON = (By.CSS_SELECTOR,'button[id="colorChange"]')
    VISIBLE_AFTER_5_SECONDS = (By.CSS_SELECTOR,'button[id="visibleAfter"]')
    WILL_ENABLE_5_SECONDS = (By.CSS_SELECTOR, 'button[id="enableAfter"]')


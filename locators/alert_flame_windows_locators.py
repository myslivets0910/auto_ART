

from selenium.webdriver.common.by import By

class BrowserWindowPageLocators:

    NEW_TAB_BUTTON = (By.XPATH,"//*[@id='tabButton']")
    NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, '#windowButton')
    NEW_WINDOW_MESSAGE_BUTTON = (By.CSS_SELECTOR, "//*[@id='messageWindowButton']")

    #result_tab_window
    NEW_TAB_BUTTON_RESULT = (By.XPATH, "//*[@id='sampleHeading']")

    NEW_WINDOW_BUTTON_RESULT = (By.XPATH, "//*[@id='sampleHeading']")
    NEW_WINDOW_MESSAGE_BUTTON_RESULT = (By.CSS_SELECTOR, "//*[@id='messageWindowButton']")

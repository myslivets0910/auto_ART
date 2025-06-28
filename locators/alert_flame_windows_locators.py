

from selenium.webdriver.common.by import By

class BrowserWindowPageLocators:

    NEW_TAB_BUTTON = (By.XPATH,"//*[@id='tabButton']")
    NEW_WINDOW_BUTTON = (By.CSS_SELECTOR, '#windowButton')
    NEW_WINDOW_MESSAGE_BUTTON = (By.CSS_SELECTOR, "//*[@id='messageWindowButton']")

    #result_tab_window
    NEW_TAB_BUTTON_RESULT = (By.XPATH, "//*[@id='sampleHeading']")

    NEW_WINDOW_BUTTON_RESULT = (By.XPATH, "//*[@id='sampleHeading']")
    NEW_WINDOW_MESSAGE_BUTTON_RESULT = (By.CSS_SELECTOR, "//*[@id='messageWindowButton']")



class AlertWindowPageLocators:

    #buttons
    SEE_ALERT_BUTTON = (By.XPATH, '//*[@id="alertButton"]')
    TIMER_ALERT_BUTTON = (By.XPATH, '//*[@id="timerAlertButton"]')
    CONFIRM_ALERT_BUTTON = (By.XPATH, '//*[@id="confirmButton"]')
    PROMPT_INPUT_ALERT_BUTTON = (By.XPATH, '//*[@id="promtButton"]')

    # result
    RESULT_CONFIRM_ALERT_ACCEPT = (By.CSS_SELECTOR, 'span[id="confirmResult"]')
    RESULT_INPUT_VALUE_ALERT_ACCEPT = (By.CSS_SELECTOR, 'span[id="promptResult"]')


class FramePageLocators:

    FRAME_1 = (By.CSS_SELECTOR, 'iframe[id="frame1"]')
    FRAME_2 = (By.CSS_SELECTOR, 'iframe[id="frame2"]')
    TITLE_FRAME = (By.XPATH, "//*[@id='sampleHeading']")

class NestedFramesPageLocators:

    PARENT_FRAME = (By.CSS_SELECTOR, 'iframe[id="frame1"]')
    CHILD_FRAME = (By.CSS_SELECTOR, 'iframe[srcdoc="<p>Child Iframe</p>"]')
    PARENT_FRAME_TITLE = (By.CSS_SELECTOR, 'body')
    CHILD_FRAME_TITLE = (By.CSS_SELECTOR, 'p')

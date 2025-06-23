import base64
import os
import random
import time

from selenium.common import TimeoutException

from locators.alert_flame_windows_locators import BrowserWindowPageLocators, AlertWindowPageLocators
from pages.base_page import BasePage


class BrowserWindowPage(BasePage):
    locators = BrowserWindowPageLocators()

    def check_opened_new_tab(self):
        # метод на получение текста на новой вкладе
        self.element_is_visible(self.locators.NEW_TAB_BUTTON).click() # по клику открылось новая вкалдка, на которую нас и перевело
        self.driver.switch_to.window(self.driver.window_handles[1])
        # перенаправили фокус на новую вкладу, (она у нас 2 теперь, но по коду она 1
        # (0 - первая вкладка,1 - вторая вклада,2 - треться вкалка
        new_window_text = self.element_is_present(self.locators.NEW_TAB_BUTTON_RESULT).text
        # print(new_window_text)
        return new_window_text

    def check_opened_new_window(self):
        # метод на получение текста на новой вкладе
        self.element_is_visible(self.locators.NEW_WINDOW_BUTTON).click() # по клику открылось новое окно, на которую нас и перевело
        self.driver.switch_to.window(self.driver.window_handles[1])
        # перенаправили фокус на новое окно, (она у нас 2 теперь, но по коду она 1
        # (0 - первая вкладка,1 - вторая вклада,2 - треться вкалка
        new_window_text = self.element_is_present(self.locators.NEW_WINDOW_BUTTON_RESULT).text
        #print(new_window_text)
        return new_window_text

class AlertWindowPage(BasePage):
    locators = AlertWindowPageLocators()

    def check_see_alert(self):
        self.element_is_visible(self.locators.SEE_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        # print(alert_window.text)
        return alert_window.text

    def check_alert_appear_5_sec(self):
        self.element_is_visible(self.locators.TIMER_ALERT_BUTTON).click()
        time.sleep(5)
        alert_window = self.driver.switch_to.alert
        # print(alert_window.text)
        return alert_window.text

    def check_confirm_alert(self):
        self.element_is_visible(self.locators.CONFIRM_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.accept()
        text_result = self.element_is_present(self.locators.RESULT_CONFIRM_ALERT_ACCEPT).text
        return text_result

    def check_input_value_alert(self):
        text = f"autotest{random.randint(0,999)}"
        # для ввода любого значение в инпут алерта
        self.element_is_visible(self.locators.PROMPT_INPUT_ALERT_BUTTON).click()
        alert_window = self.driver.switch_to.alert
        alert_window.send_keys(text)
        alert_window.accept()
        text_result = self.element_is_present(self.locators.RESULT_INPUT_VALUE_ALERT_ACCEPT).text
        return text, text_result


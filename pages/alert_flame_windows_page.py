import base64
import os
import random
import time

from selenium.common import TimeoutException

from locators.alert_flame_windows_locators import BrowserWindowPageLocators
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

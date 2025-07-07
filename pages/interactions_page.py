import base64
import os
import random
import time


import requests
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from generator.generator import generated_color, generated_date
from locators.interactions_locators import SortablePageLocators
from pages.base_page import BasePage


class SortablePage(BasePage):
    locators = SortablePageLocators()
    def get_sortable_items(self, elements):
        # метод который вытаскивает список элементов
        item_list = self.elements_are_visible(elements)
        return [item.text for item in item_list]

    def change_list_order(self):
        # метод, который ищет и перемещает элементы + возращает результаты до и после
        self.element_is_visible(self.locators.LIST_TAB).click()
        order_before = self.get_sortable_items(self.locators.LIST_TAB_ITEM)
        item_list = random.sample(self.elements_are_presents(self.locators.LIST_TAB_ITEM), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_items(self.locators.LIST_TAB_ITEM)
        return order_before , order_after

    def change_grid_order(self):
        # метод, который ищет и перемещает элементы + возращает результаты до и после
        self.element_is_visible(self.locators.GRID_TAB).click()
        order_before = self.get_sortable_items(self.locators.GRID_TAB_ITEM)
        item_list = random.sample(self.elements_are_presents(self.locators.GRID_TAB_ITEM), k=2)
        item_what = item_list[0]
        item_where = item_list[1]
        self.action_drag_and_drop_to_element(item_what, item_where)
        order_after = self.get_sortable_items(self.locators.GRID_TAB_ITEM)
        return order_before , order_after


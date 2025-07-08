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
from locators.interactions_locators import SortablePageLocators, SelectablePageLocators, ResizablePageLocators
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
        return order_before, order_after



class SelectablePage(BasePage):
    locators = SelectablePageLocators()
    def click_selectable_item(self, elements):
        # метод ищет список, и  который кликает на элемент списка
        item_list = self.elements_are_visible(elements)
        random.sample(item_list, k=2)[0].click()

    def select_list_item(self):
        # метод, который выбирает на какой элемент списка кликнуть и возвращает его
        self.element_is_visible(self.locators.LIST_TAB).click()
        self.click_selectable_item(self.locators.LIST_TAB_ITEM)
        active_element = self.element_is_visible(self.locators.LIST_TAB_ITEM_ACTIVE)
        return active_element.text

    def select_grid_item(self):
        # метод, который выбирает на какой  элемент списка кликнуть и возвращает его
        self.element_is_visible(self.locators.GRID_TAB).click()
        self.click_selectable_item(self.locators.GRID_TAB_ITEM)
        active_element = self.element_is_visible(self.locators.GRID_TAB_ITEM_ACTIVE)
        return active_element.text


class ResizablePage(BasePage):
    locators = ResizablePageLocators()

    def get_px_from_width_height(self, value_of_size):
        # вспомогательный метод для определения размеров окна
        width = value_of_size.split(';')[0].split(':')[1].replace(' ','')
        height = value_of_size.split(';')[0].split(':')[1].replace(' ','')
        return width, height

    def get_max_min_size(self, element):
        # вспомогательный метод для определения размеров элемента
        size = self.element_is_present(element)
        size_value = size.get_attribute('style')
        return size_value

    def change_size_resizable_box(self):
        # метод, который передвигает угол окна по координатам
        self.action_drag_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_BOX_HANDLE), 400, 200)
        max_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))
        self.action_drag_and_drop_by_offset(self.element_is_present(self.locators.RESIZABLE_BOX_HANDLE), -100, -50)
        mix_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE_BOX))
        return max_size, mix_size

    def change_size_resizable(self):
        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_HANDLE),
                                            random.randint(20,50),random.randint(60,70))

        max_size = self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE))

        self.action_drag_and_drop_by_offset(self.element_is_visible(self.locators.RESIZABLE_HANDLE),
                                           random.randint(-50, -40), random.randint(-30, -20))
        min_size =self.get_px_from_width_height(self.get_max_min_size(self.locators.RESIZABLE))
        return max_size, min_size






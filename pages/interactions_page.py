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
from locators.interactions_locators import SortablePageLocators, SelectablePageLocators, ResizablePageLocators, \
    DroppablePageLocators
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



class DroppablePage(BasePage):
    locators = DroppablePageLocators()

    def drop_simple(self):
        # методы,  который перетаскивает элемент в элемент и возращает текст элементов
        self.element_is_visible(self.locators.TAB_SIMPLE).click()
        drag_div = self.element_is_visible(self.locators.DRAG_ME_SIMPLE)
        drop_div = self.element_is_visible(self.locators.DROP_HERE_SIMPLE)
        self.action_drag_and_drop_to_element(drag_div, drop_div)
        return drop_div.text

    def drop_accept(self):
        # методы,  который перетаскивает элемент в элемент и возращает текст элементов
        self.element_is_visible(self.locators.TAB_ACCEPT).click() # клик на таб
        # указываем на элементы, что есть на странице
        acceptable_div = self.element_is_visible(self.locators.ACCEPTABLE)
        not_acceptable_div = self.element_is_visible(self.locators.NOT_ACCEPTABLE)
        drop_div = self.element_is_visible(self.locators.DROP_HERE_ACCEPT)
        # перетаскиваем элемент в элемент
        self.action_drag_and_drop_to_element(not_acceptable_div, drop_div)
        drop_div_not_acceptable = drop_div.text
        # перетаскиваем элемент в элемент
        self.action_drag_and_drop_to_element(acceptable_div, drop_div)
        drop_div_acceptable = drop_div.text
        # выводим результат перетаскиваний
        return drop_div_not_acceptable, drop_div_acceptable


    def drop_prevent(self):
        # методы,  который перетаскивает элементы в элемент и возращает текст элементов
        self.element_is_visible(self.locators.TAB_PREVENT).click()
        drag_div = self.element_is_visible(self.locators.DRAG_ME_PREVENT)
        not_greedy_box_inner = self.element_is_visible(self.locators.NOT_GREEDY_INNER_BOX)
        greedy_box_inner = self.element_is_visible(self.locators.GREEDY_INNER_BOX)

        self.action_drag_and_drop_to_element(drag_div, not_greedy_box_inner)
        text_not_greedy_box = self.element_is_visible(self.locators.NOT_GREEDY_DROP_BOX_TEXT).text
        text_not_greedy_box_inner = not_greedy_box_inner.text

        self.action_drag_and_drop_to_element(drag_div, greedy_box_inner)
        text_greedy_box = self.element_is_visible(self.locators.GREEDY_DROP_BOX_TEXT).text
        text_greedy_box_inner = greedy_box_inner.text

        return text_not_greedy_box, text_not_greedy_box_inner, text_greedy_box, text_greedy_box_inner


    def drop_will_revert_draggable(self):
        # методы,  который перетаскивает элемент в элемент и возращает координаты элементов
        # не используется
        self.element_is_visible(self.locators.TAB_REVENT).click()
        will_revert = self.element_is_visible(self.locators.WILL_REVENT)
        drop_div = self.element_is_visible(self.locators.DROP_HERE_REVENT)

        self.action_drag_and_drop_to_element(will_revert, drop_div)
        position_after_move = will_revert.get_attribute('style')
        time.sleep(1)
        position_after_revert = will_revert.get_attribute('style')
        return position_after_move, position_after_revert

    def drop_revert_draggable(self, type_drag):
        # методы,  который перетаскивает элемент в элемент и возвращает координаты элементов
        #используется, общий для всей вкладки
        drags = {'will':
                    {'revert': self.locators.WILL_REVENT,},
                'not_will':
                    {'revert': self.locators.NOT_REVENT},
        }
        self.element_is_visible(self.locators.TAB_REVENT).click()
        revert = self.element_is_visible(drags[type_drag]['revert'])
        drop_div = self.element_is_visible(self.locators.DROP_HERE_REVENT)
        self.action_drag_and_drop_to_element(revert, drop_div)
        position_after_move = revert.get_attribute('style')
        time.sleep(1)
        position_after_revert = revert.get_attribute('style')
        return position_after_move, position_after_revert



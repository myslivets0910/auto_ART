import random
from random import randint

from selenium.webdriver.common.by import By


class SortablePageLocators:

        LIST_TAB = (By.CSS_SELECTOR,'a[id="demo-tab-list"]')
        # список элементов из таба LIST
        LIST_TAB_ITEM = (By.CSS_SELECTOR, 'div[id="demo-tabpane-list"] div[class="list-group-item list-group-item-action"]')

        GRID_TAB = (By.CSS_SELECTOR,'a[id="demo-tab-grid"]')
        # список элементов из таба GRID
        GRID_TAB_ITEM = (By.CSS_SELECTOR, 'div[id="demo-tabpane-grid"] div[class="list-group-item list-group-item-action"]')


class SelectablePageLocators:

        LIST_TAB = (By.CSS_SELECTOR, 'a[id="demo-tab-list"]')
        # список элементов из таба LIST
        LIST_TAB_ITEM = (By.CSS_SELECTOR,
                         'ul[id="verticalListContainer"] li[class="mt-2 list-group-item list-group-item-action"]')
        LIST_TAB_ITEM_ACTIVE = \
                (By.CSS_SELECTOR,
                 'ul[id="verticalListContainer"] li[class="mt-2 list-group-item active list-group-item-action"]')

        GRID_TAB = (By.CSS_SELECTOR, 'a[id="demo-tab-grid"]')
        # список элементов из таба GRID
        GRID_TAB_ITEM = (By.CSS_SELECTOR,
                         'div[id="gridContainer"] li[class="list-group-item list-group-item-action"]')
        GRID_TAB_ITEM_ACTIVE = (By.CSS_SELECTOR,
                                'div[id="gridContainer"] li[class="list-group-item active list-group-item-action"]')
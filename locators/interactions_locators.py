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


class ResizablePageLocators:

    RESIZABLE_BOX_HANDLE = (By.CSS_SELECTOR,
                 'div[class="constraint-area"] span[class="react-resizable-handle react-resizable-handle-se"]')

    RESIZABLE_BOX = (By.CSS_SELECTOR,'div[id="resizableBoxWithRestriction"]')
    RESIZABLE_HANDLE = (By.CSS_SELECTOR, 'div[id="resizable"] span[class="react-resizable-handle react-resizable-handle-se"]')
    RESIZABLE = (By.CSS_SELECTOR, 'div[id="resizable"]')


class DroppablePageLocators:
    #simple
    TAB_SIMPLE = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-simple"]')
    DRAG_ME_SIMPLE = (By.CSS_SELECTOR, 'div[id="simpleDropContainer"] div[id="draggable"]')
    DROP_HERE_SIMPLE = (By.CSS_SELECTOR, 'div[id="simpleDropContainer"] div[id="droppable"]')


    # accept
    TAB_ACCEPT = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-accept"]')
    ACCEPTABLE = (By.CSS_SELECTOR, 'div[id="acceptable"]')
    NOT_ACCEPTABLE = (By.CSS_SELECTOR, 'div[id="notAcceptable"]')
    DROP_HERE_ACCEPT = (By.CSS_SELECTOR, 'div[id="acceptDropContainer"] div[id="droppable"]')


    # prevent
    TAB_PREVENT = (By.CSS_SELECTOR, 'a[id="droppableExample-tab-preventPropogation"]')
    NOT_GREEDY_DROP_BOX_TEXT = (By.CSS_SELECTOR, 'div[id="notGreedyDropBox"] p:nth-child(1)')
    NOT_GREEDY_INNER_BOX = (By.CSS_SELECTOR, 'div[id="notGreedyInnerDropBox"]')
    GREEDY_DROP_BOX_TEXT = (By.CSS_SELECTOR, 'div[id="greedyDropBox"] p:nth-child(1)')
    GREEDY_INNER_BOX = (By.CSS_SELECTOR, 'div[id="greedyDropBoxInner"]')
    DRAG_ME_PREVENT = (By.CSS_SELECTOR, 'div[id="ppDropContainer"] div[id="dragBox"]')
    # revent
    TAB_REVENT = (By.CSS_SELECTOR, '#droppableExample-tab-revertable')
    WILL_REVENT = (By.CSS_SELECTOR, 'div[id="revertable"]')
    NOT_REVENT = (By.CSS_SELECTOR, 'div[id="notRevertable"]')
    DROP_HERE_REVENT = (By.CSS_SELECTOR, '#revertableDropContainer #droppable')





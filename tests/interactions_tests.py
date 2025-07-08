import time

from pages.interactions_page import SortablePage, SelectablePage, ResizablePage


class TestInteractions:
    class TestSortablePage:
        def test_sortable(self, driver):

            sortable_page = SortablePage(driver, "https://demoqa.com/sortable")
            sortable_page.open()
            list_before, list_after = sortable_page.change_list_order()
            grid_before, grid_after = sortable_page.change_grid_order()
            #print(list_before,list_after)
            #print(grid_before,grid_after)
            assert list_before != list_after, 'Ошибка, списки LIST не должны быть равны'
            assert grid_before != grid_after, 'Ошибка, списки GRID не должны быть равны'


    class TestSelectablePage:
        def test_selectable(self, driver):

            selectable_page = SelectablePage(driver, "https://demoqa.com/selectable")
            selectable_page.open()
            list_active = selectable_page.select_list_item()
            grid_active = selectable_page.select_grid_item()
            #print(list_active)
            #print(grid_active)
            assert len(list_active) > 0 , 'Ошибка, элемент не выбран из списка'
            assert len(grid_active) > 0 , 'Ошибка, элемент не выбран из списка'

    class TestResizablePage:
        # изменяющиеся окна в размерах
        def test_resizable(self, driver):
            resizable_page = ResizablePage(driver, "https://demoqa.com/resizable")
            resizable_page.open()
            max_box, min_box = resizable_page.change_size_resizable_box()
            max_box_r, min_box_r = resizable_page.change_size_resizable()
            print(min_box, max_box)
            print(min_box_r, max_box_r)

            assert ('400px', '400px') == min_box, 'минимальные границы не равны 400рх'
            assert ('500px', '500px') == max_box, 'максимальные границы не равны 500рх'
            assert min_box_r != max_box_r ,'Ошибка, минимальная и максимальная граница одинаковые'




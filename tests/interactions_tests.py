import time

from pages.interactions_page import SortablePage, SelectablePage, ResizablePage, DroppablePage


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


    class TestDroppablePage:
     # тест на перемещение элементов в элемент
        def test_droppable_simple(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            text_simple = droppable_page.drop_simple()
            print(text_simple)
            assert text_simple == "Dropped!", 'Текст в DROP не совпадает с результатом'

        def test_droppable_accept(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            not_accept, accept = droppable_page.drop_accept()
            #print(not_accept)
            #print(accept)
            assert not_accept == "Drop here", 'Текст в DROP не совпадает при not_accept'
            assert accept == "Dropped!", 'Текст в DROP не совпадает при accept'

        def test_droppable_prevent_propogation(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            text_1, text_2, text_3, text_4 = droppable_page.drop_prevent()
            print(text_1)
            print(text_2)
            print(text_3)
            print(text_4)

            assert text_1 == "Dropped!", 'Текст в DROP не совпадает при Drag Me'
            assert text_2 == "Dropped!", 'Текст в DROP не совпадает при Drag Me'
            assert text_3 == "Outer droppable", 'Текст в DROP не совпадает при Drag Me'
            assert text_4 == "Dropped!", 'Текст в DROP не совпадает при Drag Me'

        def test_droppable_revent_draggable(self, driver):
            droppable_page = DroppablePage(driver, "https://demoqa.com/droppable")
            droppable_page.open()
            will_after_move, will_after_revert = droppable_page.drop_revert_draggable("will")
            not_will_after_move, not_will_after_revert = droppable_page.drop_revert_draggable("not_will")
            assert will_after_move != will_after_revert, 'Ошибка, элемент не переместился'
            assert not_will_after_move == not_will_after_revert, 'Ошибка, элемент переместился'

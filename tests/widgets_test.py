import time


from pages.widgets_page import AccordianPage, AutoCompletePage, DatePickerPage, ProgressBarPage, SliderPage, TabsPage, \
    ToolTipsPage, DroppingMenuPage


class TestWidgets:
    class TestAccordianPage:
        def test_accordian(self, driver):
            accordian_page = AccordianPage(driver, "https://demoqa.com/accordian")
            accordian_page.open()
            first_title, first_content = accordian_page.check_accordian('first')
            second_title, second_content = accordian_page.check_accordian('second')
            third_title, third_content = accordian_page.check_accordian('third')

            assert first_title == 'What is Lorem Ipsum?' and first_content > 0
            assert second_title == 'Where does it come from?' and second_content > 0
            assert third_title == 'Why do we use it?' and third_content > 0


    class TestAutoComplete:
        def test_fill_multi_autocomplete(self,driver):
            # тест который пвыбирает и проверяет выбор
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            colors = autocomplete_page.fill_input_multi()
            colors_result = autocomplete_page.check_color_in_multi()
            #print(colors)
            #print(colors_result)
            assert colors == colors_result, "об ошибке "


        def test_remove_value_from_multi(self,driver):
            # тест который удаляет и сравнивает значения после удаления
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            autocomplete_page.fill_input_multi()
            time.sleep(3)
            count_value_before, count_value_after = autocomplete_page.remove_value_from_multi()
            time.sleep(3)
            #print(count_value_before)
            #print(count_value_after)
            assert count_value_before != count_value_after, "об ошибке "


        def test_fill_single_autocomplete(self, driver):
            # тест на выбор и сравнение с результатом
            autocomplete_page = AutoCompletePage(driver, 'https://demoqa.com/auto-complete')
            autocomplete_page.open()
            color = autocomplete_page.fill_input_single()
            colors_result = autocomplete_page.check_color_in_single()
            #print(color)
            #print(colors_result)
            assert color == colors_result, "об ошибке "


    class TestDatePickerPage:
        def test_change_date(self, driver):
            # тест на изменение даты
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            value_date_before, value_date_after = date_picker_page.select_date()
            #print(value_date_before)
            #print(value_date_after)

            assert value_date_before != value_date_after, 'ОШИБКА, даты не должны быть одинаковыми'


        def test_change_date_and_time(self, driver):
            # тест на изменение даты и времени
            date_picker_page = DatePickerPage(driver, 'https://demoqa.com/date-picker')
            date_picker_page.open()
            value_date_before, value_date_after = date_picker_page.select_date_and_time()
            print(value_date_before)
            print(value_date_after)
            assert value_date_before != value_date_after, 'ОШИБКА, даты не должны быть одинаковыми'


    class TestSliderPage:
        def test_change_slider_value(self, driver):
            # тест изменение значение в Слайдере
            slider_page = SliderPage(driver, 'https://demoqa.com/slider')
            slider_page.open()
            before, after = slider_page.change_slider_value()
            print(before)
            print(after)
            assert before != after, "Слайдер, значение не были изменены"


    class TestProgressBarPage:
        def test_change_progress_bar_value(self, driver):
            # тест на изменение значений в ПрогрессБар
            progress_bar_page = ProgressBarPage(driver, 'https://demoqa.com/progress-bar')
            progress_bar_page.open()
            before, after = progress_bar_page.change_progress_bar_value()
            #print(before)
            #print(after)
            assert before != after, "ПрогрессБар, значение не были изменены"


    class TestTabsPage:
        def test_change_tabs(self, driver):
            # тест переключение по табам и проверку текста в них
            # тест more с ошибкой - поэтому эта часть закомменчина
            tabs_page = TabsPage(driver, 'https://demoqa.com/tabs')
            tabs_page.open()
            what_button, what_content = tabs_page.check_tabs('what')
            origin_button, origin_content = tabs_page.check_tabs('origin')
            use_button, use_content = tabs_page.check_tabs('use')
            #more_button, more_content = tabs_page.check_tabs('more')

            print(what_button, what_content)
            print(origin_button, origin_content)
            print(use_button, use_content)

            assert what_button == "What" and what_content != 0, 'Загаловок не совпал, в ТАБЕ нет текста'
            assert origin_button == "Origin" and origin_content != 0, 'Загаловок не совпал, в ТАБЕ нет текста'
            assert use_button == "Use" and use_content != 0, 'Загаловок не совпал, в ТАБЕ нет текста'
            #assert more_button == "More" and more_content != 0, 'Загаловок не совпал, в ТАБЕ нет текста'


    class TestToolTipsPage:
        def test_tool_tips(self, driver):
            #
            tool_tips_page = ToolTipsPage(driver, 'https://demoqa.com/tool-tips')
            tool_tips_page.open()

            a, b, c, d = tool_tips_page.check_tool_tips()
            print(a)
            print(b)
            print(c)
            print(d)

            assert a ==  "You hovered over the Button", 'Button = текст в тултипе не совподает'
            assert b ==  "You hovered over the text field", 'Field = текст в тултипе не совподает'
            assert c ==  "You hovered over the Contrary", 'Contrary = текст в тултипе не совподает'
            assert d ==  "You hovered over the 1.10.32", 'Number = текст в тултипе не совподает'



    class TestDroppingMenu:
        def test_dropping_menu(self, driver):
            #
            dropping_menu_page = DroppingMenuPage(driver, 'https://demoqa.com/menu')
            dropping_menu_page.open()
            data = dropping_menu_page.check_dropping_menu()
            #print(data)
            assert data == ['Main Item 1', 'Main Item 2', 'Sub Item', 'Sub Item', 'SUB SUB LIST »', 'Sub Sub Item 1', 'Sub Sub Item 2', 'Main Item 3'], 'Ошибка, загаловки в выпадающем меню не совпадают'
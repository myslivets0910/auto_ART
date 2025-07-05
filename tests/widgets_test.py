import time


from pages.widgets_page import AccordianPage, AutoCompletePage, DatePickerPage


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



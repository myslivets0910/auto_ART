# прописваем тесты только здесь


import time

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage


class TestElements: # основной класс для наших тестов
    class TestTextBox: # класс которые который отвечает за проверку полей на https://demoqa.com/text-box
        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, "https://demoqa.com/text-box")
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_cur_addr, output_per_addr = text_box_page.check_filled_form()

            assert full_name == output_name, "the full name does not match"
            assert email == output_email, "the email does not match"
            assert current_address == output_cur_addr,  "the current_address does not match"
            assert permanent_address == output_per_addr,  "the permanent_address does not match"
            #сравниваем данные которые ввели и которые отобразились в таблице

    class TestChechBox: # класс в котором проводятс проверки на странице ЧЕКБОКСОВ
        def test_check_box(self, driver):
            check_box_page = CheckBoxPage(driver,"https://demoqa.com/checkbox")
            check_box_page.open() #открыли страницу
            check_box_page.open_full_list() #раскрыли все чекбоксы
            check_box_page.click_random_checkbox() #выделили рандомом чекбоксы
            input_checkbox = check_box_page.get_checked_checkboxes() #нашли названия выделеных чекбоксов
            output_result = check_box_page.get_output_result() #нашли результат выделения чекбоксов (список с выделенными чекбоксам)
            assert input_checkbox == output_result, 'checkboxes have been selected'
        # сравнили результаты


        class TestRadioButton: # класс который проводит тесты на радиокнопки
            def test_radiobutton(self, driver):
                radio_button_page = RadioButtonPage(driver, "https://demoqa.com/radio-button")
                radio_button_page.open()

                #Проверка на первую радиокнопку
                radio_button_page.click_on_the_radio_button('yes')
                output_yes = radio_button_page.get_output_result_button()
                assert output_yes == 'Yes', '"YES" have not been selected'

                # Проверка на вторую радиокнопку
                radio_button_page.click_on_the_radio_button('impressive')
                output_impressive = radio_button_page.get_output_result_button()
                assert output_impressive == 'Impressive', '"Impressive" have not been selected'

                # Проверка на третью радиокнопку (баг)
                radio_button_page.click_on_the_radio_button('no')
                output_no = radio_button_page.get_output_result_button()
                assert output_no == 'No','"No" have not been selected'




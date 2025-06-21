# прописваем тесты только здесь
import random
import time

from pages.elements_page import TextBoxPage, CheckBoxPage, RadioButtonPage, WebTablePage, ButtonsPage, LinksPage, \
    UploadDownloadPage, DynamicPropertiesPage

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

    class TestWebTable:
        # класс который проводит тесты с таблицей.
        def test_web_table_add_person(self,driver):
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            new_person = web_table_page.add_new_person()
            # создание новой персоны
            table_result = web_table_page.check_new_person_web_table()
            # проверка новой персоны в таблице
            print(new_person)
            print(table_result)
            assert new_person in table_result

        def test_search_for_a_person_in_web_table(self, driver):
            # тест на проверку персоны в таблице через поисковую строку
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            key_word = web_table_page.add_new_person()[random.randint(0,5)]
            # вводим рандомное значение персоны
            web_table_page.search_for_a_person_in_web_table(key_word)
            # ищем в таблице персону по значению
            table_result = web_table_page.check_new_person_web_table()
            # проверяем что такое значение в таблице есть
            print(key_word)
            print(table_result)

            # Проверяем, содержится ли key_word в одной из строк таблицы
            assert any(key_word in row for row in table_result), f"'{key_word}' not found in the results"

        def test_web_table_update_person_info(self,driver):
            # обновление информации о человеке
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()

            lastname = web_table_page.add_new_person()[1] #создаем нового пользователя
            web_table_page.search_for_a_person_in_web_table(lastname) # ищем пользователя в таблице по поисковой строке
            age = web_table_page.update_person_info() # изменяем данные, возраст
            table_result = web_table_page.check_new_person_web_table() # ищем пользователя в таблице
            print(age)
            print(table_result)
            assert any(age in sublist for sublist in table_result), f"{age} не найдено в таблице!"
            #Таким образом, мы используем any для проверки,
            # присутствует ли значение age в любом из подсписков table_result.
            # Если оно не будет найдено, генерируется более понятное сообщение об ошибке,
            # что может помочь вам в дальнейшем диагностировании проблемы.

        def test_web_table_delete_persons(self,driver):
            # тест на удаление персоны
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            email = web_table_page.add_new_person()[3]
            web_table_page.search_for_a_person_in_web_table(email)
            web_table_page.delete_person()
            text = web_table_page.check_deleted()
            assert text == "No rows found"

        def test_web_table_change_the_lines_page(self,driver):
            # изменение отображения кол-ва строк в таблице
            web_table_page = WebTablePage(driver, "https://demoqa.com/webtables")
            web_table_page.open()
            count = web_table_page.select_up_to_some_row()
            assert count == [5, 10, 20, 25, 50, 100],'Смена кол-ва строк в таблице отработало НЕКОРРЕКТНО'

    class TestButtonsPage:

        def test_different_click_on_the_button(self, driver):
            # тест на нажатие кнопок по очереди
            button_page = ButtonsPage(driver, "https://demoqa.com/buttons")
            button_page.open()
            double = button_page.click_on_different_button("double")
            print(double) # принты можно не оствлять, они для того что бы отсматривать результат
            assert double == 'You have done a double click', 'the double click button was not present'
            right = button_page.click_on_different_button("right")
            print(right)
            assert right == 'You have done a right click', 'the right click button was not present'
            one_click = button_page.click_on_different_button("click")
            print(one_click)
            assert one_click == 'You have done a dynamic click', 'the dynamic click button was not present'

    class TestLinksPage:
        # класс на проверку перехода по ссылкам

        def test_check_link(self,driver):
            # тест по переходу на активные ссылки
            links_page = LinksPage(driver, "https://demoqa.com/links")
            links_page.open()
            link_href, current_link = links_page.check_new_tab_simple_link()
            print(link_href, current_link)
            assert link_href == current_link, 'коммент в случае падения'


        def test_broken_link(self,driver):
            # тест по переходу на неактивные ссылки
            links_page = LinksPage(driver, "https://demoqa.com/links")
            links_page.open()
            responce_code = links_page.check_broken_link('https://demoqa.com/bad-request')
            assert responce_code == 400, 'коммент в случае падения'


class TestUploadDownloadPage:
    def test_upload_file(self, driver):
        # тест по загрузке файла и проверку, что загрузился этот файл
        upload_download_page = UploadDownloadPage(driver, "https://demoqa.com/upload-download")
        upload_download_page.open()
        file_name, result = upload_download_page.upload_file()
        assert file_name == result, 'the file has not been uploaded'

    def test_download_file(self, driver):
        # тест по переходу на активные ссылки
        upload_download_page = UploadDownloadPage(driver, "https://demoqa.com/upload-download")
        upload_download_page.open()
        check = upload_download_page.download_file()
        assert check is True, 'the file has not been downloaded'

class TestDynamicPropertiesPage:


    def test_dynamic_properties(self,driver):
        dynamic_properties_page = DynamicPropertiesPage(driver,"https://demoqa.com/dynamic-properties")
        dynamic_properties_page.open()
        color_button_defore , color_button_after = dynamic_properties_page.check_changed_of_color()
        assert color_button_defore != color_button_after , 'одинаковые цвета , упал test_dynamic_properties'

    def test_appear_button(self,driver):
        dynamic_properties_page = DynamicPropertiesPage(driver, "https://demoqa.com/dynamic-properties")
        dynamic_properties_page.open()
        appear = dynamic_properties_page.check_appear_of_button()
        assert appear is True , 'test_appear_button'

    def test_enable_button(self, driver):
        dynamic_properties_page = DynamicPropertiesPage(driver, "https://demoqa.com/dynamic-properties")
        dynamic_properties_page.open()
        enable = dynamic_properties_page.check_enable_button()
        assert enable is True, 'упал test_enable_button'






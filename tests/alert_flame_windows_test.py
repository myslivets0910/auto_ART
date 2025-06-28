import time

from pages.alert_flame_windows_page import BrowserWindowPage, AlertWindowPage, FramePage, NestedFramesPage, \
    ModalDialogsPage


class TestAlertFlameWindows:
    class TestBrowserWindow:
        def test_new_tab(self,driver):
            # тест на проверку, что по клику открывается новая вкладка
            browser_windows_new_tab_page = BrowserWindowPage(driver, "https://demoqa.com/browser-windows")
            browser_windows_new_tab_page.open()
            text_result_new_tab_page = browser_windows_new_tab_page.check_opened_new_tab()
            # time.sleep(3)
            assert text_result_new_tab_page == "This is a sample page", 'текст ошибки'


        def test_new_window(self,driver):
            # тест на проверку, что по клику открывается новое окно
            browser_windows_new_window_page = BrowserWindowPage(driver, "https://demoqa.com/browser-windows")
            browser_windows_new_window_page.open()
            text_result_new_window_page = browser_windows_new_window_page.check_opened_new_window()
            # time.sleep(3)
            assert text_result_new_window_page == "This is a sample page", 'текст ошибки'


    class TestAlertWindows:
        def test_see_alert(self, driver):
            # тест на проверку сообщения в алерте
            see_alert_page = AlertWindowPage(driver, "https://demoqa.com/alerts")
            see_alert_page.open()
            alert_text = see_alert_page.check_see_alert()
            assert alert_text == "You clicked a button", 'сообщение об ошибке '

        def test_alert_appear_5_sec(self, driver):
            # тест на проверку сообщения в алерте 5 секунд
            see_alert_page = AlertWindowPage(driver, "https://demoqa.com/alerts")
            see_alert_page.open()
            alert_text = see_alert_page.check_alert_appear_5_sec()
            assert alert_text == "This alert appeared after 5 seconds", 'сообщение об ошибке '

        def test_confirm_alert(self,driver):
            # тест на проверку сообщения в алерте c подтверждением (кнопками ОК или ОТмена)
            see_alert_page = AlertWindowPage(driver, "https://demoqa.com/alerts")
            see_alert_page.open()
            alert_text = see_alert_page.check_confirm_alert()
            print(alert_text)
            assert alert_text == "You selected Ok", 'сообщение об ошибке'

        def test_input_value_alert(self,driver):
            # тест на проверку алерта с вводом значения
            see_alert_page = AlertWindowPage(driver, "https://demoqa.com/alerts")
            see_alert_page.open()
            text, alert_text = see_alert_page.check_input_value_alert()
            #print(text)
            #print(alert_text)
            assert alert_text == f"You entered {text}", 'сообщение об ошибке' # один вариант
            # или что данные текст содержится в ответе
            #assert text in alert_text, 'сообщение об ошибке'


    class TestFrame:
        def test_frames(self, driver):
            # тест на проверку сообщения в фраме
            frame_page = FramePage(driver, "https://demoqa.com/frames")
            frame_page.open()
            result_1 = frame_page.check_frame('frame1')
            result_2 = frame_page.check_frame('frame2')
            assert result_1 == ['This is a sample page', '500px', '350px'], 'сообщение об ошибке'
            assert result_2 == ['This is a sample page', '100px', '100px'], 'сообщение об ошибке'


    class TestNestedFrames:
        def test_nested_frames(self, driver):
            # тест на проверку сообщения в вложенные фреймы
            nested_frames_page = NestedFramesPage(driver, "https://demoqa.com/nestedframes")
            nested_frames_page.open()
            parent_text, child_text = nested_frames_page.check_nested_frame()
            #print(parent_text)
            #print(child_text)
            assert parent_text == 'Parent frame', "сообщение от ошибке"
            assert child_text == 'Child Iframe', "сообщение от ошибке"


    class TestModalDialogs:

        def test_modal_dialogs(self, driver):
            # теста на проверку модальных окон
            modal_dialogs_page = ModalDialogsPage(driver, "https://demoqa.com/modal-dialogs")
            modal_dialogs_page.open()
            small, large = modal_dialogs_page.check_modal_dialogs()

            assert small[1] < large[1] # на отличие кол-ва символов в текстах
            assert small[0] == 'Small Modal' , "сообщение от ошибке" # 2 = на соответствие текста в загаловке
            assert large[0] == 'Large Modal' , "сообщение от ошибке" # 3 = на соответствие текста в загаловке



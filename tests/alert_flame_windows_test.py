import time

from pages.alert_flame_windows_page import BrowserWindowPage, AlertWindowPage


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
        def test_see_alert(self,driver):
            # тест на проверку соjбения в алерте
            see_alert_page = AlertWindowPage(driver, "https://demoqa.com/alerts")
            see_alert_page.open()
            alert_text = see_alert_page.check_see_alert()
            assert alert_text == "You clicked a button", 'сообщение об ошибке '



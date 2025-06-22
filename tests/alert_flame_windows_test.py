import time

from pages.alert_flame_windows_page import BrowserWindowPage


class TestAlertFlameWindows:
    class TestBrowserWindow:
        def test_new_tab(self,driver):
            # тест на проверку, что по клику открывается новая вкладка
            new_tab_page = BrowserWindowPage(driver, "https://demoqa.com/browser-windows")
            new_tab_page.open()
            text_result_new_tab_page = new_tab_page.check_opened_new_tab()
            time.sleep(3)
            assert text_result_new_tab_page == "This is a sample page" , 'текст ошибки'


        def test_new_window(self,driver):
            # тест на проверку, что по клику открывается новая вкладка
            new_window_page = BrowserWindowPage(driver, "https://demoqa.com/browser-windows")
            new_window_page.open()
            text_result_new_window_page = new_window_page.check_opened_new_window()
            # time.sleep(3)

            assert text_result_new_window_page == "This is a sample page    ", 'текст ошибки'




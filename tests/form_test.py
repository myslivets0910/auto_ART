import random
import time

from pages.form_page import PracticeFormPage




class TestForm:
    class TestPracticeFormPage:

        def test_practice_form_filling(self, driver):
            practice_form_page = PracticeFormPage(driver, "https://demoqa.com/automation-practice-form")
            practice_form_page.open()
            p = practice_form_page.fill_form_fields()
            result = practice_form_page.form_result()

            # принты нужны для сверки результатов, для теста их можно не оставлять
            print(p.firstname, p.lastname, p.email)
            print(result[0], result[1])

            assert [p.firstname + " " + p.lastname, p.email] == [result[0], result[1]]

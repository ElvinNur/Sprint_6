import pytest
import allure
from pages.main_page import MainPage

@pytest.mark.parametrize('question_key, answer_key', [
    ('question_1', 'answer_1'),
    ('question_2', 'answer_2'),
    ('question_3', 'answer_3'),
    ('question_4', 'answer_4'),
    ('question_5', 'answer_5'),
    ('question_6', 'answer_6'),
    ('question_7', 'answer_7'),
    ('question_8', 'answer_8'),
])
@allure.title("Проверка раздела - Вопросы о важном")
def test_faq_question(driver, question_key, answer_key):
    main_page = MainPage(driver)
    main_page.open('https://qa-scooter.praktikum-services.ru/')
    main_page.scroll_to_faq_section()
    main_page.expand_question(question_key)
    assert main_page.is_answer_displayed(answer_key), f"Ответ на {question_key} не отображается"
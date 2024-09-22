from .base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class MainPage(BasePage):
    def scroll_to_faq_section(self):
        faq_section = self.driver.find_element(*MainPageLocators.FAQ_SECTION)
        self.driver.execute_script("arguments[0].scrollIntoView();", faq_section)

    def expand_question(self, question_key):
        question_locator = MainPageLocators.QUESTIONS[question_key]
        # Ожидание, пока элемент станет кликабельным
        question_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(question_locator))
        # Прокрутка к элементу вопроса
        self.driver.execute_script("arguments[0].scrollIntoView(true);", question_element)
        # Небольшая задержка для стабильности (опционально)
        # time.sleep(0.5)
        # Клик по элементу
        question_element.click()

    def is_answer_displayed(self, answer_key):
        answer_locator = MainPageLocators.ANSWERS[answer_key]
        try:
            answer_element = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(answer_locator))
            return answer_element.is_displayed() and answer_element.size['height'] > 0
        except:
            return False
        
    def click_order_button_top(self):
        self.driver.find_element(*MainPageLocators.ORDER_BUTTON_TOP).click()

    def click_order_button_bottom(self):
        time.sleep(0.5)
        order_button = self.driver.find_element(*MainPageLocators.ORDER_BUTTON_BOTTOM)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", order_button)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(MainPageLocators.ORDER_BUTTON_BOTTOM)).click()

    def click_scooter_logo(self):
        self.driver.find_element(*MainPageLocators.SCOOTER_LOGO).click()

    def click_yandex_logo(self):
        self.driver.find_element(*MainPageLocators.YANDEX_LOGO).click()
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import allure

class MainPage(BasePage):
    @allure.step("Прокрутить страницу до раздела FAQ")
    def scroll_to_faq_section(self):
        faq_section = self.find_element(MainPageLocators.FAQ_SECTION)
        self.execute_script("arguments[0].scrollIntoView();", faq_section)

    @allure.step("Развернуть вопрос: {question_key}")
    def expand_question(self, question_key):
        question_locator = MainPageLocators.QUESTIONS[question_key]
        question_element = self.wait_for_element_to_be_clickable(question_locator)
        self.execute_script("arguments[0].scrollIntoView(true);", question_element)
        self.click_element(question_locator)

    @allure.step("Проверить, что ответ отображается: {answer_key}")
    def is_answer_displayed(self, answer_key):
        answer_locator = MainPageLocators.ANSWERS[answer_key]
        try:
            answer_element = self.find_element(answer_locator)
            return answer_element.is_displayed() and answer_element.size['height'] > 0
        except TimeoutException:
            return False
        
    @allure.step("Нажать на верхнюю кнопку 'Заказать'")
    def click_order_button_top(self):
        self.click_element(MainPageLocators.ORDER_BUTTON_TOP)

    @allure.step("Нажать нижнюю кнопку 'Заказать'")
    def click_order_button_bottom(self):
        order_button = self.find_element(MainPageLocators.ORDER_BUTTON_BOTTOM)
        self.execute_script("arguments[0].scrollIntoView(true);", order_button)
        self.wait_for_element_to_be_clickable(MainPageLocators.ORDER_BUTTON_BOTTOM)
        order_button.click()

    @allure.step("Кликнуть по логотипу Самоката")
    def click_scooter_logo(self):
        self.click_element(MainPageLocators.SCOOTER_LOGO)

    @allure.step("Кликнуть по логотипу Яндекса")
    def click_yandex_logo(self):
        self.click_element(MainPageLocators.YANDEX_LOGO)

    @allure.step("Переключиться на новую вкладку")
    def switch_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step("Проверить, что текущий URL равен '{expected_url}'")
    def verify_current_url(self, expected_url):
        actual_url = self.driver.current_url
        assert actual_url == expected_url, f"Ожидали URL '{expected_url}', но получили '{actual_url}'"

    @allure.step("Проверить, что текущий URL содержит '{url_fragment}'")
    def verify_current_url_contains(self, url_fragment):
        try:
            WebDriverWait(self.driver, self.timeout).until(
                EC.url_contains(url_fragment))
        except TimeoutException:
            self.attach_screenshot(f"Текущий URL не содержит '{url_fragment}'")
            raise AssertionError(f"Текущий URL не содержит '{url_fragment}'")
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 10

    @allure.step("Открыть страницу по URL: {url}")
    def open(self, url):
        self.driver.get(url)
        
    @allure.step("Найти элемент: {locator}")
    def find_element(self, locator):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_element_located(locator)
            )
        except TimeoutException:
            allure.attach(self.driver.get_screenshot_as_png(), name="Скриншот при ошибке", attachment_type=allure.attachment_type.PNG)
            raise
        
    @allure.step("Найти элементы: {locator}")
    def find_elements(self, locator):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.visibility_of_all_elements_located(locator)
            )
        except TimeoutException:
            allure.attach(self.driver.get_screenshot_as_png(), name="Скриншот при ошибке", attachment_type=allure.attachment_type.PNG)
            raise
        
    @allure.step("Кликнуть по элементу: {locator}")
    def click_element(self, locator):
        element = self.find_element(locator)
        element.click()

    @allure.step("Ввести текст '{text}' в элемент: {locator}")
    def send_keys(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Выполнить JavaScript скрипт")
    def execute_script(self, script, *args):
        self.driver.execute_script(script, *args)
        
    @allure.step("Прокрутить страницу до элемента")
    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.execute_script("arguments[0].scrollIntoView();", element)
        
    @allure.step("Ожидать, пока элемент станет кликабельным: {locator}")
    def wait_for_element_to_be_clickable(self, locator):
        try:
            return WebDriverWait(self.driver, self.timeout).until(
                EC.element_to_be_clickable(locator)
            )
        except TimeoutException:
            self.attach_screenshot("Элемент не кликабелен: {}".format(locator))
            raise
        
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
        
    def attach_screenshot(self, name):
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name=name,
            attachment_type=allure.attachment_type.PNG)
        
    
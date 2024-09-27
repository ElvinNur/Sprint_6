import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from selenium.webdriver.support.ui import WebDriverWait
from data.test_order_data import test_data_top, test_data_bottom


@allure.epic("Оформление заказа")
class TestOrderFlow:
    @allure.title("Проверка оформления заказа через верхнюю кнопку 'Заказать'")
    @allure.description("Тест проверяет, что пользователь может оформить заказ через верхнюю кнопку 'Заказать'")
    def test_order_flow_top_button(self, driver):
        data = test_data_top  # Данные для верхней кнопки
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.open('https://qa-scooter.praktikum-services.ru/')
        main_page.click_order_button_top()
        # Далее шаги по заполнению формы и проверке результата
        order_page.fill_order_form_step1(
            data['first_name'], data['last_name'], data['address'],
            data['metro_station'], data['phone_number']
        )
        order_page.fill_order_form_step2(
            data['delivery_date'], data['rental_period'], data['scooter_color'], data['comment']
        )
        assert order_page.is_order_successful(), "Заказ не был успешно оформлен"
        
    @allure.title("Проверка оформления заказа через нижнюю кнопку 'Заказать'")
    @allure.description("Тест проверяет, что пользователь может оформить заказ через нижнюю кнопку 'Заказать'")
    def test_order_flow_bottom_button(self, driver):
        data = test_data_bottom  # Данные для нижней кнопки
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.open('https://qa-scooter.praktikum-services.ru/')
        main_page.click_order_button_bottom()
        # Далее шаги по заполнению формы и проверке результата
        order_page.fill_order_form_step1(
            data['first_name'], data['last_name'], data['address'],
            data['metro_station'], data['phone_number']
        )
        order_page.fill_order_form_step2(
            data['delivery_date'], data['rental_period'], data['scooter_color'], data['comment']
        )
        assert order_page.is_order_successful(), "Заказ не был успешно оформлен"


@allure.epic("Проверка редиректов")
class TestRedirects:        
    @allure.title("Проверка редиректа - Самокат")
    def test_scooter_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.open('https://qa-scooter.praktikum-services.ru/order')
        main_page.click_scooter_logo()
        main_page.verify_current_url('https://qa-scooter.praktikum-services.ru/')
        
    @allure.title("Проверка редиректа - Яндекс")
    def test_yandex_logo_redirect(self, driver):
        main_page = MainPage(driver)
        main_page.open('https://qa-scooter.praktikum-services.ru/order')
        main_page.click_yandex_logo()
        # Переключаемся на новую вкладку
        main_page.switch_to_new_tab()
        # Ждём редиректа
        main_page.verify_current_url_contains('dzen.ru')
        
        
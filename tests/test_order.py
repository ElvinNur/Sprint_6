import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from selenium.webdriver.support.ui import WebDriverWait
from data.test_order_data import test_data


@allure.epic("Оформление заказа")
class TestOrderFlow:
    @allure.title("Проверка оформления заказа")
    @allure.description("Тест проверяет, что пользователь может оформить заказ с различными параметрами")
    @pytest.mark.parametrize('data', test_data)
    def test_order_flow(self, driver, data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.open('https://qa-scooter.praktikum-services.ru/')

        # Нажимаем кнопку «Заказать» (верхнюю или нижнюю)
        with allure.step(f"Нажать кнопку 'Заказать' ({data['order_button']})"):
            if data['order_button'] == 'top':
                main_page.click_order_button_top()
            else:
                main_page.click_order_button_bottom()

        # Заполняем форму заказа - Шаг 1
        order_page.fill_order_form_step1(
            data['first_name'], data['last_name'], data['address'],
            data['metro_station'], data['phone_number'])

        # Заполняем форму заказа - Шаг 2
        order_page.fill_order_form_step2(
            data['delivery_date'], data['rental_period'], data['scooter_color'], data['comment'])

        # Проверяем успешность оформления заказа
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
        
        
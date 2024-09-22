import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from selenium.webdriver.support.ui import WebDriverWait
import time
from datetime import datetime, timedelta

# Функция для получения даты в формате дд.мм.гггг
def get_future_date(days):
    future_date = datetime.now() + timedelta(days=days)
    return future_date.strftime('%d.%m.%Y')

test_data = [
    {
        'first_name': 'Алексей',
        'last_name': 'Смирнов',
        'address': 'ул. Ленина, д. 10',
        'metro_station': 'Черкизовская',
        'phone_number': '+79005551111',
        'delivery_date': get_future_date(1),  # Завтрашняя дата
        'rental_period': 'трое суток',
        'scooter_color': 'чёрный',
        'comment': 'Доставить утром',
        'order_button': 'top'
    },
    {
        'first_name': 'Екатерина',
        'last_name': 'Васильева',
        'address': 'пр. Мира, д. 5',
        'metro_station': 'Преображенская площадь',
        'phone_number': '+79007772222',
        'delivery_date': get_future_date(2),  # Послезавтрашняя дата
        'rental_period': 'сутки',
        'scooter_color': 'серый',
        'comment': 'Позвонить за 30 минут',
        'order_button': 'bottom'
    }
]

@allure.title("Проверка оформления заказа")
@allure.description("Тест проверяет, что пользователь может оформить заказ с различными параметрами")
@pytest.mark.parametrize('data', test_data)
def test_order_flow(driver, data):
    with allure.step("Открыть главную страницу"):
        main_page = MainPage(driver)
        main_page.open('https://qa-scooter.praktikum-services.ru/')
    
    with allure.step(f"Нажать кнопку 'Заказать' ({data['order_button']})"):
        if data['order_button'] == 'top':
            main_page.click_order_button_top()
        else:
            main_page.click_order_button_bottom()
    
    with allure.step("Заполнить форму заказа - Шаг 1"):
        order_page = OrderPage(driver)
        order_page.fill_order_form_step1(
            data['first_name'], data['last_name'], data['address'],
            data['metro_station'], data['phone_number'])
        
    with allure.step("Заполнить форму заказа - Шаг 2"):
        order_page.fill_order_form_step2(
            data['delivery_date'], data['rental_period'], data['scooter_color'], data['comment'])
    
    with allure.step("Проверить успешность оформления заказа"):
        assert order_page.is_order_successful(), "Заказ не был успешно оформлен"
        
@allure.title("Проверка редиректа - Самокат")
def test_scooter_logo_redirect(driver):
    main_page = MainPage(driver)
    main_page.open('https://qa-scooter.praktikum-services.ru/order')
    main_page.click_scooter_logo()
    assert driver.current_url == 'https://qa-scooter.praktikum-services.ru/', "Переход по логотипу «Самокат» не привёл на главную страницу"

@allure.title("Проверка редиректа - Яндекс")
def test_yandex_logo_redirect(driver):
    main_page = MainPage(driver)
    main_page.open('https://qa-scooter.praktikum-services.ru/order')
    main_page.click_yandex_logo()
    # Переключаемся на новую вкладку
    driver.switch_to.window(driver.window_handles[1])
    # Ждём редиректа
    WebDriverWait(driver, 10).until(lambda d: 'dzen.ru' in d.current_url)
    assert 'dzen.ru' in driver.current_url, "Переход по логотипу Яндекса не привёл на главную страницу Дзена"
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import allure

class OrderPage(BasePage):
    @allure.step("Заполнить форму заказа - Шаг 1")
    def fill_order_form_step1(self, first_name, last_name, address, metro_station, phone_number):
        self.send_keys(OrderPageLocators.FIRST_NAME_INPUT, first_name)
        
        self.send_keys(OrderPageLocators.LAST_NAME_INPUT, last_name)

        self.send_keys(OrderPageLocators.ADDRESS_INPUT, address)
        
        self.click_element(OrderPageLocators.METRO_STATION_INPUT)
        metro_options = self.find_elements(OrderPageLocators.METRO_STATION_LIST)
        for option in metro_options:
            if option.text == metro_station:
                option.click()
                break
        
        self.send_keys(OrderPageLocators.PHONE_NUMBER_INPUT, phone_number)
        
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнить форму заказа - Шаг 2")
    def fill_order_form_step2(self, delivery_date, rental_period, scooter_color, comment):
        self.send_keys(OrderPageLocators.DELIVERY_DATE_INPUT, delivery_date)
        
        self.send_keys(OrderPageLocators.DELIVERY_DATE_INPUT, Keys.ENTER)
        
        self.click_element(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        
        rental_options = self.find_elements(OrderPageLocators.RENTAL_PERIOD_OPTIONS)
        for option in rental_options:
            if option.text.strip() == rental_period:
                option.click()
                break
        
        # Выбор цвета самоката
        if 'чёрный' in scooter_color.lower():
            self.click_element(OrderPageLocators.SCOOTER_COLOR_CHECKBOX_BLACK)
        if 'серый' in scooter_color.lower():
            self.click_element(OrderPageLocators.SCOOTER_COLOR_CHECKBOX_GREY)
        
        # Ввод комментария
        self.send_keys(OrderPageLocators.COMMENT_INPUT, comment)
        
        # Нажать «Заказать» и подтвердить
        self.click_element(OrderPageLocators.ORDER_BUTTON)
        
        # Ждём появления кнопки подтверждения
        self.click_element(OrderPageLocators.CONFIRM_ORDER_BUTTON)
        
    @allure.step("Проверить успешность оформления заказа")
    def is_order_successful(self):
        try:
            success_modal = self.find_element(OrderPageLocators.ORDER_SUCCESS_MODAL)
            return 'Заказ оформлен' in success_modal.text
        except TimeoutException:
            return False


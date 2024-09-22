from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class OrderPage(BasePage):
    def fill_order_form_step1(self, first_name, last_name, address, metro_station, phone_number):
        self.driver.find_element(*OrderPageLocators.FIRST_NAME_INPUT).send_keys(first_name)
        self.driver.find_element(*OrderPageLocators.LAST_NAME_INPUT).send_keys(last_name)
        self.driver.find_element(*OrderPageLocators.ADDRESS_INPUT).send_keys(address)
        
        # Выбор станции метро
        self.driver.find_element(*OrderPageLocators.METRO_STATION_INPUT).click()
        # Используем явное ожидание для загрузки списка станций
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_all_elements_located(OrderPageLocators.METRO_STATION_LIST)
        )
        metro_options = self.driver.find_elements(*OrderPageLocators.METRO_STATION_LIST)
        for option in metro_options:
            if option.text == metro_station:
                option.click()
                break
        
        self.driver.find_element(*OrderPageLocators.PHONE_NUMBER_INPUT).send_keys(phone_number)
        self.driver.find_element(*OrderPageLocators.NEXT_BUTTON).click()

    def fill_order_form_step2(self, delivery_date, rental_period, scooter_color, comment):
        # Ввод даты доставки в формате дд.мм.гггг
        date_input = self.driver.find_element(*OrderPageLocators.DELIVERY_DATE_INPUT)
        date_input.click()
        date_input.send_keys(delivery_date)
        date_input.send_keys(Keys.ENTER)

        # Выбор срока аренды
        self.driver.find_element(*OrderPageLocators.RENTAL_PERIOD_DROPDOWN).click()
        rental_options = self.driver.find_elements(*OrderPageLocators.RENTAL_PERIOD_OPTIONS)
        for option in rental_options:
            if option.text.strip() == rental_period:
                option.click()
                break
        
        # Выбор цвета самоката
        if 'чёрный' in scooter_color.lower():
            self.driver.find_element(*OrderPageLocators.SCOOTER_COLOR_CHECKBOX_BLACK).click()
        if 'серый' in scooter_color.lower():
            self.driver.find_element(*OrderPageLocators.SCOOTER_COLOR_CHECKBOX_GREY).click()
        
        # Ввод комментария
        self.driver.find_element(*OrderPageLocators.COMMENT_INPUT).send_keys(comment)
        
        # Нажать «Заказать» и подтвердить
        self.driver.find_element(*OrderPageLocators.ORDER_BUTTON).click()
        # Ждём появления кнопки подтверждения
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(OrderPageLocators.CONFIRM_ORDER_BUTTON)
        ).click()
        
    def is_order_successful(self):
        try:
            modal_header = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(OrderPageLocators.ORDER_SUCCESS_MODAL)
            )
            return 'Заказ оформлен' in modal_header.text
        except:
            return False
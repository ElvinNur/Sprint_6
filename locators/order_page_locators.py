from selenium.webdriver.common.by import By

class OrderPageLocators:
    # Поля формы заказа — Шаг 1
    FIRST_NAME_INPUT = (By.XPATH, '//input[@placeholder="* Имя"]')
    LAST_NAME_INPUT = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    ADDRESS_INPUT = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    METRO_STATION_INPUT = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    METRO_STATION_LIST = (By.XPATH, '//div[contains(@class, "Order_Text")]')  # Элементы списка метро
    PHONE_NUMBER_INPUT = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    NEXT_BUTTON = (By.XPATH, '//button[contains(@class, "Button_Middle") and text()="Далее"]')

    # Поля формы заказа — Шаг 2
    DELIVERY_DATE_INPUT = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    RENTAL_PERIOD_DROPDOWN = (By.CLASS_NAME, 'Dropdown-placeholder')
    RENTAL_PERIOD_OPTIONS = (By.CLASS_NAME, 'Dropdown-option')
    SCOOTER_COLOR_CHECKBOX_BLACK = (By.ID, 'black')
    SCOOTER_COLOR_CHECKBOX_GREY = (By.ID, 'grey')
    COMMENT_INPUT = (By.XPATH, '//input[@placeholder="Комментарий для курьера"]')
    ORDER_BUTTON = (By.XPATH, '//button[contains(@class, "Button_Middle") and text()="Заказать"]')
    CONFIRM_ORDER_BUTTON = (By.XPATH, '//button[text()="Да"]')
    ORDER_SUCCESS_MODAL = (By.XPATH, '//div[contains(@class, "Order_Modal")]')
    
from selenium.webdriver.common.by import By

class MainPageLocators:
    # Локатор раздела «Вопросы о важном»
    FAQ_SECTION = (By.XPATH, '//div[contains(@class, "Home_FourPart") and contains(@style, "opacity: 1")]')
    
    # Локаторы вопросов и ответов
    QUESTIONS = {
        'question_1': (By.XPATH, '//div[contains(@id, "accordion__heading-0") and contains(@class, "accordion__button")]'),
        'question_2': (By.XPATH, '//div[contains(@id, "accordion__heading-1") and contains(@class, "accordion__button")]'),
        'question_3': (By.XPATH, '//div[contains(@id, "accordion__heading-2") and contains(@class, "accordion__button")]'),
        'question_4': (By.XPATH, '//div[contains(@id, "accordion__heading-3") and contains(@class, "accordion__button")]'),
        'question_5': (By.XPATH, '//div[contains(@id, "accordion__heading-4") and contains(@class, "accordion__button")]'),
        'question_6': (By.XPATH, '//div[contains(@id, "accordion__heading-5") and contains(@class, "accordion__button")]'),
        'question_7': (By.XPATH, '//div[contains(@id, "accordion__heading-6") and contains(@class, "accordion__button")]'),
        'question_8': (By.XPATH, '//div[contains(@id, "accordion__heading-7") and contains(@class, "accordion__button")]'),
    }
    ANSWERS = {
        'answer_1': (By.XPATH, '//*[@id="accordion__panel-0"]'),
        'answer_2': (By.XPATH, '//*[@id="accordion__panel-1"]'),
        'answer_3': (By.XPATH, '//*[@id="accordion__panel-2"]'),
        'answer_4': (By.XPATH, '//*[@id="accordion__panel-3"]'),
        'answer_5': (By.XPATH, '//*[@id="accordion__panel-4"]'),
        'answer_6': (By.XPATH, '//*[@id="accordion__panel-5"]'),
        'answer_7': (By.XPATH, '//*[@id="accordion__panel-6"]'),
        'answer_8': (By.XPATH, '//*[@id="accordion__panel-7"]'),
    }
    
     # Локаторы кнопок «Заказать» на главной странице
    ORDER_BUTTON_TOP = (By.XPATH, '//button[contains(@class, "Button_Button") and text()="Заказать"]')
    ORDER_BUTTON_BOTTOM = (By.XPATH, '(//button[contains(@class, "Button_Button") and text()="Заказать"])[2]') #(By.XPATH, '//button[contains(@class, "Button_Middle") and text()="Заказать"]')
    
    # Логотипы
    YANDEX_LOGO = (By.XPATH, '//img [@src="/assets/ya.svg" and @alt="Yandex"]') 
    SCOOTER_LOGO = (By.XPATH, '//img [@src="/assets/scooter.svg" and @alt="Scooter"]')
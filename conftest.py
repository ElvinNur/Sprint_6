import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions

@pytest.fixture(scope="function")
def driver():
    options = FirefoxOptions()
    # Устанавливаем уровень масштабирования на 80%
    options.set_preference("layout.css.devPixelsPerPx", "0.8")
    # Устанавливаем размеры окна (опционально)
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    # Если хотите запустить браузер в безголовом режиме (без UI), раскомментируйте следующую строку
    # options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()
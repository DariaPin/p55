import pytest
from selenium import webdriver

@pytest.fixture
def chrome():
    driver = webdriver.Chrome()
    driver.get('https://qa-desk.stand.praktikum-services.ru/')
    yield driver
    driver.quit()
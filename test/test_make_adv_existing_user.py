import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators_all.locators import DoskaLocators
from project_source.helpers import get_sign_up_data
from project_source.data import existing_user_data
from project_source.data import get_sign_up_data_existing_user
from project_source.helpers import get_price
from project_source.helpers import get_text
from project_source.helpers import get_name

class TestMakeAddExistingUser:

    def test_make_adv_existing_user(self, chrome):

        adv_price = get_price()
        adv_text = get_text()
        adv_name = get_name()
        chrome.find_element(*DoskaLocators. LOGIN_AND_REGISTRATION_BUTTON).click()
        email_data, password_data = get_sign_up_data_existing_user()
        chrome.find_element(*DoskaLocators.EMAIL_FIELD).send_keys(email_data)
        chrome.find_element(*DoskaLocators.PASSWORD_FIELD).send_keys(password_data)
        chrome.find_element(*DoskaLocators.ENTER).click()

        time.sleep(3)

        adv = WebDriverWait(chrome, 5).until(expected_conditions.presence_of_element_located(DoskaLocators.REKLAMA))
        assert adv.is_displayed() is True, "ADV is not displayed"
        chrome.find_element(*DoskaLocators.REKLAMA).click()

        chrome.find_element(*DoskaLocators.NAME_ADV).send_keys(adv_name)
        chrome.find_element(*DoskaLocators.PRICE).send_keys(adv_price)
        chrome.find_element(*DoskaLocators.TEXT_AREA).send_keys(adv_text)

        chrome.find_element(*DoskaLocators.PUBLISH).click()
        chrome.find_element(*DoskaLocators.AVATAR).click()
        my_adv = chrome.find_element(*DoskaLocators.MY_ADV)
        assert my_adv.is_displayed() is True, "ADD not displayed"








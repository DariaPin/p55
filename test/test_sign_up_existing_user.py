import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators_all.locators import DoskaLocators
from project_source.helpers import get_sign_up_data
from project_source.data import existing_user_data
from project_source.data import existing_user_data_email


class TestSignUpExistingUser:

    def test_sign_up_existing_user(self, chrome):
        chrome.find_element(*DoskaLocators.LOGIN_BUTTON).click()
        chrome.find_element(*DoskaLocators.ACCOUNT_NOT_EXIST_BUTTON).click()

        chrome.find_element(*DoskaLocators.EMAIL_FIELD).send_keys(existing_user_data_email())
        chrome.find_element(*DoskaLocators.PASSWORD_FIELD).send_keys(existing_user_data())
        chrome.find_element(*DoskaLocators.PASSWORD_FIELD_REPEAT).send_keys(existing_user_data())

        chrome.find_element(*DoskaLocators.CREATE_ACCOUNT).click()
        error_message = WebDriverWait(chrome, 5).until(expected_conditions.presence_of_element_located(DoskaLocators.MISTAKE))
        assert error_message.is_displayed() is True, "Avatar is not displayed"

        email_field_error = WebDriverWait(chrome, 5).until(expected_conditions.presence_of_element_located(DoskaLocators.BOARDER_ERROR_EMAIL))
        assert email_field_error.is_displayed() is True, "User is not displayed"
        border_color = email_field_error.value_of_css_property('border-color')
        assert border_color == "rgb(255, 105, 114)"
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators_all.locators import DoskaLocators
from project_source.helpers import get_sign_up_data
from project_source.data import existing_user_data

class TestSignUp1:

    def test_sign_up(self, chrome):
        email_data = get_sign_up_data()
        chrome.find_element(*DoskaLocators.LOGIN_BUTTON).click()
        chrome.find_element(*DoskaLocators.ACCOUNT_NOT_EXIST_BUTTON).click()
        chrome.find_element(*DoskaLocators.EMAIL_FIELD).send_keys(email_data)
        chrome.find_element(*DoskaLocators.PASSWORD_FIELD).send_keys(existing_user_data())
        chrome.find_element(*DoskaLocators.PASSWORD_FIELD_REPEAT).send_keys(existing_user_data())
        chrome.find_element(*DoskaLocators.CREATE_ACCOUNT).click()
        avatar = WebDriverWait(chrome, 5).until(expected_conditions.presence_of_element_located(DoskaLocators.AVATAR))
        assert avatar.is_displayed() is True, "Avatar is not displayed"
        user = WebDriverWait(chrome, 5).until(expected_conditions.presence_of_element_located(DoskaLocators.USER))
        assert user.is_displayed() is True, "User is not displayed "
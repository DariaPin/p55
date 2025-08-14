import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators_all.locators import DoskaLocators
from project_source.helpers import get_sign_up_data
from project_source.data import existing_user_data
from project_source.data import get_sign_up_data_existing_user
from constance_all.constance import Const

class TestLogout:

    def test_logout(self, chrome):
        chrome.find_element(*DoskaLocators. LOGIN_AND_REGISTRATION_BUTTON).click()
        chrome.find_element(*DoskaLocators.EMAIL_FIELD).send_keys(Const.EMAILDATA)
        chrome.find_element(*DoskaLocators.PASSWORD_FIELD).send_keys(Const.PASSWORDDATA)
        chrome.find_element(*DoskaLocators.ENTER).click()

        exit = WebDriverWait(chrome, 5).until(expected_conditions.presence_of_element_located(DoskaLocators.EXIT))
        exit.click()
        sign_in_and_registration = WebDriverWait(chrome, 10).until(expected_conditions.presence_of_element_located(DoskaLocators.LOGIN_AND_REGISTRATION_BUTTON))
        assert sign_in_and_registration.is_displayed() is True, "Sign in and registration Button is not displayed"
        avatar = WebDriverWait(chrome, 5).until(expected_conditions.invisibility_of_element(DoskaLocators.AVATAR))
        assert avatar is True, "Avatar is displayed"
        time.sleep(8)
        user = WebDriverWait(chrome, 5).until(expected_conditions.invisibility_of_element(DoskaLocators.USER))
        assert user is True, "User is displayed"
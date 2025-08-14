import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators_all.locators import DoskaLocators
from project_source.helpers import get_sign_up_data
from project_source.data import existing_user_data

class TestMakeAdd:

    def test_make_adv(self, chrome):
        chrome.find_element(*DoskaLocators.REKLAMA).click()

        modal = WebDriverWait(chrome, 5).until(expected_conditions.presence_of_element_located(DoskaLocators.MODAL))
        assert modal.is_displayed() is True, "Avatar is not displayed"

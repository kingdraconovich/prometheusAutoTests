# -*- coding: utf-8 -*-
import random
import unittest

import time
from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver
from PabeObject import page


class T02LoginTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def test_T03_01_Registration_Page_Elements_Appearance(self):
        registration_page = page.RegistrationPage(self.driver)
        registration_page.get()
        assert registration_page.is_registration_page_elements_visible()

    def test_T03_02_Registration_Page_Elements_Appearance(self):
        registration_page = page.RegistrationPage(self.driver)
        dashboard_page = page.DashboardPage(self.driver)
        registration_page.get()
        random_id = str(random.randint(1, 1000))
        registration_page.email_element = "test_email" + random_id + "@gmail.com"
        registration_page.name_element = "Test Test"
        registration_page.username_element = "autoTester" + random_id
        registration_page.password_element = "test"
        registration_page.education_element = "Бакалавр"
        registration_page.gender_element = "Чоловіча"
        registration_page.birth_year_element = "2015"
        registration_page.mailing_address_area = "Somewhere over the rainbow"
        registration_page.goals_area = "I'ma little robot to test your site"
        registration_page.click_on_terms_of_service_checkbox()
        registration_page.click_on_honor_code_checkbox()
        # registration_page.click_on_submit_button()
        self.wait.until(lambda driver: self.driver.current_url.encode('utf-8') == dashboard_page.url)
        assert (self.driver.current_url.encode(
            'utf-8') == dashboard_page.url), "User is not able to register with valid credentials"

    def tearDown(self):
        self.driver.quit()

    if __name__ == "__main__":
        unittest.main()

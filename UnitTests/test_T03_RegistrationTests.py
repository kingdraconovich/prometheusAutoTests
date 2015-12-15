# -*- coding: utf-8 -*-
import random
import unittest

import time
from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver
from PabeObject import page


class T03RegistrationTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def test_T03_01_Registration_Page_Elements_Appearance(self):
        registration_page = page.RegistrationPage(self.driver)
        registration_page.get()
        assert registration_page.is_registration_page_elements_visible()

    def test_T03_02_Registration_With_Valid_Credentials(self):
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
        # uncomment this part to proceed with registration submission. Commented to prevent junk users cloning
        '''
        registration_page.click_on_submit_button()
        self.wait.until(lambda driver: self.driver.current_url.encode('utf-8') == dashboard_page.url)
        assert (self.driver.current_url.encode(
            'utf-8') == dashboard_page.url), "User is not able to register with valid credentials"
        '''

    def test_T03_03_Registration_With_Invalid_Email(self):
        registration_page = page.RegistrationPage(self.driver)
        dashboard_page = page.DashboardPage(self.driver)
        registration_page.get()
        random_id = str(random.randint(1, 1000))
        registration_page.email_element = "test_email"
        registration_page.name_element = "Test Test"
        registration_page.username_element = "autoTester" + random_id
        registration_page.password_element = "test"
        registration_page.click_on_terms_of_service_checkbox()
        registration_page.click_on_honor_code_checkbox()
        registration_page.click_on_submit_button()
        time.sleep(1.7)
        assert registration_page.is_invalid_credentials_alert_visible()
        self.wait.until(lambda driver: self.driver.current_url.encode('utf-8') != dashboard_page.url)
        assert (self.driver.current_url.encode(
            'utf-8') != dashboard_page.url), "User is able to register with invalid email"

    def test_T03_04_Registration_With_Existing_Email(self):
        registration_page = page.RegistrationPage(self.driver)
        dashboard_page = page.DashboardPage(self.driver)
        registration_page.get()
        random_id = str(random.randint(1, 1000))
        registration_page.email_element = "vlad.belogorodskiy@gmail.com"
        registration_page.name_element = "Test Test"
        registration_page.username_element = "autoTester" + random_id
        registration_page.password_element = "test"
        registration_page.click_on_terms_of_service_checkbox()
        registration_page.click_on_honor_code_checkbox()
        registration_page.click_on_submit_button()
        time.sleep(1.7)
        assert registration_page.is_invalid_credentials_alert_visible()
        self.wait.until(lambda driver: self.driver.current_url.encode('utf-8') != dashboard_page.url)
        assert (self.driver.current_url.encode(
            'utf-8') != dashboard_page.url), "User is able to register with existing email"

    def test_T03_05_Registration_With_Invalid_Name(self):
        registration_page = page.RegistrationPage(self.driver)
        dashboard_page = page.DashboardPage(self.driver)
        registration_page.get()
        random_id = str(random.randint(1, 1000))
        registration_page.email_element = "test_email@gmail.com"
        registration_page.username_element = "autoTester" + random_id
        registration_page.password_element = "test"
        registration_page.click_on_terms_of_service_checkbox()
        registration_page.click_on_honor_code_checkbox()
        registration_page.click_on_submit_button()
        time.sleep(1.7)
        assert registration_page.is_invalid_credentials_alert_visible()
        self.wait.until(lambda driver: self.driver.current_url.encode('utf-8') != dashboard_page.url)
        assert (self.driver.current_url.encode(
            'utf-8') != dashboard_page.url), "User is able to register without entering name"

    def test_T03_06_Registration_With_Invalid_Username(self):
        registration_page = page.RegistrationPage(self.driver)
        dashboard_page = page.DashboardPage(self.driver)
        registration_page.get()
        registration_page.email_element = "test_email@gmail.com"
        registration_page.name_element = "Test Test"
        registration_page.password_element = "test"
        registration_page.click_on_terms_of_service_checkbox()
        registration_page.click_on_honor_code_checkbox()
        registration_page.click_on_submit_button()
        time.sleep(1.7)
        assert registration_page.is_invalid_credentials_alert_visible()
        self.wait.until(lambda driver: self.driver.current_url.encode('utf-8') != dashboard_page.url)
        assert (self.driver.current_url.encode(
            'utf-8') != dashboard_page.url), "User is able to register without entering username"

    def test_T03_07_Registration_With_Existing_Username(self):
        registration_page = page.RegistrationPage(self.driver)
        dashboard_page = page.DashboardPage(self.driver)
        registration_page.get()
        registration_page.email_element = "test_email@gmail.com"
        registration_page.name_element = "Test Test"
        registration_page.username_element = "autoTester"
        registration_page.password_element = "test"
        registration_page.click_on_terms_of_service_checkbox()
        registration_page.click_on_honor_code_checkbox()
        registration_page.click_on_submit_button()
        time.sleep(1.7)
        assert registration_page.is_invalid_credentials_alert_visible()
        self.wait.until(lambda driver: self.driver.current_url.encode('utf-8') != dashboard_page.url)
        assert (self.driver.current_url.encode(
            'utf-8') != dashboard_page.url), "User is able to register with existing username"

    def test_T03_08_Registration_With_Incorrect_Password(self):
        registration_page = page.RegistrationPage(self.driver)
        dashboard_page = page.DashboardPage(self.driver)
        registration_page.get()
        registration_page.email_element = "test_email@gmail.com"
        registration_page.name_element = "Test Test"
        registration_page.username_element = "autoTester"
        registration_page.password_element = "1"
        registration_page.click_on_terms_of_service_checkbox()
        registration_page.click_on_honor_code_checkbox()
        registration_page.click_on_submit_button()
        time.sleep(1.7)
        assert registration_page.is_invalid_credentials_alert_visible()
        self.wait.until(lambda driver: self.driver.current_url.encode('utf-8') != dashboard_page.url)
        assert (self.driver.current_url.encode(
            'utf-8') != dashboard_page.url), "User is able to register with incorrect password"

    def test_T03_08_Registration_Without_Entering_Password(self):
        registration_page = page.RegistrationPage(self.driver)
        dashboard_page = page.DashboardPage(self.driver)
        registration_page.get()
        registration_page.email_element = "test_email@gmail.com"
        registration_page.name_element = "Test Test"
        registration_page.username_element = "autoTester"
        registration_page.click_on_terms_of_service_checkbox()
        registration_page.click_on_honor_code_checkbox()
        registration_page.click_on_submit_button()
        time.sleep(1.7)
        assert registration_page.is_invalid_credentials_alert_visible()
        self.wait.until(lambda driver: self.driver.current_url.encode('utf-8') != dashboard_page.url)
        assert (self.driver.current_url.encode(
            'utf-8') != dashboard_page.url), "User is able to register without entering password"

    def test_T03_09_Registration_Without_Submitting_Terms_Of_Service(self):
        registration_page = page.RegistrationPage(self.driver)
        dashboard_page = page.DashboardPage(self.driver)
        registration_page.get()
        registration_page.email_element = "test_email@gmail.com"
        registration_page.name_element = "Test Test"
        registration_page.username_element = "autoTester"
        registration_page.password_element = "test"
        registration_page.click_on_honor_code_checkbox()
        registration_page.click_on_submit_button()
        time.sleep(1.7)
        assert registration_page.is_invalid_credentials_alert_visible()
        self.wait.until(lambda driver: self.driver.current_url.encode('utf-8') != dashboard_page.url)
        assert (self.driver.current_url.encode(
            'utf-8') != dashboard_page.url), "User is able to register without submitting terms of service"

    def test_T03_10_Registration_Without_Submitting_Honor_Code(self):
        registration_page = page.RegistrationPage(self.driver)
        dashboard_page = page.DashboardPage(self.driver)
        registration_page.get()
        registration_page.email_element = "test_email@gmail.com"
        registration_page.name_element = "Test Test"
        registration_page.username_element = "autoTester"
        registration_page.password_element = "test"
        registration_page.click_on_terms_of_service_checkbox()
        registration_page.click_on_submit_button()
        time.sleep(1.7)
        assert registration_page.is_invalid_credentials_alert_visible()
        self.wait.until(lambda driver: self.driver.current_url.encode('utf-8') != dashboard_page.url)
        assert (self.driver.current_url.encode(
            'utf-8') != dashboard_page.url), "User is able to register without submitting honor code"

    def test_T03_11_Registration_Without_Submitting_Both_Checkboxes(self):
        registration_page = page.RegistrationPage(self.driver)
        dashboard_page = page.DashboardPage(self.driver)
        registration_page.get()
        registration_page.email_element = "test_email@gmail.com"
        registration_page.name_element = "Test Test"
        registration_page.username_element = "autoTester"
        registration_page.password_element = "test"
        registration_page.click_on_submit_button()
        time.sleep(1.7)
        assert registration_page.is_invalid_credentials_alert_visible()
        self.wait.until(lambda driver: self.driver.current_url.encode('utf-8') != dashboard_page.url)
        assert (self.driver.current_url.encode(
            'utf-8') != dashboard_page.url), "User is able to register without submitting both checkboxes"



    def tearDown(self):
        self.driver.quit()

    if __name__ == "__main__":
        unittest.main()

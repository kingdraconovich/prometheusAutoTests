import unittest

import time
from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver
from PabeObject import page

class T02_LoginTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def test_T02_01_Login_Page_Elements_Appearance(self):
        main_page = page.MainPage(self.driver)
        login_page = page.LoginPage(self.driver)
        main_page.get()
        main_page.is_main_menu_elements_visible()
        main_page.click_login_menu_entry()
        assert (login_page.url in self.driver.current_url.encode('utf-8'))
        assert login_page.is_email_field_visible()
        assert login_page.is_password_field_visible()
        assert login_page.is_remember_me_checkbox_visible()
        assert login_page.is_submit_button_visible()

    def test_T02_02_Valid_User_Login_Test(self):
        login_page = page.LoginPage(self.driver)
        dashboard_page = page.DashboardPage(self.driver)
        login_page.get()
        login_page.email_element = 'vlad.belogorodskiy@gmail.com'
        login_page.password_element = 'test'
        login_page.click_on_remember_button()
        login_page.click_on_submit_button()
        self.wait.until(lambda driver: self.driver.current_url.encode('utf-8') == dashboard_page.url)
        assert (self.driver.current_url.encode('utf-8') == dashboard_page.url), "User is not able to log in with valid credentials"

    def test_T02_03_Not_Registered_Credentials_Test(self):
        login_page = page.LoginPage(self.driver)
        dashboard_page = page.DashboardPage(self.driver)
        login_page.get()
        login_page.email_element = 'invalid_user@gmail.com'
        login_page.password_element = 'password'
        login_page.click_on_submit_button()
        time.sleep(1)
        assert (self.driver.current_url.encode('utf-8') == login_page.url), "User is logged with not pre-registered credentials"
        assert login_page.is_invalid_credentials_alert_visible()

    def test_T02_04_Invalid_Email_Format_Login_Test(self):
        login_page = page.LoginPage(self.driver)
        dashboard_page = page.DashboardPage(self.driver)
        login_page.get()
        login_page.email_element = 'invalid_user'
        login_page.password_element = 'password'
        login_page.click_on_submit_button()
        time.sleep(1)
        assert (self.driver.current_url.encode('utf-8') == login_page.url), "User is logged with invalid email format"
        assert login_page.is_invalid_credentials_alert_visible()

    def test_T02_05_No_Credentials_Login_Test(self):
        login_page = page.LoginPage(self.driver)
        dashboard_page = page.DashboardPage(self.driver)
        login_page.get()
        login_page.click_on_submit_button()
        time.sleep(1)
        assert (self.driver.current_url.encode('utf-8') == login_page.url), "User is logged without entering credentials"
        assert login_page.is_invalid_credentials_alert_visible()


    def tearDown(self):
        self.driver.quit()


    if __name__ == "__main__":
        unittest.main()
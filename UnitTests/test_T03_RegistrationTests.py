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

    def tearDown(self):
        self.driver.quit()

    if __name__ == "__main__":
        unittest.main()
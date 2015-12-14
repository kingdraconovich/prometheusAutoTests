# -*- coding: utf-8 -*-

import unittest

from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver
from PabeObject import page


class T01_Main_Page_Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def test_T01_01_Main_Page_Elements_Appearance(self):
        main_page = page.MainPage(self.driver)
        main_page.get()
        assert main_page.is_title_matches()
        self.wait.until(lambda driver: main_page.is_main_text_visible())
        assert main_page.is_main_text_visible()
        self.wait.until(lambda driver: main_page.is_description_text_visible())
        assert main_page.is_description_text_visible()
        self.wait.until(lambda driver: main_page.is_findout_button_visible())
        assert main_page.is_findout_button_visible()
        self.wait.until(lambda driver: main_page.is_start_button_visible())
        assert main_page.is_start_button_visible()

    def test_T01_02_Headers_Menu_Elements_Appearance(self):
        main_page = page.MainPage(self.driver)
        main_page.get()
        assert main_page.is_main_menu_elements_visible()

    def test_T01_03_Static_Header_Menu_Elements_Appearance(self):
        main_page = page.MainPage(self.driver)
        main_page.get()
        self.driver.execute_script("window.scrollTo(0, 400)")
        assert main_page.is_main_menu_elements_visible()

    def tearDown(self):
        self.driver.quit()

    if __name__ == "__main__":
        unittest.main()

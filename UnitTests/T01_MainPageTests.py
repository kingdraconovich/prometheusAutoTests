#-*- coding: utf-8 -*-

import unittest

import time
from selenium import webdriver
from PabeObject import page


class T01_01_Main_Page_Tests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://prometheus.org.ua")
        self.driver.maximize_window()

    def test_T01_01_Main_Page_Elements_Appearance(self):
        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches()
        time.sleep(1)
        assert main_page.is_main_text_visible()
        assert main_page.is_description_text_visible()

    def test_T01_02_Headers_Menu_Elements_Appearance(self):
        main_page = page.MainPage(self.driver)
        assert main_page.is_main_menu_elements_visible()

    def tearDown(self):
        self.driver.quit()

    if __name__ == "__main__":
        unittest.main()
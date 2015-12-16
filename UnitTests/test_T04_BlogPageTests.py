import time

__author__ = 'vbilohorodskyi'

import unittest

from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver
from PabeObject import page

class T04_Blog_Page_Tests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def test_T04_01_Blog_Page_Elements_Appearance(self):
        blog_page = page.BlogPage(self.driver)
        blog_page.get()
        assert blog_page.is_blog_page_elements_visible(), "Not all of the main blog page elements is visible"

    def test_T04_02_Search_For_Articles(self):
        blog_page = page.BlogPage(self.driver)
        blog_page.get()
        assert blog_page.is_search_field_visible()
        assert blog_page.is_submit_search_button_visible()
        blog_page.search_element = "prometheus"
        blog_page.click_on_submit_search_button()
        time.sleep(0.6)
        assert blog_page.is_url_contains_search_query() #crashes right here
        assert blog_page.is_search_results_visible()

    def tearDown(self):
        self.driver.quit()

    if __name__ == "__main__":
        unittest.main()

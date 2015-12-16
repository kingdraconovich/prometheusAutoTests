## -*- coding: utf-8 -*-
__author__ = 'vbilohorodskyi'

import time
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

    #
    # NOTE: Search tests are stable only with english search queries, fitting them to cyrillic compatibility would cause
    # a tons of a junk code. It's easier to verify cyrillic search compatibility using manual testing according to
    # following test-cases
    #

    def test_T04_02_Search_For_Articles_With_Results_Found(self):
        blog_page = page.BlogPage(self.driver)
        blog_page.get()
        assert blog_page.is_search_field_visible()
        assert blog_page.is_submit_search_button_visible()
        search_string = "prometheus"
        blog_page.search_element = search_string
        blog_page.click_on_submit_search_button()
        time.sleep(0.6)
        assert search_string in self.driver.current_url.encode('utf-8'), "Generated URL does not contains search query"
        time.sleep(0.6)
        assert blog_page.is_search_results_visible(), "There are no matches despite that the search query is valid"


    def test_T04_03_Search_For_Articles_With_No_Results_Found(self):
        blog_page = page.BlogPage(self.driver)
        blog_page.get()
        assert blog_page.is_search_field_visible()
        assert blog_page.is_submit_search_button_visible()
        search_string = "Some random string that will never return serch results"
        blog_page.search_element = search_string
        blog_page.click_on_submit_search_button()
        time.sleep(0.6)
        assert search_string.replace(' ', '+') in self.driver.current_url.encode(
            'utf-8'), "Generated URL does not contains search query"
        time.sleep(0.6)
        assert blog_page.is_not_found_block_elements_visible(), "Block with error explanation is not visible"
        assert not blog_page.is_search_results_visible(), "There are existing matches, despite that the search query is valid"

    def test_T04_04_Search_For_Valid_Articles_From_No_Results_Found(self):
        blog_page = page.BlogPage(self.driver)
        self.test_T04_03_Search_For_Articles_With_No_Results_Found()
        search_string = "prometheus"
        blog_page.search_element = search_string
        blog_page.click_on_submit_search_button()
        time.sleep(0.6)
        assert search_string in self.driver.current_url.encode('utf-8'), "Generated URL does not contains search query"
        time.sleep(0.6)
        assert blog_page.is_search_results_visible(), "There are no matches despite that the search query is valid"

    def tearDown(self):
        self.driver.quit()

    if __name__ == "__main__":
        unittest.main()

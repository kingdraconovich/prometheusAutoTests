# -*- coding: utf-8 -*-

from element import BasePageElement
from locators import MainPageLocators

class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):

    def is_title_matches(self):
        title = "Prometheus – масові безкоштовні онлайн-курси"
        return (title in self.driver.title.encode('utf-8'))


    def is_main_menu_elements_visible(self):
        assert self.driver.find_element(*MainPageLocators.LOGO).is_displayed()
        assert self.driver.find_element(*MainPageLocators.MAIN_MENU_ENTRY).is_displayed()
        assert self.driver.find_element(*MainPageLocators.COURSES_MENU_ENTRY).is_displayed()
        assert self.driver.find_element(*MainPageLocators.SPECS_MENU_ENTRY).is_displayed()
        assert self.driver.find_element(*MainPageLocators.ABOUT_MENU_ENTRY).is_displayed()
        assert self.driver.find_element(*MainPageLocators.MEDIA_MENU_ENTRY).is_displayed()
        assert self.driver.find_element(*MainPageLocators.BLOG_MENU_ENTRY).is_displayed()
        assert self.driver.find_element(*MainPageLocators.LOGIN_MENU_ENTRY).is_displayed()
        assert self.driver.find_element(*MainPageLocators.LOGIN_ICON).is_displayed()
        assert self.driver.find_element(*MainPageLocators.REGISTER_ICON).is_displayed()
        return True

    def is_main_text_visible(self):
        return self.driver.find_element(*MainPageLocators.MAIN_TEXT).is_displayed()

    def is_description_text_visible(self):
        return self.driver.find_element(*MainPageLocators.DESCRIPTION_TEXT).is_displayed()

    def click_main_menu_entry(self):
        element = self.driver.find_element(*MainPageLocators.MAIN_MENU_ENTRY)
        element.click()

    def click_courses_menu_entry(self):
        element = self.driver.find_element(*MainPageLocators.COURSES_MENU_ENTRY)
        element.click()

    def click_cycles_menu_entry(self):
        element = self.driver.find_element(*MainPageLocators.SPECS_MENU_ENTRY)
        element.click()

    def click_about_menu_entry(self):
        element = self.driver.find_element(*MainPageLocators.ABOUT_MENU_ENTRY)
        element.click()

    def click_media_menu_entry(self):
        element = self.driver.find_element(*MainPageLocators.MEDIA_MENU_ENTRY)
        element.click()

    def click_blog_menu_entry(self):
        element = self.driver.find_element(*MainPageLocators.BLOG_MENU_ENTRY)
        element.click()

    def click_login_menu_entry(self):
        element = self.driver.find_element(*MainPageLocators.LOGIN_MENU_ENTRY)
        element.click()

    def click_register_menu_entry(self):
        element = self.driver.find_element(*MainPageLocators.REGISTER_MENU_ENTRY)
        element.click()
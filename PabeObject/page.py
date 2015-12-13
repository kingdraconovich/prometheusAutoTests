# -*- coding: utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait

from element import BasePageElement
from locators import *


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def get(self):
        self.driver.get(self.url)


class EmailElement(BasePageElement):
    locator = '//input[@id="email"]'


class PasswordElement(BasePageElement):
    locator = "//input[@id='password']"


class MainPage(BasePage):

    url = "http://prometheus.org.ua"

    def get_main_page(self):
        self.driver.get(self.url)

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

    def is_findout_button_visible(self):
        return self.driver.find_element(*MainPageLocators.FINDOUT_BUTTON).is_displayed()

    def is_start_button_visible(self):
        return self.driver.find_element(*MainPageLocators.START_BUTTON).is_displayed()

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


class LoginPage(BasePage):

    url = "http://courses.prometheus.org.ua/login"

    email_element = EmailElement()
    password_element = PasswordElement()

    def is_remember_me_checkbox_visible(self):
        return self.driver.find_element(*LoginPageLocators.REMEMBER_ME_CHECKBOX)

    def is_email_field_visible(self):
        return self.driver.find_element(*LoginPageLocators.EMAIL_FIELD).is_displayed()

    def is_password_field_visible(self):
        return self.driver.find_element(*LoginPageLocators.PASSWORD_FIELD).is_displayed()

    def is_submit_button_visible(self):
        return self.driver.find_element(*LoginPageLocators.SUBMIT_BUTTON).is_displayed()

    def click_on_remember_button(self):
        self.driver.find_element(*LoginPageLocators.REMEMBER_ME_CHECKBOX).click()

    def click_on_submit_button(self):
        self.driver.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()

    def is_invalid_credentials_alert_visible(self):
        return self.driver.find_element(*LoginPageLocators.ALERT_INVALID_USER).is_displayed()


class DashboardPage(BasePage):
    url = "http://courses.prometheus.org.ua/dashboard"
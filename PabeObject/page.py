# -*- coding: utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait

from element import *
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

    def click_on_main_menu_entry(self):
        element = self.driver.find_element(*MainPageLocators.MAIN_MENU_ENTRY)
        element.click()

    def click_on_courses_menu_entry(self):
        element = self.driver.find_element(*MainPageLocators.COURSES_MENU_ENTRY)
        element.click()

    def click_on_cycles_menu_entry(self):
        element = self.driver.find_element(*MainPageLocators.SPECS_MENU_ENTRY)
        element.click()

    def click_on_about_menu_entry(self):
        element = self.driver.find_element(*MainPageLocators.ABOUT_MENU_ENTRY)
        element.click()

    def click_on_media_menu_entry(self):
        element = self.driver.find_element(*MainPageLocators.MEDIA_MENU_ENTRY)
        element.click()

    def click_on_blog_menu_entry(self):
        element = self.driver.find_element(*MainPageLocators.BLOG_MENU_ENTRY)
        element.click()

    def click_on_login_menu_entry(self):
        element = self.driver.find_element(*MainPageLocators.LOGIN_MENU_ENTRY)
        element.click()

    def click_on_register_menu_entry(self):
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

    def click_on_remember_me_checkbox(self):
        self.driver.find_element(*LoginPageLocators.REMEMBER_ME_CHECKBOX).click()

    def click_on_submit_button(self):
        self.driver.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()

    def is_invalid_credentials_alert_visible(self):
        return self.driver.find_element(*LoginPageLocators.ALERT_INVALID_LOGIN).is_displayed()


class NameElement(BasePageElement):
    locator = '//input[@id="name"]'


class UsernameElement(BasePageElement):
    locator = '//input[@id="username"]'


class EducationElement(BaseSelectElement):
    locator = "//select[@id='education-level']"


class GenderElement(BaseSelectElement):
    locator = "//select[@id='gender']"


class BirthYearlement(BaseSelectElement):
    locator = "//select[@id='yob']"


class MailingAddressElement(BasePageElement):
    locator = '//textarea[@id="address-mailing"]'


class GoalsArea(BasePageElement):
    locator = '//textarea[@id="goals"]'


class RegistrationPage(BasePage):
    url = "http://courses.prometheus.org.ua/register"

    email_element = EmailElement()
    name_element = NameElement()
    username_element = UsernameElement()
    password_element = PasswordElement()
    education_element = EducationElement()
    gender_element = GenderElement()
    birth_year_element = BirthYearlement()
    mailing_address_area = MailingAddressElement()
    goals_area = GoalsArea()

    def is_email_element_visible(self):
        return self.driver.find_element(*RegistrationPageLocators.EMAIL_FIELD).is_displayed()

    def is_name_element_visible(self):
        return self.driver.find_element(*RegistrationPageLocators.NAME_FIELD).is_displayed()

    def is_username_element_visible(self):
        return self.driver.find_element(*RegistrationPageLocators.USERNAME_FIELD).is_displayed()

    def is_password_element_visible(self):
        return self.driver.find_element(*RegistrationPageLocators.PASSWORD_FIELD).is_displayed()

    def is_education_element_visible(self):
        return self.driver.find_element(*RegistrationPageLocators.EDUCATION_LEVEL_SELECT).is_displayed()

    def is_gender_element_visible(self):
        return self.driver.find_element(*RegistrationPageLocators.GENDER_LEVEL_SELECT).is_displayed()

    def is_birth_year_element_visible(self):
        return self.driver.find_element(*RegistrationPageLocators.YEAR_OF_BIRTH_SELECT).is_displayed()

    def is_mailing_adress_area_visible(self):
        return self.driver.find_element(*RegistrationPageLocators.ADDRESS_TEXT_AREA).is_displayed()

    def is_goals_area_visible(self):
        return self.driver.find_element(*RegistrationPageLocators.GOALS_TEXT_AREA).is_displayed()

    def is_terms_of_service_checkbox_visible(self):
        return self.driver.find_element(*RegistrationPageLocators.TERMS_OF_SERVICE_CHECKBOX).is_displayed()

    def is_honor_code_checkbox_visible(self):
        return self.driver.find_element(*RegistrationPageLocators.HONOR_CODE_CHECKBOX).is_displayed()

    def is_submit_button_visible(self):
        return self.driver.find_element(*RegistrationPageLocators.SUBMIT_BUTTON).is_displayed()

    def is_registration_page_elements_visible(self):
        assert self.is_email_element_visible()
        assert self.is_name_element_visible()
        assert self.is_username_element_visible()
        assert self.is_password_element_visible()
        assert self.is_education_element_visible()
        assert self.is_gender_element_visible()
        assert self.is_birth_year_element_visible()
        assert self.is_mailing_adress_area_visible()
        assert self.is_goals_area_visible()
        assert self.is_terms_of_service_checkbox_visible()
        assert self.is_honor_code_checkbox_visible()
        assert self.is_submit_button_visible()
        return True

    def click_on_terms_of_service_checkbox(self):
        self.driver.find_element(*RegistrationPageLocators.TERMS_OF_SERVICE_CHECKBOX).click()

    def click_on_honor_code_checkbox(self):
        self.driver.find_element(*RegistrationPageLocators.HONOR_CODE_CHECKBOX).click()

    def click_on_submit_button(self):
        self.driver.find_element(*RegistrationPageLocators.SUBMIT_BUTTON).click()

    def is_invalid_credentials_alert_visible(self):
        return self.driver.find_element(*RegistrationPageLocators.ALERT_INVALID_REGISTRATION).is_displayed()

    def click_on_snippet_login_button(self):
        self.driver.find_element(*RegistrationPageLocators.SNIPPET_LOGIN_BUTTON).click()

    def click_on_header_login_button(self):
        self.driver.find_element(*RegistrationPageLocators.HEADER_LOGIN_BUTTON).click()


class DashboardPage(BasePage):
    url = "http://courses.prometheus.org.ua/dashboard"


class SearchElement(BasePageElement):
    locator = "//input[@id='s']"


class BlogPage(BasePage):
    url = "http://prometheus.org.ua/blog"
    search_element = SearchElement()

    def is_header_text_visible(self):
        return self.driver.find_element(*BlogPageLocators.HEADER_TEXT_BLOCK).is_displayed()

    def is_search_field_visible(self):
        return self.driver.find_element(*BlogPageLocators.SEARCH_FIELD).is_displayed()

    def is_submit_search_button_visible(self):
        return self.driver.find_element(*BlogPageLocators.SUBMIT_SEARCH_BUTTON).is_displayed()

    def is_articles_visible(self):
        for element in self.driver.find_elements(*BlogPageLocators.ARTICLE):
            if element.is_displayed():
                pass
        return True

    def is_vk_widget_visible(self):
        return self.driver.find_element(*BlogPageLocators.VK_WIDGET).is_displayed()

    def is_facebook_widget_visible(self):
        return self.driver.find_element(*BlogPageLocators.FACEBOOK_WIDGET).is_displayed()

    def is_twitter_widget_visible(self):
        return self.driver.find_element(*BlogPageLocators.TWITTER_WIDGET).is_displayed()

    def is_tag_cloud_visible(self):
        return self.driver.find_element(*BlogPageLocators.TAG_CLOUD).is_displayed()

    def is_current_page_number_visible(self):
        return self.driver.find_element(*BlogPageLocators.CURRENT_PAGE_ENTRY).is_displayed()

    def is_next_page_entry_visible(self):
        return self.driver.find_element(*BlogPageLocators.NEXT_PAGE_ENTRY).is_displayed()

    def is_previous_page_entry_visible(self):
        return self.driver.find_element(*BlogPageLocators.PREVIOUS_PAGE_ENTRY).is_displayed()

    def is_blog_page_elements_visible(self):
        assert self.is_header_text_visible()
        assert self.is_search_field_visible()
        assert self.is_submit_search_button_visible()
        assert self.is_articles_visible()
        assert self.is_vk_widget_visible()
        assert self.is_facebook_widget_visible()
        assert self.is_twitter_widget_visible()
        assert self.is_tag_cloud_visible()
        assert self.is_current_page_number_visible()
        assert self.is_next_page_entry_visible()
        if "/page/" in self.driver.current_url.encode('utf-8'):
            assert self.is_previous_page_entry_visible(*BlogPageLocators.PREVIOUS_PAGE_ENTRY)
        return True

    def click_on_submit_search_button(self):
        self.driver.find_element(*BlogPageLocators.SUBMIT_SEARCH_BUTTON).click()

    def click_on_next_page_entry_button(self):
        self.driver.find_element(*BlogPageLocators.NEXT_PAGE_ENTRY).click()

        # def is_url_contains_search_query(self):
        # return self.search_element in self.driver.current_url #this is not working. To fix.

    def is_search_results_visible(self):
        for element in self.driver.find_elements(*BlogPageLocators.SEARCH_RESULT):
            if element.is_displayed():
                pass
        return True
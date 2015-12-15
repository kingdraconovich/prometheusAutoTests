# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By


class MainPageLocators(object):
    # Header menu locators
    LOGO = (By.XPATH, "//img[contains(@src, 'http://prometheus.org.ua/wp-content/uploads/2014/09/logo')]")
    MAIN_MENU_ENTRY = (By.XPATH, "//ul[contains(@id, 'menu-main-menu-1')]/li/a[@href='http://prometheus.org.ua/']")
    COURSES_MENU_ENTRY = (
        By.XPATH, "//ul[contains(@id, 'menu-main-menu-1')]/li/a[@href='http://prometheus.org.ua/courses/']")
    SPECS_MENU_ENTRY = (
        By.XPATH, "//ul[contains(@id, 'menu-main-menu-1')]/li/a[@href='http://prometheus.org.ua/cycles/']")
    ABOUT_MENU_ENTRY = (
        By.XPATH, "//ul[contains(@id, 'menu-main-menu-1')]/li/a[@href='http://prometheus.org.ua/about-us/']")
    MEDIA_MENU_ENTRY = (
        By.XPATH, "//ul[contains(@id, 'menu-main-menu-1')]/li/a[@href='http://prometheus.org.ua/prometheus-start/']")
    BLOG_MENU_ENTRY = (By.XPATH, "//ul[contains(@id, 'menu-main-menu-1')]/li/a[@href='http://prometheus.org.ua/blog/']")
    LOGIN_MENU_ENTRY = (
        By.XPATH, "//ul[contains(@id, 'menu-main-menu-1')]/li/a[@href='http://edx.prometheus.org.ua/login']")
    LOGIN_ICON = (By.XPATH,
                  "//ul[contains(@id, 'menu-main-menu-1')]/li/a[@href='http://edx.prometheus.org.ua/login']/i[@class='icon-signin']")
    REGISTER_MENU_ENTRY = (
        By.XPATH, "//ul[contains(@id, 'menu-main-menu-1')]/li/a[@href='http://edx.prometheus.org.ua/register']")
    REGISTER_ICON = (By.XPATH,
                     "//ul[contains(@id, 'menu-main-menu-1')]/li/a[@href='http://edx.prometheus.org.ua/register']/i[@class='icon-group']")

    # Mid page elements locators
    MAIN_TEXT = (By.XPATH, "//div[contains(., 'Найкраща освіта для кожного') and contains(@data-ease, 'easeOutQuint')]")
    DESCRIPTION_TEXT = (By.XPATH,
                        "//div[contains(., 'Безкоштовні онлайн-курси від викладачів КНУ, КПІ та Києво-Могилянської академії') and contains(@data-ease, 'easeOutQuint')]")
    FINDOUT_BUTTON = (By.XPATH, "//div/a[contains(@onclick, 'scroll(0,600)')]/ancestor::div[1]")
    START_BUTTON = (By.XPATH, "//div/a[contains(@href, 'http://edx.prometheus.org.ua/register')]/ancestor::div[1]")


class LoginPageLocators():
    REMEMBER_ME_CHECKBOX = (By.XPATH, "//input[@id='remember-yes']")
    EMAIL_FIELD = (By.XPATH, "//input[@id='email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@id='password']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@id='submit']")
    ALERT_INVALID_LOGIN = (By.XPATH, "//div[contains(@class, 'submission-error')]")


class RegistrationPageLocators():
    EMAIL_FIELD = (By.XPATH, "//input[@id='email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@id='password']")
    NAME_FIELD = (By.XPATH, "//input[@id='name']")
    USERNAME_FIELD = (By.XPATH, "//input[@id='username']")
    ADDRESS_TEXT_AREA = (By.XPATH, "//ol/li/textarea[@id='address-mailing']")
    GOALS_TEXT_AREA = (By.XPATH, "//ol/li/textarea[@id='goals']")
    EDUCATION_LEVEL_SELECT = (By.XPATH, "//select[@id='education-level']")
    GENDER_LEVEL_SELECT = (By.XPATH, "//select[@id='gender']")
    YEAR_OF_BIRTH_SELECT = (By.XPATH, "//select[@id='yob']")
    TERMS_OF_SERVICE_CHECKBOX = (By.XPATH, "//input[@id='tos-yes']")
    HONOR_CODE_CHECKBOX = (By.XPATH, "//input[@id='honorcode-yes']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@id='submit']")
    ALERT_INVALID_REGISTRATION = (By.XPATH, "//div[contains(@class, 'submission-error')]")
    SNIPPET_LOGIN_BUTTON = (By.XPATH, "//p/a[contains(@class, 'login')]")
    HEADER_LOGIN_BUTTON = (By.XPATH, "//li/a[contains(@class, 'login')]")


class BlogPageLocators():
    HEADER_TEXT_BLOCK = (By.XPATH, "//h1[text()='Блог']")
    SEARCH_FIELD = (By.XPATH, "//input[@id='s']")
    SUBMIT_SEARCH_BUTTON = (By.XPATH, "//input[@id='searchsubmit']")
    ARTICLE = (By.XPATH, "//article")
    VK_WIDGET = (By.XPATH, "//div[@id='vk_groups']")
    FACEBOOK_WIDGET = (
    By.XPATH, "//*[@id='text-2']/div[2]/iframe[1]")  # this is an automatically generated Xpath. Might be unstable
    TWITTER_WIDGET = (By.XPATH, "//iframe[@id='twitter-widget-0']")

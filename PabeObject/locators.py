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
    #Login page elements locators
    REMEMBER_ME_CHECKBOX = (By.XPATH, "//input[@id='remember-yes']")
    EMAIL_FIELD = (By.XPATH, "//input[@id='email']")
    PASSWORD_FIELD = (By.XPATH, "//input[@id='password']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@id='submit']")
    ALERT_INVALID_USER = (By.XPATH, "//div[text()='Виникли помилки при вході. Можливо, невірний email або пароль.']")
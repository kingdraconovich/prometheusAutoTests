# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By

class MainPageLocators(object):

    # Header menu locators
    LOGO = (By.XPATH, "//img[@src='http://prometheus.org.ua/wp-content/uploads/2014/09/logo_white_wp.png']")
    MAIN_MENU_ENTRY = (By.XPATH, "//ul[contains(@id, 'menu-main-menu-1')]/li/a[@href='http://prometheus.org.ua/']")
    COURSES_MENU_ENTRY = (By.XPATH, "//ul[contains(@id, 'menu-main-menu-1')]/li/a[@href='http://prometheus.org.ua/courses/']")
    SPECS_MENU_ENTRY = (By.XPATH, "//ul[contains(@id, 'menu-main-menu-1')]/li/a[@href='http://prometheus.org.ua/cycles/']")
    ABOUT_MENU_ENTRY = (By.XPATH, "//ul[contains(@id, 'menu-main-menu-1')]/li/a[@href='http://prometheus.org.ua/about-us/']")
    MEDIA_MENU_ENTRY = (By.XPATH, "//ul[contains(@id, 'menu-main-menu-1')]/li/a[@href='http://prometheus.org.ua/prometheus-start/']")
    BLOG_MENU_ENTRY = (By.XPATH, "//ul[contains(@id, 'menu-main-menu-1')]/li/a[@href='http://prometheus.org.ua/blog/']")
    LOGIN_MENU_ENTRY = (By.XPATH, "//ul[contains(@id, 'menu-main-menu-1')]/li/a[@href='http://edx.prometheus.org.ua/login']")
    LOGIN_ICON = (By.XPATH, "//ul[contains(@id, 'menu-main-menu-1')]/li/a[@href='http://edx.prometheus.org.ua/login']/i[@class='icon-signin']")
    REGISTER_MENU_ENTRY = (By.XPATH, "//ul[contains(@id, 'menu-main-menu-1')]/li/a[@href='http://edx.prometheus.org.ua/register']")
    REGISTER_ICON = (By.XPATH, "//ul[contains(@id, 'menu-main-menu-1')]/li/a[@href='http://edx.prometheus.org.ua/register']/i[@class='icon-group']")


    #Mid page elements locators
    MAIN_TEXT = (By.XPATH, "//div[contains(., 'Найкраща освіта для кожного') and contains(@data-ease, 'easeOutQuint')]")
    DESCRIPTION_TEXT = (By.XPATH, "//div[contains(., 'Безкоштовні онлайн-курси від викладачів КНУ, КПІ та Києво-Могилянської академії') and contains(@data-ease, 'easeOutQuint')]")
    ##FINDOUT_BUTTON = (By.XPATH, )

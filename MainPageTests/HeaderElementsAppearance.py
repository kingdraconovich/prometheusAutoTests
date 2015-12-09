# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import unittest



class AppearanceTest(unittest.TestCase):

    #Prerequisites
    #1. Open Browser: Google Chrome
    #2. Site: prometheus.org
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://prometheus.org.ua")

    def test_logoAppearance(self):

    #Summary: to verify Prometheus Logo on the main page
    #
    #Steps:
    #1. Check the Prometheus logo
    #
    #Expected results:
    #1. Logo appears

        driver = self.driver

        logoXpath = "//div/a/img[@src='http://prometheus.org.ua/wp-content/uploads/2014/09/logo_white_wp.png']"

        logoElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(logoXpath))

    def test_menuElementsAppearance(self):

    #Summary: to verify all of the menu entries and linked icons are present on the main page
    #
    #Steps:
    #1. Check if the "Головна" menu entry available
    #2. Check if the "Курси" menu entry available
    #3. Check if the "Цикли курсів" menu entry available
    #4. Check if the "Для ЗМІ" menu entry available
    #5. Check if the "Блог" menu entry available
    #6. Check if the "Увійти" menu entry available
    #7. Check if the linked login icon is present
    #8. Check if the "Зареєструватися" menu entry available
    #9. Check if the linked register icon is present
    #
    #Expected results:
    #1. All menu entries are available
    #2. All linked icons are present

        driver = self.driver

        main_MenuEntryXpath = "//a[contains(., 'Головна')]"
        cources_MenuEntryXpath = "//a[contains(., 'Курси')]"
        cycles_MenuEntryXpath = "//a[contains(., 'Цикли') and contains(., 'курсів')]"
        media_MenuEntryXpath = "//a[contains(., 'Для') and contains(., 'ЗМІ')]"
        blog_MenuEntryXpath = "//a[contains(., 'Блог')]"
        login_MenuEntryXpath = "//a[contains(., 'Увійти')]"
        loginIcon_MenuXpath = "//i[@class='icon-signin']"
        register_MenuEntryXpath = "//a[contains(., 'Зареєструватися')]"
        registerIcon_MenuXpath = "//i[@class='icon-group']"

        main_MenuEntryElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(main_MenuEntryXpath))
        cources_MenuEntryElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(cources_MenuEntryXpath))
        cycles_MenuEntryElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(cycles_MenuEntryXpath))
        media_MenuEntryElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(media_MenuEntryXpath))
        blog_MenuEntryElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(blog_MenuEntryXpath))
        login_MenuEntryElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(login_MenuEntryXpath))
        loginIcon_MenuEntryElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(loginIcon_MenuXpath))
        register_MenuEntryElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(register_MenuEntryXpath))
        registerIcon_MenuEntryElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(registerIcon_MenuXpath))

    def test_topBackgroundImageAppearance(self):

    #Summary: To verify Top background image appearance
    #
    #Steps:
    #1. Verify if top background image appears
    #
    #Expected results:
    #1. Top background image appears

        driver = self.driver

        topBackgroundImageXpath = "//div/img[@src='http://prometheus.org.ua/wp-content/uploads/2014/09/work-watermark-1920x1080-09.jpg']"

        topBackgroundImageElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(topBackgroundImageXpath))

    def test_textAppearanceAndValidation(self):

    #Summary: To verify presence of main text and validate it
    #
    #Steps:
    #1. Verify that the header section title appears with content: "Найкраща освіта для кожного"
    #2. Verify that the header secition description text appears with content: "Безкоштовні онлайн-курси від викладачів КНУ,
    #КПІ та Києво-Могилянської академії "
    #3. Check that the title is larger than the description text.

        driver = self.driver

        textTitleXpath = "//div/div/div/div/div/div/div/div/div/div/div[contains(., 'Найкраща') " \
                         "and contains(., 'освіта') and contains(., 'для') and contains(., 'кожного')]"

        textDesctiptionXpath = "//div/div/div/div/div/div/div/div/div/div/div[contains(., 'Безкоштовні')" \
                               " and contains(., 'онлайн-курси') and contains(., 'від') and contains(., 'викладачів')" \
                               " and contains(., 'КНУ') and contains(., 'КПІ') and contains(., 'та')" \
                               " and contains(., 'Києво-Могилянської')and contains(., 'академії')]"

        textTitleElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(textTitleXpath))
        textDescriptionElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(textDesctiptionXpath))

        titleSize = driver.find_element_by_xpath(textTitleXpath).value_of_css_property("font-size")
        descriptionSize = driver.find_element_by_xpath(textDesctiptionXpath).value_of_css_property("font-size")

        assert (titleSize > descriptionSize)



    def tearDown(self):
        self.driver.quit()

    if __name__ == "__main__":
        unittest.main()
# -*- coding: utf-8 -*-
import unittest
import time
import random
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


# basic actions methods realization

# user login method
def user_login(self, emailStr, passwordStr, driver):
    wait = self.wait

    emailField = driver.find_element_by_id("email")
    passwordField = driver.find_element_by_id("password")

    wait.until(lambda driver: emailField)
    wait.until(lambda driver: passwordField)
    emailField.clear()
    passwordField.clear()
    emailField.send_keys(emailStr)
    passwordField.send_keys(passwordStr)
    driver.find_element_by_id("remember-yes").click()
    driver.find_element_by_id("submit").click()


# method that solves domains conversion problem
def convert_subdomains(courseUrl):
    editedCourseUrl = "http://courses" + courseUrl.encode('utf-8')[10:]
    print("WARNING: Issue with subdomains!")
    print("Initial string: " + courseUrl.encode('utf-8'))
    print("Edited string: " + editedCourseUrl)
    courseUrl = editedCourseUrl
    return courseUrl


class Registration:
    randomID = str(random.randint(1, 1000))
    emailStr = "test_email" + randomID + "@gmail.com"
    passwordStr = "test"
    nameStr = "Test Test"
    usernameStr = "autoTester" + randomID

    # Values for drop-down lists
    educationChoice = "Немає"
    genderChoice = "Інше"
    yobChoice = "1949"

    # Values for text areas
    mailingAdressStr = "Somewhere, over the rainbow"
    goalsStr = "I am just a little robot, trying to test your site"

    def verify_and_register(self):
        driver = self.driver
        wait = self.wait
        register_MenuEntryXpath = "//a[@href='http://edx.prometheus.org.ua/register']"
        registerButton = driver.find_element_by_xpath(register_MenuEntryXpath)
        wait.until(lambda driver: registerButton)
        driver.get("http://edx.prometheus.org.ua/register")

    def enter_email(self, emailStr):
        emailField = self.driver.find_element_by_xpath("//li/input[@id='email']")
        self.wait.until(lambda driver: emailField)
        self.emailField.clear()
        self.emailField.send_keys(emailStr)
        time.sleep(1)

    def enter_name(self, nameStr):
        nameField = self.driver.find_element_by_xpath("//li/input[@id='name']")
        self.wait.until(lambda driver: nameField)
        self.nameField.clear()
        self.nameField.send_keys(nameStr)
        time.sleep(1)

    def enter_username(self, usernameStr):
        usernameField = webdriver.find_element_by_xpath("//li/input[@id='username']")
        self.wait.until(lambda driver: usernameField)
        self.usernameField.clear()
        self.usernameField.send_keys(usernameStr)
        time.sleep(1)

    def enter_password(self, passwordStr):
        passwordField = self.driver.find_element_by_xpath("//li/input[@id='password']")
        self.wait.until(lambda driver: passwordField)
        self.passwordField.clear()
        self.passwordField.send_keys(passwordStr)
        time.sleep(1)

    def fill_education_list(self):
        educationDDList = self.driver.find_element_by_xpath("//li/div/select[@id='education-level']")
        self.wait.until(lambda driver: educationDDList)
        Select(self.educationDDList).select_by_visible_text(self.educationChoice)
        time.sleep(1)

    def fill_gender_list(self):
        genderDDList = self.driver.find_element_by_xpath("//li/div/select[@id='gender']")
        self.wait.until(lambda driver: genderDDList)
        Select(self.genderDDList).select_by_visible_text(self.genderChoice)
        time.sleep(1)

    def fill_birth_year_list(self):
        yobDDList = self.driver.find_element_by_xpath("//li/div/select[@id='yob']")
        self.wait.until(lambda driver: yobDDList)
        Select(self.yobDDList).select_by_visible_text(self.yobChoice)
        time.sleep(1)

    def fill_mailing_adress_area(self, mailingAdressStr):
        mailingAdressField = self.driver.find_element_by_xpath("//ol/li/textarea[@id='address-mailing']")
        self.wait.until(lambda driver: mailingAdressField)
        self.mailingAdressField.clear()
        self.mailingAdressField.send_keys(mailingAdressStr)
        time.sleep(1)

    def fill_goals_area(self, goalsStr):
        goalsAreaField = self.driver.find_element_by_xpath("//ol/li/textarea[@id='goals']")
        self.wait.until(lambda driver: goalsAreaField)
        self.goalsAreaField.clear()
        self.goalsAreaField.send_keys(goalsStr)
        time.sleep(1)

    def check_terms_of_service_box(self):
        termsOfServiceBox = self.driver.find_element_by_xpath("//div/input[@id='tos-yes']")
        self.wait.until(lambda driver: termsOfServiceBox)
        self.termsOfServiceBox.click()
        time.sleep(1)

    def check_honor_code_box(self):
        honorCodeBox = self.driver.find_element_by_xpath("//div/input[@id='honorcode-yes']")
        self.wait.until(lambda driver: honorCodeBox)
        self.honorCodeBox.click()
        time.sleep(1)

    def registration_submit(self):
        submitButton = self.driver.find_element_by_xpath("//div/button[@id='submit']")
        self.wait.until(lambda driver: submitButton)
        self.submitButton.click()

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
    courseUrl = editedCourseUrl.encode('utf-8')
    return courseUrl


class Registration:

    def __init__(self, driver, courseId, emailStr, passwordStr, nameStr, usernameStr, educationChoice, genderChoice, yobChoice, mailingAdressStr, goalsStr):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

        self.ID = courseId
        self.emailStr = emailStr
        self.passwordStr = passwordStr
        self.nameStr = nameStr
        self.usernameStr = usernameStr

        # Values for drop-down lists
        self.educationChoice = educationChoice
        self.genderChoice = genderChoice
        self.yobChoice = yobChoice

        # Values for text areas
        self.mailingAdressStr = mailingAdressStr
        self.goalsStr = goalsStr


    def verify_and_register(self):
        driver = self.driver
        wait = self.wait
        register_MenuEntryXpath = "//a[@href='http://edx.prometheus.org.ua/register']"
        registerButton = driver.find_element_by_xpath(register_MenuEntryXpath)
        wait.until(lambda driver: registerButton)
        driver.get("http://edx.prometheus.org.ua/register")

    def enter_email(self):
        emailField = self.driver.find_element_by_xpath("//li/input[@id='email']")
        self.wait.until(lambda driver: emailField)
        emailField.clear()
        emailField.send_keys(self.emailStr)
        #time.sleep(1)

    def enter_name(self):
        nameField = self.driver.find_element_by_xpath("//li/input[@id='name']")
        self.wait.until(lambda driver: nameField)
        nameField.clear()
        nameField.send_keys(self.nameStr)
        #time.sleep(1)

    def enter_username(self):
        usernameField = self.driver.find_element_by_xpath("//li/input[@id='username']")
        self.wait.until(lambda driver: usernameField)
        usernameField.clear()
        usernameField.send_keys(self.usernameStr)
        #time.sleep(1)

    def enter_password(self):
        passwordField = self.driver.find_element_by_xpath("//li/input[@id='password']")
        self.wait.until(lambda driver: passwordField)
        passwordField.clear()
        passwordField.send_keys(self.passwordStr)
        #time.sleep(1)

    def fill_education_list(self):
        educationDDList = self.driver.find_element_by_xpath("//li/div/select[@id='education-level']")
        self.wait.until(lambda driver: educationDDList)
        Select(educationDDList).select_by_visible_text(self.educationChoice)
        #time.sleep(1)

    def fill_gender_list(self):
        genderDDList = self.driver.find_element_by_xpath("//li/div/select[@id='gender']")
        self.wait.until(lambda driver: genderDDList)
        Select(genderDDList).select_by_visible_text(self.genderChoice)
        #time.sleep(1)

    def fill_birth_year_list(self):
        yobDDList = self.driver.find_element_by_xpath("//li/div/select[@id='yob']")
        self.wait.until(lambda driver: yobDDList)
        Select(yobDDList).select_by_visible_text(self.yobChoice)
        #time.sleep(1)

    def fill_mailing_adress_area(self):
        mailingAdressField = self.driver.find_element_by_xpath("//ol/li/textarea[@id='address-mailing']")
        self.wait.until(lambda driver: mailingAdressField)
        mailingAdressField.clear()
        mailingAdressField.send_keys(self.mailingAdressStr)
        #time.sleep(1)

    def fill_goals_area(self):
        goalsAreaField = self.driver.find_element_by_xpath("//ol/li/textarea[@id='goals']")
        self.wait.until(lambda driver: goalsAreaField)
        goalsAreaField.clear()
        goalsAreaField.send_keys(self.goalsStr)
        #time.sleep(1)

    def check_terms_of_service_box(self):
        termsOfServiceBox = self.driver.find_element_by_xpath("//div/input[@id='tos-yes']")
        self.wait.until(lambda driver: termsOfServiceBox)
        termsOfServiceBox.click()
        #time.sleep(1)

    def check_honor_code_box(self):
        honorCodeBox = self.driver.find_element_by_xpath("//div/input[@id='honorcode-yes']")
        self.wait.until(lambda driver: honorCodeBox)
        honorCodeBox.click()
        #time.sleep(1)

    def registration_submit(self):
        submitButton = self.driver.find_element_by_xpath("//div/button[@id='submit']")
        self.wait.until(lambda driver: submitButton)
        submitButton.click()
        time.sleep(1)

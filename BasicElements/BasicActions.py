# -*- coding: utf-8 -*-
import unittest
import time
import random
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
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
def convert_subdomains(self, courseUrl):
    editedCourseUrl = "http://courses" + courseUrl.encode('utf-8')[10:]
    print("WARNING: Issue with subdomains!")
    print("Initial string: " + courseUrl.encode('utf-8'))
    print("Edited string: " + editedCourseUrl)
    courseUrl = editedCourseUrl
    return courseUrl

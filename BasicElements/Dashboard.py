# -*- coding: utf-8 -*-
import unittest
import time
import random
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


# method for verification of dashboard elements.
def verify_dashboard_elements(self, emailStr, usernameStr, nameStr, driver):
    wait = self.wait

    wait.until(lambda driver: driver.find_element_by_xpath("//a[contains(., " + usernameStr + ")]"))
    wait.until(lambda driver: driver.find_element_by_xpath("//h1[contains(., " + usernameStr + ")]"))
    wait.until(lambda driver: driver.find_element_by_xpath("//li/span[contains(., " + "'" + nameStr + "')]"))
    wait.until(lambda driver: driver.find_element_by_xpath("//li/span[contains(., " + "'" + emailStr + "')]"))
    wait.until(lambda driver: driver.find_element_by_id("pwd_reset_button"))
    wait.until(lambda driver: driver.find_element_by_xpath(
        "//span/a[contains(., 'редагувати') and @href='#apply_name_change']"))
    wait.until(
        lambda driver: driver.find_element_by_xpath("//span/a[contains(., 'редагувати') and @href='#change_email']"))


# method for initiating dashboard clean-up
def dashboard_cleanup(self, driver):
    wait = self.wait

    print("WARNING!!! WARNING!!!")
    print("Initiating Dashboard clean up")

    subscribedCoursesList = driver.find_elements_by_xpath("//a[contains(@class, 'unenroll')]")

    while len(subscribedCoursesList) > 0:
        wait.until(lambda driver: subscribedCoursesList[0])
        subscribedCoursesList[0].click()
        wait.until(
            lambda driver: driver.find_element_by_xpath("//div/input[contains(@value, 'Відписатись від курсу')]"))
        driver.find_element_by_xpath("//div/input[contains(@value, 'Відписатись від курсу')]").click()
        time.sleep(1)
        subscribedCoursesList = driver.find_elements_by_xpath("//a[contains(@class, 'unenroll')]")
